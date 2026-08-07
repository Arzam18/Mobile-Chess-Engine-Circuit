import os
import glob
import re
import math
import chess.pgn

MAIN_SEASON_DIR = "seasons/season_3/main"
STAGES_OUTPUT_DIR = "stages"
DEFAULT_RATING = 3000.0
K_FACTOR = 32.0

# 🛠️ ENGINE ALIAS & RENAME MAP
ENGINE_ALIASES = {
    "hobess": "Hobbes",
    "hobbes 3.0": "Hobbes",
    "hobbes dev": "Hobbes",
}

def calculate_expected_score(r1, r2):
    return 1.0 / (1.0 + 10.0 ** ((r2 - r1) / 400.0))

def get_canonical_name(name):
    lower_name = name.strip().lower()
    if lower_name in ENGINE_ALIASES:
        return ENGINE_ALIASES[lower_name]
    cleaned = re.sub(r'\s+(?:v?\d+(?:\.\d+)*).*$', '', name, flags=re.IGNORECASE).strip()
    return cleaned if cleaned else name

def format_time_display(sec):
    if sec >= 99990.0:
        return "N/A"
    if sec < 1.0:
        return f"{int(round(sec * 1000))}ms"
    return f"{sec:.1f}s"

def parse_engine_comment(comment):
    """Parses depth, time in seconds, and normalized kNPS from PGN comments like:
       [19] 2.03 1.8s 158.0knps or [130] mate 3 1.7s 1.5Mnps"""
    if not comment:
        return None, None, None
        
    match = re.search(r'\[(\d+)\]\s+(?:mate\s+\d+|[-\d\.]+)\s+([\d\.]+)(s|ms)\s+([\d\.]+)([kKM]?)nps', comment, re.IGNORECASE)
    if not match:
        return None, None, None
        
    depth = int(match.group(1))
    val = float(match.group(2))
    unit = match.group(3).lower()
    time_sec = val / 1000.0 if unit == 'ms' else val
    
    nps_val = float(match.group(4))
    multiplier = match.group(5).upper()
    
    if multiplier == 'M':
        knps = nps_val * 1000.0
    else:
        knps = nps_val

    return depth, time_sec, knps

def get_mcec_stage_status(idx, stage_type, total_engines):
    rank = idx + 1  
    half_cutoff = math.ceil(total_engines / 2.0)

    if "gateway" in stage_type:
        if rank <= half_cutoff: return rank + 36, "🟢 Advanced to Entry League"
        else: return rank + 36, "🔴 Relegated to The Survival"
    elif "entry" in stage_type:
        if rank <= half_cutoff: return rank, "🟢 Promoted to Foundation"
        else: return rank + 36, "🔴 Relegated to Gatekeeper / Fringe"
    elif "league_4" in stage_type or "league4" in stage_type or "l4" in stage_type:
        if rank <= 6: return rank + 24, "🟢 Promoted to League 3"
        else: return rank + 24, "🔴 Relegated"
    elif "league_3" in stage_type or "league3" in stage_type or "l3" in stage_type:
        if rank <= 6: return rank + 18, "🟢 Promoted to League 2"
        else: return rank + 18, "🔴 Relegated"
    elif "league_2" in stage_type or "league2" in stage_type or "l2" in stage_type:
        if rank <= 6: return rank + 12, "🟢 Promoted to League 1"
        else: return rank + 12, "🔴 Relegated"
    elif "league_1" in stage_type or "league1" in stage_type or "l1" in stage_type:
        if rank <= 6: return rank + 6, "🟢 Promoted to Main"
        else: return rank + 6, "🔴 Relegated"
    elif "main" in stage_type:
        if rank <= 6: return rank, "🟢 Advanced to Semi-Final"
        else: return rank, "🔴 Relegated"
    elif "semi" in stage_type:
        if rank <= 2: return rank, "🟢 Advanced to Final"
        else: return rank, "🔴 Retained in Main Pool"
    elif "final" in stage_type:
        if rank == 1: return rank, "🏆 MCEC Champion"
        elif rank == 2: return rank, "🥈 MCEC Runner-Up"
        else: return rank, "🥉 Podium"
    elif "survival" in stage_type:
        if rank <= 22: return rank + 48, "🟢 Advanced to The Fringe"
        else: return rank + 48, "🔴 Fully Kicked Out"
    elif "fringe" in stage_type:
        if rank <= half_cutoff: return rank + 48, "🟢 Retained in Circuit"
        else: return rank + 48, "🔴 Relegated to Crucible / Out"
    return rank, "⚔️ Active"

