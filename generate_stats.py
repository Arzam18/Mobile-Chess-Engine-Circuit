import os
import glob
import re
import math
import chess.pgn

MAIN_SEASON_DIR = "seasons/season_3/main"
DEFAULT_RATING = 3000.0
K_FACTOR = 32.0

# 🛠️ ENGINE ALIAS & RENAME MAP
# Maps variations, typos, or previous versions to a unified canonical ID 
# for shared historical Elo and stats continuity.
ENGINE_ALIASES = {
    "hobess": "Hobbes",
    "hobbes 3.0": "Hobbes",
    "hobbes dev": "Hobbes",
}

def calculate_expected_score(r1, r2):
    return 1.0 / (1.0 + 10.0 ** ((r2 - r1) / 400.0))

def get_canonical_name(name):
    """Normalizes engine names using the alias map or falls back to stripping 
    version numbers so updates and renames maintain historical continuity."""
    lower_name = name.strip().lower()
    if lower_name in ENGINE_ALIASES:
        return ENGINE_ALIASES[lower_name]
        
    cleaned = re.sub(r'\s+(?:v?\d+(?:\.\d+)*).*$', '', name, flags=re.IGNORECASE).strip()
    return cleaned if cleaned else name

def parse_move_comments(game):
    """Extract move time from PGN comments if available."""
    clk_times = []
    prev_clk = None
    
    for node in game.mainline():
        comment = node.comment
        if not comment:
            continue
            
        clk_match = re.search(r'\[%clk\s+(\d+):(\d+):(\d+(?:\.\d+)?)\]', comment)
        if clk_match:
            h, m, s = float(clk_match.group(1)), float(clk_match.group(2)), float(clk_match.group(3))
            total_sec = h * 3600 + m * 60 + s
            if prev_clk is not None:
                used_sec = max(0.0, prev_clk - total_sec)
                clk_times.append(used_sec)
            prev_clk = total_sec

    avg_time = round(sum(clk_times) / len(clk_times), 2) if clk_times else None
    return avg_time

def get_mcec_stage_status(idx, stage_type, total_engines):
    """Calculates Global Rank and Status Badges according to MCEC Season 3 Structure Rules."""
    rank = idx + 1  
    half_cutoff = math.ceil(total_engines / 2.0)

    if "gateway" in stage_type:
        if rank <= half_cutoff:
            return rank + 36, "🟢 Advanced to Entry League"
        else:
            return rank + 36, "🔴 Relegated to The Survival"

    elif "entry" in stage_type:
        if rank <= half_cutoff:
            return rank, "🟢 Promoted to Foundation"
        else:
            return rank + 36, "🔴 Relegated to Gatekeeper / Fringe"

    elif "league_4" in stage_type or "league4" in stage_type or "l4" in stage_type:
        if rank <= 6:
            return rank + 24, "🟢 Promoted to League 3"
        else:
            return rank + 24, "🔴 Relegated"

    elif "league_3" in stage_type or "league3" in stage_type or "l3" in stage_type:
        if rank <= 6:
            return rank + 18, "🟢 Promoted to League 2"
        else:
            return rank + 18, "🔴 Relegated"

    elif "league_2" in stage_type or "league2" in stage_type or "l2" in stage_type:
        if rank <= 6:
            return rank + 12, "🟢 Promoted to League 1"
        else:
            return rank + 12, "🔴 Relegated"

    elif "league_1" in stage_type or "league1" in stage_type or "l1" in stage_type:
        if rank <= 6:
            return rank + 6, "🟢 Promoted to Main"
        else:
            return rank + 6, "🔴 Relegated"

    elif "main" in stage_type:
        if rank <= 6:
            return rank, "🟢 Advanced to Semi-Final"
        else:
            return rank, "🔴 Relegated"

    elif "semi" in stage_type:
        if rank <= 2:
            return rank, "🟢 Advanced to Final"
        else:
            return rank, "🔴 Retained in Main Pool"

    elif "final" in stage_type:
        if rank == 1:
            return rank, "🏆 MCEC Champion"
        elif rank == 2:
            return rank, "🥈 MCEC Runner-Up"
        else:
            return rank, "🥉 Podium"

    elif "survival" in stage_type:
        if rank <= 22:
            return rank + 48, "🟢 Advanced to The Fringe"
        else:
            return rank + 48, "🔴 Fully Kicked Out"

    elif "fringe" in stage_type:
        if rank <= half_cutoff:
            return rank + 48, "🟢 Retained in Circuit"
        else:
            return rank + 48, "🔴 Relegated to Crucible / Out"

    return rank, "⚔️ Active"

