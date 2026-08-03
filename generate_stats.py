import os
import glob
import chess.pgn

DEFAULT_RATING = 3200.0
K_FACTOR = 32.0

def calculate_expected_score(r1, r2):
    return 1.0 / (1.0 + 10.0 ** ((r2 - r1) / 400.0))

def process_stage(pgn_files, global_ratings):
    stage_start_ratings = {}
    stats = {}
    head_to_head = {}
    engines_in_stage = set()

    for pgn_path in pgn_files:
        with open(pgn_path, encoding="utf-8", errors="replace") as pgn_file:
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:
                    break

                white = game.headers.get("White", "Unknown").strip()
                black = game.headers.get("Black", "Unknown").strip()
                result = game.headers.get("Result", "*").strip()

                if white == "Unknown" or black == "Unknown" or result not in ["1-0", "0-1", "1/2-1/2", "0.5-0.5"]:
                    continue

                engines_in_stage.add(white)
                engines_in_stage.add(black)

                for eng in (white, black):
                    if eng not in global_ratings:
                        global_ratings[eng] = DEFAULT_RATING
                    if eng not in stage_start_ratings:
                        stage_start_ratings[eng] = global_ratings[eng]
                    if eng not in stats:
                        stats[eng] = {"points": 0.0, "played": 0, "wins": 0, "draws": 0, "losses": 0}

                if white not in head_to_head: head_to_head[white] = {}
                if black not in head_to_head: head_to_head[black] = {}
                if black not in head_to_head[white]: head_to_head[white][black] = {"pts": 0.0, "games": 0}
                if white not in head_to_head[black]: head_to_head[black][white] = {"pts": 0.0, "games": 0}

                if result == "1-0":
                    s_w, s_b = 1.0, 0.0
                    stats[white]["wins"] += 1
                    stats[black]["losses"] += 1
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    stats[black]["wins"] += 1
                    stats[white]["losses"] += 1
                else:
                    s_w, s_b = 0.5, 0.5
                    stats[white]["draws"] += 1
                    stats[black]["draws"] += 1

                stats[white]["points"] += s_w
                stats[black]["points"] += s_b
                stats[white]["played"] += 1
                stats[black]["played"] += 1

                head_to_head[white][black]["pts"] += s_w
                head_to_head[black][white]["pts"] += s_b
                head_to_head[white][black]["games"] += 1
                head_to_head[black][white]["games"] += 1

                r_w = global_ratings[white]
                r_b = global_ratings[black]

                exp_w = calculate_expected_score(r_w, r_b)
                exp_b = calculate_expected_score(r_b, r_w)

                global_ratings[white] += K_FACTOR * (s_w - exp_w)
                global_ratings[black] += K_FACTOR * (s_b - exp_b)

    sorted_engines = sorted(
        engines_in_stage, 
        key=lambda x: (stats[x]["points"], global_ratings[x]), 
        reverse=True
    )

    md = "| Rank | Engine | Start Elo | End Elo | Change (Δ) | Points | Played | Win % |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for rank, eng in enumerate(sorted_engines, 1):
        start_r = stage_start_ratings[eng]
        end_r = global_ratings[eng]
        diff = end_r - start_r
        diff_str = f"+{diff:.1f}" if diff >= 0 else f"{diff:.1f}"

        p, g = stats[eng]["points"], stats[eng]["played"]
        win_pct = f"{(p / g * 100):.1f}%" if g > 0 else "0.0%"

        md += f"| {rank} | **{eng}** | {start_r:.0f} | **{end_r:.0f}** | `{diff_str}` | **{p:.1f}** | {g} | {win_pct} |\n"

    md += "\n<details><summary><b>🔍 View Stage Crosstable</b></summary>\n\n"
    header_row = "| Engine | " + " | ".join([f"**{i+1}**" for i in range(len(sorted_engines))]) + " |\n"
    divider_row = "| :--- | " + " | ".join([":---:"] * len(sorted_engines)) + " |\n"
    md += header_row + divider_row

    for i, eng1 in enumerate(sorted_engines):
        row = f"| **{i+1}. {eng1}** | "
        cells = []
        for j, eng2 in enumerate(sorted_engines):
            if i == j:
                cells.append("—")
            else:
                record = head_to_head.get(eng1, {}).get(eng2, None)
                if record and record["games"] > 0:
                    cells.append(f"{record['pts']:.1f}/{record['games']}")
                else:
                    cells.append("*")
        row += " | ".join(cells) + " |\n"
        md += row

    md += "\n</details>\n"
    return md

def main():
    stage_dirs = sorted([d for d in glob.glob("pgn/*") if os.path.isdir(d)])
    
    if not stage_dirs:
        print("No stage directories found in pgn/")
        return

    global_ratings = {}
    full_md_output = "## 🏆 Stage Results & Live Standings\n\n"

    for stage_path in stage_dirs:
        raw_folder = os.path.basename(stage_path)
        stage_title = " ".join(raw_folder.split("_")[1:]).title()
        pgn_files = sorted(glob.glob(os.path.join(stage_path, "*.pgn")))
        
        if pgn_files:
            full_md_output += f"### 📌 Stage: {stage_title}\n\n"
            full_md_output += process_stage(pgn_files, global_ratings) + "\n\n---\n\n"

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
            print("Successfully updated README.md with live tournament stats!")

if __name__ == "__main__":
    main()
