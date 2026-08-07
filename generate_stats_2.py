import os
import glob
import re
import math
import chess.pgn

MAIN_SEASON_DIR = "seasons/season_3/main"
STAGES_OUTPUT_DIR = "stages"
DEFAULT_RATING = 3000.0
K_FACTOR = 32.0

# 🛠️ ENGINE ALIAS & RENAME MAP (Must match generate_stats.py to stay aligned)
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

def generate_spcc_rating_list():
    if not os.path.exists(MAIN_SEASON_DIR):
        print(f"Directory {MAIN_SEASON_DIR} does not exist yet.")
        return

    pgn_files = sorted(glob.glob(os.path.join(MAIN_SEASON_DIR, "**", "*.pgn"), recursive=True))
    if not pgn_files:
        print("No PGN files found for rating list generation.")
        return

    global_ratings = {}
    engine_data = {}

    # Pass 1: Simulate all games chronologically to compute stable Elo ratings and track opponent stats
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

                c_white = get_canonical_name(white)
                c_black = get_canonical_name(black)

                if c_white not in global_ratings: global_ratings[c_white] = DEFAULT_RATING
                if c_black not in global_ratings: global_ratings[c_black] = DEFAULT_RATING

                for eng in [c_white, c_black]:
                    if eng not in engine_data:
                        engine_data[eng] = {
                            "games": 0, "points": 0.0, "draws": 0, 
                            "opp_rating_sum": 0.0
                        }

                r_w = global_ratings[c_white]
                r_b = global_ratings[c_black]

                # Record pre-game opponent ratings for Av.Op. calculation
                engine_data[c_white]["opp_rating_sum"] += r_b
                engine_data[c_black]["opp_rating_sum"] += r_w

                # Determine scores
                if result == "1-0":
                    s_w, s_b = 1.0, 0.0
                    engine_data[c_white]["draws"] += 0
                    engine_data[c_black]["draws"] += 0
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    engine_data[c_white]["draws"] += 0
                    engine_data[c_black]["draws"] += 0
                else:
                    s_w, s_b = 0.5, 0.5
                    engine_data[c_white]["draws"] += 1
                    engine_data[c_black]["draws"] += 1

                engine_data[c_white]["games"] += 1
                engine_data[c_white]["points"] += s_w
                engine_data[c_black]["games"] += 1
                engine_data[c_black]["points"] += s_b

                # Update Elo ratings
                exp_w = calculate_expected_score(r_w, r_b)
                exp_b = calculate_expected_score(r_b, r_w)
                global_ratings[c_white] += K_FACTOR * (s_w - exp_w)
                global_ratings[c_black] += K_FACTOR * (s_b - exp_b)

    # Compile final SPCC-style stats table rows
    sorted_rating_list = sorted(global_ratings.items(), key=lambda x: x[1], reverse=True)

    md = "### 📊 MCEC Official Computer Rating List (SPCC Style)\n\n"
    md += "Ranking engines based on cumulative Elo performance, score percentages, average opponent strength, and draw rates across all tournament stages.\n\n"
    md += "| Rank | Engine | Rating | + | - | Games | Score % | Av. Op. | Draws % |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for idx, (eng, rating) in enumerate(sorted_rating_list, start=1):
        data = engine_data[eng]
        games = data["games"]
        if games == 0:
            continue
        
        score_pct = (data["points"] / games) * 100.0
        draw_pct = (data["draws"] / games) * 100.0
        av_op = data["opp_rating_sum / games"] if "opp_rating_sum / games" in data else (data["opp_rating_sum"] / games)
        
        # Statistical error margins approximation based on game count variance (standard SPCC/CCRL style heuristic)
        error_margin = max(2, int(round(160.0 / math.sqrt(games)))) if games > 0 else 0

        md += f"| {idx} | **{eng}** | **{rating:.0f}** | {error_margin} | {error_margin} | {games:,} | {score_pct:.1f}% | {av_op:.0f} | {draw_pct:.1f}% |\n"

    os.makedirs(STAGES_OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(STAGES_OUTPUT_DIR, "computer_rating_list.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# MCEC Season 3 - Computer Rating List\n\n{md}")
    print(f"Successfully generated SPCC rating list at: {output_path}")

    # Optionally inject into README under custom markers to keep it modular
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = "<!-- RATING_LIST_START -->"
        end_marker = "<!-- RATING_LIST_END -->"

        if start_marker in content and end_marker in content:
            before = content.split(start_marker)[0]
            after = content.split(end_marker)[1]
            new_content = f"{before}{start_marker}\n{md}\n{end_marker}{after}"
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully updated README.md rating list section!")

if __name__ == "__main__":
    generate_spcc_rating_list()