def process_stage_pgns(pgn_files, global_ratings, stage_name=""):
    stage_start_ratings = {}
    stats = {}
    head_to_head = {}
    engines_in_stage = set()

    total_stage_games = 0
    total_white_wins = 0
    total_black_wins = 0
    total_draws = 0

    stage_key = stage_name.lower().replace(" ", "_")

    for pgn_path in pgn_files:
        with open(pgn_path, encoding="utf-8", errors="replace") as pgn_file:
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:
                    break

                white = game.headers.get("White", "Unknown").strip()
                black = game.headers.get("Black", "Unknown").strip()
                result = game.headers.get("Result", "*").strip()
                termination = game.headers.get("Termination", "Normal").strip()

                if white == "Unknown" or black == "Unknown" or result not in ["1-0", "0-1", "1/2-1/2", "0.5-0.5"]:
                    continue

                engines_in_stage.add(white)
                engines_in_stage.add(black)
                total_stage_games += 1

                plies = sum(1 for _ in game.mainline_moves())
                game_length = (plies + 1) // 2
                avg_time = parse_move_comments(game)

                c_white = get_canonical_name(white)
                c_black = get_canonical_name(black)

                for eng, c_eng in [(white, c_white), (black, c_black)]:
                    if c_eng not in global_ratings:
                        global_ratings[c_eng] = DEFAULT_RATING
                    if eng not in stage_start_ratings:
                        stage_start_ratings[eng] = global_ratings[c_eng]
                    if eng not in stats:
                        stats[eng] = {
                            "points": 0.0, "played": 0, "wins": 0, "draws": 0, "losses": 0,
                            "white_wins": 0, "black_wins": 0,
                            "white_draws": 0, "black_draws": 0,
                            "white_losses": 0, "black_losses": 0,
                            "white_pts": 0.0, "white_games": 0,
                            "black_pts": 0.0, "black_games": 0,
                            "total_moves": 0, 
                            "shortest_win": 9999, "longest_win": 0,
                            "shortest_draw": 9999, "longest_draw": 0,
                            "shortest_loss": 9999, "longest_loss": 0,
                            "time_losses": 0, "crashes": 0,
                            "move_times": []
                        }

                if white not in head_to_head: head_to_head[white] = {}
                if black not in head_to_head: head_to_head[black] = {}
                if black not in head_to_head[white]: head_to_head[white][black] = {"pts": 0.0, "games": 0, "results": []}
                if white not in head_to_head[black]: head_to_head[black][white] = {"pts": 0.0, "games": 0, "results": []}

                if avg_time:
                    stats[white]["move_times"].append(avg_time)
                    stats[black]["move_times"].append(avg_time)

                stats[white]["total_moves"] += game_length
                stats[black]["total_moves"] += game_length

                if "time" in termination.lower():
                    if result == "0-1": stats[white]["time_losses"] += 1
                    elif result == "1-0": stats[black]["time_losses"] += 1
                elif "abandoned" in termination.lower() or "rules" in termination.lower():
                    if result == "0-1": stats[white]["crashes"] += 1
                    elif result == "1-0": stats[black]["crashes"] += 1

                if result == "1-0":
                    s_w, s_b = 1.0, 0.0
                    stats[white]["wins"] += 1
                    stats[white]["white_wins"] += 1
                    stats[black]["losses"] += 1
                    stats[black]["black_losses"] += 1
                    
                    stats[white]["shortest_win"] = min(stats[white]["shortest_win"], game_length)
                    stats[white]["longest_win"] = max(stats[white]["longest_win"], game_length)
                    stats[black]["shortest_loss"] = min(stats[black]["shortest_loss"], game_length)
                    stats[black]["longest_loss"] = max(stats[black]["longest_loss"], game_length)

                    total_white_wins += 1
                    head_to_head[white][black]["results"].append("1")
                    head_to_head[black][white]["results"].append("0")
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    stats[black]["wins"] += 1
                    stats[black]["black_wins"] += 1
                    stats[white]["losses"] += 1
                    stats[white]["white_losses"] += 1
                    
                    stats[black]["shortest_win"] = min(stats[black]["shortest_win"], game_length)
                    stats[black]["longest_win"] = max(stats[black]["longest_win"], game_length)
                    stats[white]["shortest_loss"] = min(stats[white]["shortest_loss"], game_length)
                    stats[white]["longest_loss"] = max(stats[white]["longest_loss"], game_length)

                    total_black_wins += 1
                    head_to_head[white][black]["results"].append("0")
                    head_to_head[black][white]["results"].append("1")
                else:
                    s_w, s_b = 0.5, 0.5
                    stats[white]["draws"] += 1
                    stats[white]["white_draws"] += 1
                    stats[black]["draws"] += 1
                    stats[black]["black_draws"] += 1

                    stats[white]["shortest_draw"] = min(stats[white]["shortest_draw"], game_length)
                    stats[white]["longest_draw"] = max(stats[white]["longest_draw"], game_length)
                    stats[black]["shortest_draw"] = min(stats[black]["shortest_draw"], game_length)
                    stats[black]["longest_draw"] = max(stats[black]["longest_draw"], game_length)

                    total_draws += 1
                    head_to_head[white][black]["results"].append("½")
                    head_to_head[black][white]["results"].append("½")

                stats[white]["points"] += s_w
                stats[black]["points"] += s_b
                stats[white]["played"] += 1
                stats[black]["played"] += 1

                stats[white]["white_pts"] += s_w
                stats[white]["white_games"] += 1
                stats[black]["black_pts"] += s_b
                stats[black]["black_games"] += 1

                head_to_head[white][black]["pts"] += s_w
                head_to_head[black][white]["pts"] += s_b
                head_to_head[white][black]["games"] += 1
                head_to_head[black][white]["games"] += 1

                r_w, r_b = global_ratings[c_white], global_ratings[c_black]
                exp_w = calculate_expected_score(r_w, r_b)
                exp_b = calculate_expected_score(r_b, r_w)

                global_ratings[c_white] += K_FACTOR * (s_w - exp_w)
                global_ratings[c_black] += K_FACTOR * (s_b - exp_b)

    sorted_engines = sorted(
        engines_in_stage, 
        key=lambda x: (stats[x]["points"], global_ratings[get_canonical_name(x)]), 
        reverse=True
    )

    total_engines_count = len(sorted_engines)

    # 0. STAGE OVERVIEW BANNER
    w_pct = (total_white_wins / total_stage_games * 100) if total_stage_games > 0 else 0
    b_pct = (total_black_wins / total_stage_games * 100) if total_stage_games > 0 else 0
    d_pct = (total_draws / total_stage_games * 100) if total_stage_games > 0 else 0

    md = f"> 📊 **Active Stage Summary:** **{total_stage_games:,}** Total Games Played\n"
    md += f"> ⚪ **White Wins:** {total_white_wins} ({w_pct:.1f}%) | ⬛ **Black Wins:** {total_black_wins} ({b_pct:.1f}%) | 🤝 **Draws:** {total_draws} ({d_pct:.1f}%)\n\n"

    # 1. CLEAN STANDINGS
    md += "#### 🏆 Standings\n\n"
    md += "| Rank | Engine | Score |\n"
    md += "| :---: | :--- | :---: |\n"

    for idx, eng in enumerate(sorted_engines, start=1):
        st = stats[eng]
        p, g = st["points"], st["played"]
        md += f"| {idx} | **{eng}** | **{p:.1f}** / {g} |\n"

    # 2. FULL RATINGS DETAILS
    md += "\n<details><summary><b>📈 View Full Rating Lists / Full Engines (Elo Updates, Win % & Loss %)</b></summary>\n\n"
    md += "| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win % | Loss % | Status |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n"

    for idx, eng in enumerate(sorted_engines):
        abs_rank, status_badge = get_mcec_stage_status(idx, stage_key, total_engines_count)
        st = stats[eng]
        c_eng = get_canonical_name(eng)
        start_r = stage_start_ratings[eng]
        end_r = global_ratings[c_eng]
        diff = end_r - start_r
        diff_str = f"+{diff:.1f}" if diff >= 0 else f"{diff:.1f}"
        p, g = st["points"], st["played"]
        
        win_pct = f"{(st['wins'] / g * 100):.1f}%" if g > 0 else "0.0%"
        loss_pct = f"{(st['losses'] / g * 100):.1f}%" if g > 0 else "0.0%"
        
        md += f"| #{abs_rank} | **{eng}** | {start_r:.0f} | **{end_r:.0f}** | `{diff_str}` | **{p:.1f}** / {g} | {win_pct} | {loss_pct} | {status_badge} |\n"

    md += "\n</details>\n\n"

    # 3. DEVELOPER LOGS
    md += "<details><summary><b>🛠️ View Developer Performance Logs</b></summary>\n\n"
    md += "| Engine | Stage Rank | Win % | Draw % | White Win % | Black Win % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Time Losses | Crashes |\n"
    md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for idx, eng in enumerate(sorted_engines, start=1):
        st = stats[eng]
        win_pct_total = f"{(st['wins'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        draw_pct_total = f"{(st['draws'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        w_pct_e = f"{(st['white_pts'] / st['white_games'] * 100):.1f}%" if st['white_games'] > 0 else "0.0%"
        b_pct_e = f"{(st['black_pts'] / st['black_games'] * 100):.1f}%" if st['black_games'] > 0 else "0.0%"
        avg_len = f"{(st['total_moves'] / st['played']):.1f} moves" if st['played'] > 0 else "N/A"

        win_range = f"{st['shortest_win']} / {st['longest_win']} moves" if st["wins"] > 0 else "N/A"
        draw_range = f"{st['shortest_draw']} / {st['longest_draw']} moves" if st["draws"] > 0 else "N/A"
        loss_range = f"{st['shortest_loss']} / {st['longest_loss']} moves" if st["losses"] > 0 else "N/A"

        md += f"| **{eng}** | #{idx} | {win_pct_total} | {draw_pct_total} | {w_pct_e} | {b_pct_e} | {avg_len} | {win_range} | {draw_range} | {loss_range} | `{st['time_losses']}` | `{st['crashes']}` |\n"

    md += "\n</details>\n\n"

    # 4. CROSSTABLE
    md += "<details><summary><b>🔍 View Stage Crosstable</b></summary>\n\n"
    header_row = "| Engine | " + " | ".join([f"**#{i}**" for i in range(1, total_engines_count + 1)]) + " |\n"
    divider_row = "| :--- | " + " | ".join([":---:"] * total_engines_count) + " |\n"
    md += header_row + divider_row

    for i, eng1 in enumerate(sorted_engines, start=1):
        row = f"| **#{i}. {eng1}** | "
        cells = []
        for j, eng2 in enumerate(sorted_engines, start=1):
            if i == j:
                cells.append("—")
            else:
                rec1 = head_to_head.get(eng1, {}).get(eng2, None)
                rec2 = head_to_head.get(eng2, {}).get(eng1, None)
                
                if rec1 and rec1["games"] > 0:
                    pts1 = rec1["pts"]
                    pts2 = rec2["pts"] if rec2 else 0.0
                    h2h_diff = pts1 - pts2
                    
                    if h2h_diff > 0:
                        diff_str = f"+{h2h_diff:.1f}"
                    elif h2h_diff < 0:
                        diff_str = f"{h2h_diff:.1f}"
                    else:
                        diff_str = "0.0"
                    
                    game_outcomes = " ".join(rec1["results"])
                    cells.append(f"<nobr>{game_outcomes}</nobr><br>({diff_str})")
                else:
                    cells.append("*")
        row += " | ".join(cells) + " |\n"
        md += row

    md += "\n</details>\n"
    return md

def main():
    if not os.path.exists(MAIN_SEASON_DIR):
        print(f"Directory {MAIN_SEASON_DIR} does not exist yet.")
        return

    subdirs = sorted([d for d in glob.glob(os.path.join(MAIN_SEASON_DIR, "*")) if os.path.isdir(d)])
    
    if not subdirs:
        print("No stage directories found in " + MAIN_SEASON_DIR)
        return

    global_ratings = {}
    rendered_stages = []
    stage_titles = []

    for stage_path in subdirs:
        raw_folder = os.path.basename(stage_path)
        stage_title = " ".join(raw_folder.split("_")[1:]).title() if "_" in raw_folder else raw_folder.title()
        stage_pgns = sorted(glob.glob(os.path.join(stage_path, "*.pgn")))
        
        if stage_pgns:
            stage_md = process_stage_pgns(stage_pgns, global_ratings, stage_name=raw_folder)
            rendered_stages.append(stage_md)
            stage_titles.append(stage_title)

    if not rendered_stages:
        print("No PGN files found to process.")
        return

    latest_stage_title = stage_titles[-1]
    latest_stage_md = rendered_stages[-1]

    # OVERWRITTEN README EXPLANATION FOR MCEC SEASON 3 STRUCTURE
    full_md_output = "### 🏰 MCEC Season 3 Structure & Tournament Flow\n\n"
    full_md_output += "MCEC Season 3 is strictly capped at **72 engines** and operates on a core **half-promote / half-relegate** dynamic, divided into **3 core parts and 2 boundary zones**:\n\n"
    
    full_md_output += "#### 📌 Core Structure Parts\n"
    full_md_output += "* **1–36 | The Foundation:** The main tier featuring strict 6-to-6 promotion and relegation rules across Leagues 4 through Main, Semifinals, and Finals.\n"
    full_md_output += "* **37–48 | The Gateway:** The entry point where Gatekeepers and newcomers clash. The top half promotes, and the bottom half relegates.\n"
    full_md_output += "* **49–72 | The Fringe:** Lower-tier survival circuit where the top 22 retain their spots and others are fully kicked out.\n\n"
    
    full_md_output += "#### 🔄 Boundary Zones & Flows\n"
    full_md_output += "* **Entry League:** The bridge between Gateway and Foundation. Gateway top-half survivors challenge the bottom tier of the Foundation.\n"
    full_md_output += "* **The Survival:** The bridge between Gateway and Fringe. Fallen Gateway engines and gatekeeper spillover defend their ranks against the Fringe circuit.\n\n"
    
    full_md_output += "---\n\n"

    full_md_output += f"## 🏆 Active Stage: {latest_stage_title}\n\n"
    full_md_output += latest_stage_md + "\n\n---\n\n"

    if len(stage_titles) > 1:
        full_md_output += "### 📦 Archived Stages & Pre-releases\n\n"
        full_md_output += "| Stage Name | Status | Archive Link |\n"
        full_md_output += "| :--- | :---: | :--- |\n"
        for title in stage_titles[:-1]:
            slug = title.lower().replace(" ", "-")
            full_md_output += f"| **{title}** | Completed | 🔗 [View Release / Archive](../../releases/tag/v3.0-{slug}) |\n"

    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = "<!-- STATS_START -->"
        end_marker = "<!-- STATS_END -->"

        if start_marker in content and end_marker in content:
            before = content.split(start_marker)[0]
            after = content.split(end_marker)[1]
            new_content = f"{before}{start_marker}\n{full_md_output}\n{end_marker}{after}"
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully updated README.md with MCEC Season 3 Structure & dynamic stage rules!")

if __name__ == "__main__":
    main()