def process_stage_pgns(pgn_files, global_ratings, global_spcc_data, engine_display_names, stage_name=""):
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

                c_white = get_canonical_name(white)
                c_black = get_canonical_name(black)

                # Capture best version/display name for the rating table
                if c_white not in engine_display_names or len(white) >= len(engine_display_names[c_white]):
                    engine_display_names[c_white] = white
                if c_black not in engine_display_names or len(black) >= len(engine_display_names[c_black]):
                    engine_display_names[c_black] = black

                for c_eng in [c_white, c_black]:
                    if c_eng not in global_ratings:
                        global_ratings[c_eng] = DEFAULT_RATING
                    if c_eng not in global_spcc_data:
                        global_spcc_data[c_eng] = {"games": 0, "points": 0.0, "draws": 0, "opp_rating_sum": 0.0}

                for eng in [white, black]:
                    if eng not in stage_start_ratings:
                        stage_start_ratings[eng] = global_ratings[get_canonical_name(eng)]
                    if eng not in stats:
                        stats[eng] = {
                            "points": 0.0, "played": 0, "wins": 0, "draws": 0, "losses": 0,
                            "white_wins": 0, "black_wins": 0, "white_draws": 0, "black_draws": 0,
                            "white_losses": 0, "black_losses": 0, "white_pts": 0.0, "white_games": 0,
                            "black_pts": 0.0, "black_games": 0, "total_moves": 0, 
                            "shortest_win": 9999, "longest_win": 0, 
                            "shortest_draw": 9999, "longest_draw": 0,
                            "shortest_loss": 9999, "longest_loss": 0,
                            "min_depth": 9999, "max_depth": 0, "depths_list": [],
                            "min_time": 99999.0, "max_time": 0.0, "times_list": [],
                            "min_knps": 99999.0, "max_knps": 0.0, "knps_list": [],
                            "time_losses": 0, "crashes": 0
                        }

                if white not in head_to_head: head_to_head[white] = {}
                if black not in head_to_head: head_to_head[black] = {}
                if black not in head_to_head[white]: head_to_head[white][black] = {"pts": 0.0, "games": 0, "results": []}
                if white not in head_to_head[black]: head_to_head[black][white] = {"pts": 0.0, "games": 0, "results": []}

                r_w = global_ratings[c_white]
                r_b = global_ratings[c_black]

                # Accumulate SPCC opponent ratings pre-update
                global_spcc_data[c_white]["opp_rating_sum"] += r_b
                global_spcc_data[c_black]["opp_rating_sum"] += r_w

                board = game.board()
                plies = 0
                for node in game.mainline():
                    plies += 1
                    is_white = board.turn == chess.WHITE
                    player = white if is_white else black
                    
                    depth, time_sec, knps = parse_engine_comment(node.comment)
                    if depth is not None:
                        stats[player]["min_depth"] = min(stats[player]["min_depth"], depth)
                        stats[player]["max_depth"] = max(stats[player]["max_depth"], depth)
                        stats[player]["depths_list"].append(depth)
                    if time_sec is not None:
                        stats[player]["min_time"] = min(stats[player]["min_time"], time_sec)
                        stats[player]["max_time"] = max(stats[player]["max_time"], time_sec)
                        stats[player]["times_list"].append(time_sec)
                    if knps is not None:
                        stats[player]["min_knps"] = min(stats[player]["min_knps"], knps)
                        stats[player]["max_knps"] = max(stats[player]["max_knps"], knps)
                        stats[player]["knps_list"].append(knps)

                    board.push(node.move)

                game_length = (plies + 1) // 2
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
                    stats[white]["wins"] += 1; stats[white]["white_wins"] += 1
                    stats[black]["losses"] += 1; stats[black]["black_losses"] += 1
                    stats[white]["shortest_win"] = min(stats[white]["shortest_win"], game_length)
                    stats[white]["longest_win"] = max(stats[white]["longest_win"], game_length)
                    stats[black]["shortest_loss"] = min(stats[black]["shortest_loss"], game_length)
                    stats[black]["longest_loss"] = max(stats[black]["longest_loss"], game_length)
                    total_white_wins += 1
                    head_to_head[white][black]["results"].append("1")
                    head_to_head[black][white]["results"].append("0")
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    stats[black]["wins"] += 1; stats[black]["black_wins"] += 1
                    stats[white]["losses"] += 1; stats[white]["white_losses"] += 1
                    stats[black]["shortest_win"] = min(stats[black]["shortest_win"], game_length)
                    stats[black]["longest_win"] = max(stats[black]["longest_win"], game_length)
                    stats[white]["shortest_loss"] = min(stats[white]["shortest_loss"], game_length)
                    stats[white]["longest_loss"] = max(stats[white]["longest_loss"], game_length)
                    total_black_wins += 1
                    head_to_head[white][black]["results"].append("0")
                    head_to_head[black][white]["results"].append("1")
                else:
                    s_w, s_b = 0.5, 0.5
                    stats[white]["draws"] += 1; stats[white]["white_draws"] += 1
                    stats[black]["draws"] += 1; stats[black]["black_draws"] += 1
                    stats[white]["shortest_draw"] = min(stats[white]["shortest_draw"], game_length)
                    stats[white]["longest_draw"] = max(stats[white]["longest_draw"], game_length)
                    stats[black]["shortest_draw"] = min(stats[black]["shortest_draw"], game_length)
                    stats[black]["longest_draw"] = max(stats[black]["longest_draw"], game_length)
                    total_draws += 1
                    head_to_head[white][black]["results"].append("½")
                    head_to_head[black][white]["results"].append("½")
                    global_spcc_data[c_white]["draws"] += 1
                    global_spcc_data[c_black]["draws"] += 1

                stats[white]["points"] += s_w
                stats[black]["points"] += s_b
                stats[white]["played"] += 1
                stats[black]["played"] += 1
                stats[white]["white_pts"] += s_w
                stats[white]["white_games"] += 1
                stats[black]["black_pts"] += s_b
                stats[black]["black_games"] += 1

                global_spcc_data[c_white]["games"] += 1
                global_spcc_data[c_white]["points"] += s_w
                global_spcc_data[c_black]["games"] += 1
                global_spcc_data[c_black]["points"] += s_b

                head_to_head[white][black]["pts"] += s_w
                head_to_head[black][white]["pts"] += s_b
                head_to_head[white][black]["games"] += 1
                head_to_head[black][white]["games"] += 1

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

    w_pct = (total_white_wins / total_stage_games * 100) if total_stage_games > 0 else 0
    b_pct = (total_black_wins / total_stage_games * 100) if total_stage_games > 0 else 0
    d_pct = (total_draws / total_stage_games * 100) if total_stage_games > 0 else 0

    md = f"> 📊 **Active Stage Summary:** **{total_stage_games:,}** Total Games Played\n"
    md += f"> ⚪ **White Wins:** {total_white_wins} ({w_pct:.1f}%) | ⬛ **Black Wins:** {total_black_wins} ({b_pct:.1f}%) | 🤝 **Draws:** {total_draws} ({d_pct:.1f}%)\n\n"

    md += "#### 🏆 Standings\n\n"
    md += "| Rank | Engine | Score |\n"
    md += "| :---: | :--- | :---: |\n"
    for idx, eng in enumerate(sorted_engines, start=1):
        st = stats[eng]
        md += f"| {idx} | **{eng}** | **{st['points']:.1f}** / {st['played']} |\n"

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
        win_pct = f"{(st['wins'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        loss_pct = f"{(st['losses'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        md += f"| #{abs_rank} | **{eng}** | {start_r:.0f} | **{end_r:.0f}** | `{diff_str}` | **{st['points']:.1f}** / {st['played']} | {win_pct} | {loss_pct} | {status_badge} |\n"
    md += "\n</details>\n\n"

    # DEVELOPER LOGS WITH SHORT/LONG AND NORMAL METRICS
    md += "<details><summary><b>🛠️ View Developer Performance Logs</b></summary>\n\n"
    md += "| Engine | Stage Rank | Win % | Draw % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Short / Long Depth | Normal Depth | Short / Long Time | Normal Time | Short / Long kNPS | Normal kNPS | Time Losses | Crashes |\n"
    md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    for idx, eng in enumerate(sorted_engines, start=1):
        st = stats[eng]
        win_pct_total = f"{(st['wins'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        draw_pct_total = f"{(st['draws'] / st['played'] * 100):.1f}%" if st['played'] > 0 else "0.0%"
        avg_len = f"{(st['total_moves'] / st['played']):.1f} moves" if st['played'] > 0 else "N/A"
        
        win_range = f"{st['shortest_win']} / {st['longest_win']} moves" if st['shortest_win'] <= 9999 else "N/A"
        draw_range = f"{st['shortest_draw']} / {st['longest_draw']} moves" if st['shortest_draw'] <= 9999 else "N/A"
        loss_range = f"{st['shortest_loss']} / {st['longest_loss']} moves" if st['shortest_loss'] <= 9999 else "N/A"

        depth_range = f"{st['min_depth']} / {st['max_depth']}" if st['min_depth'] <= 9999 else "N/A"
        normal_depth = f"{(sum(st['depths_list']) / len(st['depths_list'])):.1f}" if st['depths_list'] else "N/A"

        time_range = f"{format_time_display(st['min_time'])} / {format_time_display(st['max_time'])}" if st['min_time'] < 99990.0 else "N/A"
        normal_time = format_time_display(sum(st['times_list']) / len(st['times_list'])) if st['times_list'] else "N/A"

        knps_range = f"{st['min_knps']:.1f} / {st['max_knps']:.1f}" if st['min_knps'] <= 9999.0 else "N/A"
        normal_knps = f"{(sum(st['knps_list']) / len(st['knps_list'])):.1f}" if st['knps_list'] else "N/A"

        md += f"| **{eng}** | #{idx} | {win_pct_total} | {draw_pct_total} | {avg_len} | {win_range} | {draw_range} | {loss_range} | {depth_range} | {normal_depth} | {time_range} | {normal_time} | {knps_range} | {normal_knps} | `{st['time_losses']}` | `{st['crashes']}` |\n"
    md += "\n</details>\n\n"

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
                    h2h_diff = rec1["pts"] - (rec2["pts"] if rec2 else 0.0)
                    diff_str = f"+{h2h_diff:.1f}" if h2h_diff > 0 else (f"{h2h_diff:.1f}" if h2h_diff < 0 else "0.0")
                    cells.append(f"<nobr>{' '.join(rec1['results'])}</nobr><br>({diff_str})")
                else:
                    cells.append("*")
        row += " | ".join(cells) + " |\n"
        md += row
    md += "\n</details>\n"
    return md

def generate_spcc_rating_table(global_ratings, global_spcc_data, engine_display_names):
    sorted_spcc = sorted(global_ratings.items(), key=lambda x: x[1], reverse=True)
    
    md = "<details><summary><b>📊 View Official Computer Rating List (SPCC Style)</b></summary>\n\n"
    md += "Ranking engines based on cumulative Elo performance, score percentages, average opponent strength, and draw rates across all stages.\n\n"
    md += "| Rank | Engine | Rating | + | - | Games | Score % | Av. Op. | Draws % |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for idx, (c_eng, rating) in enumerate(sorted_spcc, start=1):
        data = global_spcc_data.get(c_eng, {"games": 0, "points": 0.0, "draws": 0, "opp_rating_sum": 0.0})
        games = data["games"]
        if games == 0:
            continue
        
        display_name = engine_display_names.get(c_eng, c_eng)
        score_pct = (data["points"] / games) * 100.0
        draw_pct = (data["draws"] / games) * 100.0
        av_op = data["opp_rating_sum"] / games
        error_margin = max(2, int(round(160.0 / math.sqrt(games)))) if games > 0 else 0

        md += f"| {idx} | **{display_name}** | **{rating:.0f}** | {error_margin} | {error_margin} | {games:,} | {score_pct:.1f}% | {av_op:.0f} | {draw_pct:.1f}% |\n"

    md += "\n</details>\n\n"
    return md

def main():
    if not os.path.exists(MAIN_SEASON_DIR):
        print(f"Directory {MAIN_SEASON_DIR} does not exist yet.")
        return

    subdirs = sorted([d for d in glob.glob(os.path.join(MAIN_SEASON_DIR, "*")) if os.path.isdir(d)])
    if not subdirs:
        print("No stage directories found.")
        return

    os.makedirs(STAGES_OUTPUT_DIR, exist_ok=True)

    global_ratings = {}
    global_spcc_data = {}
    engine_display_names = {}
    stage_records = []

    for stage_path in subdirs:
        raw_folder = os.path.basename(stage_path)
        stage_title = " ".join(raw_folder.split("_")[1:]).title() if "_" in raw_folder else raw_folder.title()
        stage_pgns = sorted(glob.glob(os.path.join(stage_path, "*.pgn")))
        
        if stage_pgns:
            stage_md = process_stage_pgns(stage_pgns, global_ratings, global_spcc_data, engine_display_names, stage_name=raw_folder)
            slug = stage_title.lower().replace(" ", "-")
            
            stage_file_path = os.path.join(STAGES_OUTPUT_DIR, f"{slug}.md")
            with open(stage_file_path, "w", encoding="utf-8") as sf:
                sf.write(f"# MCEC Season 3 - {stage_title}\n\n{stage_md}")
            
            stage_records.append((stage_title, slug, stage_md))

    if not stage_records:
        print("No PGN files processed.")
        return

    latest_title, latest_slug, latest_md = stage_records[-1]

    full_md_output = "### 🏰 MCEC Season 3 Structure & Tournament Flow\n\n"
    full_md_output += "MCEC Season 3 is strictly capped at **72 engines** and operates on a core **half-promote / half-relegate** dynamic, divided into **3 core parts and 2 boundary zones**:\n\n"
    full_md_output += "#### 📌 Core Structure Parts\n"
    full_md_output += "* **1–36 | The Foundation:** Multi-tier elite bracket featuring strict 6-to-6 promotion and relegation rules.\n"
    full_md_output += "* **37–48 | The Gateway:** Entry gate where Gatekeepers and newcomers clash (top half promotes, bottom half relegates).\n"
    full_md_output += "* **49–72 | The Fringe:** Lower-tier survival circuit where the top 22 retain their spots and others are fully kicked out.\n\n"
    full_md_output += "#### 🔄 Boundary Zones & Flows\n"
    full_md_output += "* **Entry League:** Bridge between Gateway and Foundation.\n"
    full_md_output += "* **The Survival:** Bridge between Gateway and Fringe.\n\n"
    full_md_output += "---\n\n"

    # Append SPCC Computer Rating List with versions included
    full_md_output += generate_spcc_rating_table(global_ratings, global_spcc_data, engine_display_names)

    full_md_output += f"## 🏆 Active Stage: {latest_title}\n\n"
    full_md_output += latest_md + "\n\n---\n\n"

    if len(stage_records) > 1:
        full_md_output += "### 📦 Archived Stages & Pre-releases\n\n"
        full_md_output += "| Stage Name | Status | Full Details File |\n"
        full_md_output += "| :--- | :---: | :--- |\n"
        for title, slug, _ in stage_records[:-1]:
            full_md_output += f"| **{title}** | Completed | 🔗 [View Stage Data](stages/{slug}.md) |\n"

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
            print("Successfully updated main script with engine versions shown in the SPCC rating list!")

if __name__ == "__main__":
    main()