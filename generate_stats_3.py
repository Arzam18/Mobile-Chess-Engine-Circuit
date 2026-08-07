import os
import glob
import re
import math
import chess.pgn

SEASON_ROOT = "seasons/season_3"
OUTPUT_DIR = "Mobile-Chess-Engine-Circuit/more_results/full_engine_results_all_over"
DEFAULT_RATING = 3000.0
K_FACTOR = 32.0

# 🛠️ ENGINE ALIAS & VERSION CONSOLIDATION MAP
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

def main():
    if not os.path.exists(SEASON_ROOT):
        print(f"Directory {SEASON_ROOT} does not exist yet.")
        return

    pgn_files = sorted(glob.glob(os.path.join(SEASON_ROOT, "**", "*.pgn"), recursive=True))
    if not pgn_files:
        print("No PGN files found for tracking.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    global_ratings = {}
    engine_display_names = {}
    global_stats = {}
    global_spcc_data = {}
    total_master_games = 0

    print(f"Processing {len(pgn_files)} PGN files for master engine tracking...")

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

                total_master_games += 1
                c_white = get_canonical_name(white)
                c_black = get_canonical_name(black)

                # Dynamically update to track the latest version/name string encountered
                engine_display_names[c_white] = white
                engine_display_names[c_black] = black

                for c_eng in [c_white, c_black]:
                    if c_eng not in global_ratings:
                        global_ratings[c_eng] = DEFAULT_RATING
                    if c_eng not in global_spcc_data:
                        global_spcc_data[c_eng] = {"games": 0, "points": 0.0, "draws": 0, "opp_rating_sum": 0.0}
                    if c_eng not in global_stats:
                        global_stats[c_eng] = {
                            "points": 0.0, "played": 0, "wins": 0, "draws": 0, "losses": 0,
                            "white_wins": 0, "black_wins": 0, "white_draws": 0, "black_draws": 0,
                            "white_losses": 0, "black_losses": 0, "total_moves": 0,
                            "min_depth": 9999, "max_depth": 0, "depths_list": [],
                            "min_time": 99999.0, "max_time": 0.0, "times_list": [],
                            "min_knps": 99999.0, "max_knps": 0.0, "knps_list": [],
                            "time_losses": 0, "crashes": 0
                        }

                r_w = global_ratings[c_white]
                r_b = global_ratings[c_black]

                global_spcc_data[c_white]["opp_rating_sum"] += r_b
                global_spcc_data[c_black]["opp_rating_sum"] += r_w

                board = game.board()
                plies = 0
                for node in game.mainline():
                    plies += 1
                    is_white = board.turn == chess.WHITE
                    c_player = c_white if is_white else c_black
                    
                    depth, time_sec, knps = parse_engine_comment(node.comment)
                    if depth is not None:
                        global_stats[c_player]["min_depth"] = min(global_stats[c_player]["min_depth"], depth)
                        global_stats[c_player]["max_depth"] = max(global_stats[c_player]["max_depth"], depth)
                        global_stats[c_player]["depths_list"].append(depth)
                    if time_sec is not None:
                        global_stats[c_player]["min_time"] = min(global_stats[c_player]["min_time"], time_sec)
                        global_stats[c_player]["max_time"] = max(global_stats[c_player]["max_time"], time_sec)
                        global_stats[c_player]["times_list"].append(time_sec)
                    if knps is not None:
                        global_stats[c_player]["min_knps"] = min(global_stats[c_player]["min_knps"], knps)
                        global_stats[c_player]["max_knps"] = max(global_stats[c_player]["max_knps"], knps)
                        global_stats[c_player]["knps_list"].append(knps)
                    board.push(node.move)

                game_length = (plies + 1) // 2
                global_stats[c_white]["total_moves"] += game_length
                global_stats[c_black]["total_moves"] += game_length

                if "time" in termination.lower():
                    if result == "0-1": global_stats[c_white]["time_losses"] += 1
                    elif result == "1-0": global_stats[c_black]["time_losses"] += 1
                elif "abandoned" in termination.lower() or "rules" in termination.lower():
                    if result == "0-1": global_stats[c_white]["crashes"] += 1
                    elif result == "1-0": global_stats[c_black]["crashes"] += 1

                if result == "1-0":
                    s_w, s_b = 1.0, 0.0
                    global_stats[c_white]["wins"] += 1; global_stats[c_white]["white_wins"] += 1
                    global_stats[c_black]["losses"] += 1; global_stats[c_black]["black_losses"] += 1
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    global_stats[c_black]["wins"] += 1; global_stats[c_black]["black_wins"] += 1
                    global_stats[c_white]["losses"] += 1; global_stats[c_white]["white_losses"] += 1
                else:
                    s_w, s_b = 0.5, 0.5
                    global_stats[c_white]["draws"] += 1; global_stats[c_white]["white_draws"] += 1
                    global_stats[c_black]["draws"] += 1; global_stats[c_black]["black_draws"] += 1
                    global_spcc_data[c_white]["draws"] += 1
                    global_spcc_data[c_black]["draws"] += 1

                global_stats[c_white]["points"] += s_w
                global_stats[c_black]["points"] += s_b
                global_stats[c_white]["played"] += 1
                global_stats[c_black]["played"] += 1

                global_spcc_data[c_white]["games"] += 1
                global_spcc_data[c_white]["points"] += s_w
                global_spcc_data[c_black]["games"] += 1
                global_spcc_data[c_black]["points"] += s_b

                exp_w = calculate_expected_score(r_w, r_b)
                exp_b = calculate_expected_score(r_b, r_w)
                global_ratings[c_white] += K_FACTOR * (s_w - exp_w)
                global_ratings[c_black] += K_FACTOR * (s_b - exp_b)

    sorted_master_engines = sorted(global_ratings.keys(), key=lambda x: global_ratings[x], reverse=True)

    md = "# MCEC Season 3 - Full Engine Results All Over\n\n"
    md += f"> 📊 **Master Overview:** Tracking **{len(sorted_master_engines):,}** Unique Engines across **{total_master_games:,}** Total Season Games.\n"
    md += "> *Note: Aliased engines and version updates (e.g., Hobbes, Hobbes 3.0, Hobbes dev) are consolidated under their canonical identity, showing their latest active version name with cumulative history included.*\n\n"

    md += "### 🏆 Master Comprehensive Engine Tracking Table\n\n"
    md += "| Rank | Engine (Latest Version) | Rating | + | - | Games | Score % | Wins [W/B] | Losses [W/B] | Draws [W/B] | Av. Op. | Win % | Loss % | Avg Depth | Avg Time | Crashes |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for idx, c_eng in enumerate(sorted_master_engines, start=1):
        disp_name = engine_display_names.get(c_eng, c_eng)
        rating = global_ratings[c_eng]
        st = global_stats[c_eng]
        spcc = global_spcc_data[c_eng]
        
        games = st["played"]
        if games == 0:
            continue
            
        score_pct = (st["points"] / games) * 100.0
        win_pct = (st["wins"] / games) * 100.0
        loss_pct = (st["losses"] / games) * 100.0
        av_op = spcc["opp_rating_sum"] / games
        err = max(2, int(round(160.0 / math.sqrt(games))))
        
        wins_str = f"{st['wins']} [{st['white_wins']}/{st['black_wins']}]"
        losses_str = f"{st['losses']} [{st['white_losses']}/{st['black_losses']}]"
        draws_str = f"{st['draws']} [{st['white_draws']}/{st['black_draws']}]"
        
        avg_depth = f"{(sum(st['depths_list']) / len(st['depths_list'])):.1f}" if st['depths_list'] else "N/A"
        avg_time = format_time_display(sum(st['times_list']) / len(st['times_list'])) if st['times_list'] else "N/A"
        
        md += f"| {idx} | **{disp_name}** | **{rating:.0f}** | +{err} | -{err} | {games:,} | {score_pct:.1f}% | {wins_str} | {losses_str} | {draws_str} | {av_op:.0f} | {win_pct:.1f}% | {loss_pct:.1f}% | {avg_depth} | {avg_time} | `{st['crashes']}` |\n"

    index_file_path = os.path.join(OUTPUT_DIR, "index.md")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Successfully generated master tracking index at: {index_file_path}")

if __name__ == "__main__":
    main()