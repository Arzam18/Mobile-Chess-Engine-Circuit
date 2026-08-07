import os
import glob
import re
import math
import chess.pgn

SEASON_ROOT = "seasons/season_3"
OUTPUT_DIR = "Mobile-Chess-Engine-Circuit/more_results/all version lists"
DEFAULT_RATING = 3000.0
K_FACTOR = 32.0

def calculate_expected_score(r1, r2):
    return 1.0 / (1.0 + 10.0 ** ((r2 - r1) / 400.0))

def parse_engine_identity(name):
    """
    Splits an engine name into a base family name and a version string.
    Example: 'Hobbes 3.0' -> base: 'Hobbes', version: '3.0'
    """
    clean_name = name.strip()
    match = re.match(r'^(.*?)\s+(v?\d+(?:\.\d+)*.*)$', clean_name, re.IGNORECASE)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return clean_name, "1.0"

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

    engine_ratings = {}
    engine_stats = {}
    engine_spcc_data = {}
    family_latest_rating = {}  # Tracks the latest rating per engine family for continuation
    total_master_games = 0

    print(f"Processing {len(pgn_files)} PGN files for version-aware engine tracking...")

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

                for eng in [white, black]:
                    if eng not in engine_ratings:
                        base_name, _ = parse_engine_identity(eng)
                        # Inherit rating from predecessor family version if it exists, else use default
                        starting_rating = family_latest_rating.get(base_name, DEFAULT_RATING)
                        
                        engine_ratings[eng] = starting_rating
                        family_latest_rating[base_name] = starting_rating

                        engine_spcc_data[eng] = {"games": 0, "points": 0.0, "draws": 0, "opp_rating_sum": 0.0}
                        engine_stats[eng] = {
                            "points": 0.0, "played": 0, "wins": 0, "draws": 0, "losses": 0,
                            "white_wins": 0, "black_wins": 0, "white_draws": 0, "black_draws": 0,
                            "white_losses": 0, "black_losses": 0, "total_moves": 0,
                            "shortest_win": 9999, "longest_win": 0,
                            "shortest_draw": 9999, "longest_draw": 0,
                            "shortest_loss": 9999, "longest_loss": 0,
                            "min_depth": 9999, "max_depth": 0, "depths_list": [],
                            "min_time": 99999.0, "max_time": 0.0, "times_list": [],
                            "min_knps": 99999.0, "max_knps": 0.0, "knps_list": [],
                            "time_losses": 0, "crashes": 0
                        }

                r_w = engine_ratings[white]
                r_b = engine_ratings[black]

                engine_spcc_data[white]["opp_rating_sum"] += r_b
                engine_spcc_data[black]["opp_rating_sum"] += r_w

                board = game.board()
                plies = 0
                for node in game.mainline():
                    plies += 1
                    is_white = board.turn == chess.WHITE
                    curr_player = white if is_white else black
                    
                    depth, time_sec, knps = parse_engine_comment(node.comment)
                    if depth is not None:
                        engine_stats[curr_player]["min_depth"] = min(engine_stats[curr_player]["min_depth"], depth)
                        engine_stats[curr_player]["max_depth"] = max(engine_stats[curr_player]["max_depth"], depth)
                        engine_stats[curr_player]["depths_list"].append(depth)
                    if time_sec is not None:
                        engine_stats[curr_player]["min_time"] = min(engine_stats[curr_player]["min_time"], time_sec)
                        engine_stats[curr_player]["max_time"] = max(engine_stats[curr_player]["max_time"], time_sec)
                        engine_stats[curr_player]["times_list"].append(time_sec)
                    if knps is not None:
                        engine_stats[curr_player]["min_knps"] = min(engine_stats[curr_player]["min_knps"], knps)
                        engine_stats[curr_player]["max_knps"] = max(engine_stats[curr_player]["max_knps"], knps)
                        engine_stats[curr_player]["knps_list"].append(knps)
                    board.push(node.move)

                game_length = (plies + 1) // 2
                engine_stats[white]["total_moves"] += game_length
                engine_stats[black]["total_moves"] += game_length

                if "time" in termination.lower():
                    if result == "0-1": engine_stats[white]["time_losses"] += 1
                    elif result == "1-0": engine_stats[black]["time_losses"] += 1
                elif "abandoned" in termination.lower() or "rules" in termination.lower():
                    if result == "0-1": engine_stats[white]["crashes"] += 1
                    elif result == "1-0": engine_stats[black]["crashes"] += 1

                if result == "1-0":
                    s_w, s_b = 1.0, 0.0
                    engine_stats[white]["wins"] += 1; engine_stats[white]["white_wins"] += 1
                    engine_stats[black]["losses"] += 1; engine_stats[black]["black_losses"] += 1
                    engine_stats[white]["shortest_win"] = min(engine_stats[white]["shortest_win"], game_length)
                    engine_stats[white]["longest_win"] = max(engine_stats[white]["longest_win"], game_length)
                    engine_stats[black]["shortest_loss"] = min(engine_stats[black]["shortest_loss"], game_length)
                    engine_stats[black]["longest_loss"] = max(engine_stats[black]["longest_loss"], game_length)
                elif result == "0-1":
                    s_w, s_b = 0.0, 1.0
                    engine_stats[black]["wins"] += 1; engine_stats[black]["black_wins"] += 1
                    engine_stats[white]["losses"] += 1; engine_stats[white]["white_losses"] += 1
                    engine_stats[black]["shortest_win"] = min(engine_stats[black]["shortest_win"], game_length)
                    engine_stats[black]["longest_win"] = max(engine_stats[black]["longest_win"], game_length)
                    engine_stats[white]["shortest_loss"] = min(engine_stats[white]["shortest_loss"], game_length)
                    engine_stats[white]["longest_loss"] = max(engine_stats[white]["longest_loss"], game_length)
                else:
                    s_w, s_b = 0.5, 0.5
                    engine_stats[white]["draws"] += 1; engine_stats[white]["white_draws"] += 1
                    engine_stats[black]["draws"] += 1; engine_stats[black]["black_draws"] += 1
                    engine_stats[white]["shortest_draw"] = min(engine_stats[white]["shortest_draw"], game_length)
                    engine_stats[white]["longest_draw"] = max(engine_stats[white]["longest_draw"], game_length)
                    engine_stats[black]["shortest_draw"] = min(engine_stats[black]["shortest_draw"], game_length)
                    engine_stats[black]["longest_draw"] = max(engine_stats[black]["longest_draw"], game_length)
                    engine_spcc_data[white]["draws"] += 1
                    engine_spcc_data[black]["draws"] += 1

                engine_stats[white]["points"] += s_w
                engine_stats[black]["points"] += s_b
                engine_stats[white]["played"] += 1
                engine_stats[black]["played"] += 1

                engine_spcc_data[white]["games"] += 1
                engine_spcc_data[white]["points"] += s_w
                engine_spcc_data[black]["games"] += 1
                engine_spcc_data[black]["points"] += s_b

                exp_w = calculate_expected_score(r_w, r_b)
                exp_b = calculate_expected_score(r_b, r_w)
                
                engine_ratings[white] += K_FACTOR * (s_w - exp_w)
                engine_ratings[black] += K_FACTOR * (s_b - exp_b)

                # Update family latest ratings for future version continuity
                base_w, _ = parse_engine_identity(white)
                base_b, _ = parse_engine_identity(black)
                family_latest_rating[base_w] = engine_ratings[white]
                family_latest_rating[base_b] = engine_ratings[black]

    sorted_engines = sorted(engine_ratings.keys(), key=lambda x: engine_ratings[x], reverse=True)

    md = "# MCEC Season 3 - All Version Lists\n\n"
    md += f"> 📊 **Version-Aware Overview:** Tracking **{len(sorted_engines):,}** Distinct Engine Versions across **{total_master_games:,}** Total Season Games.\n"
    md += "> *Note: Each specific version (e.g., Hobbes 3.0, Hobbes 3.1) is preserved permanently as its own list entry. Successor versions carry forward predecessor rating baselines as a continuation while maintaining separate game logs.*\n\n"

    # Single Comprehensive Table containing all Ratings + Developer Performance Logs
    md += "### 🏆 Comprehensive Version Standings & Performance Table\n\n"
    md += "| Rank | Engine Version | Rating | +/- | Games | Score % | Wins [W/B] | Losses [W/B] | Draws [W/B] | Av. Op. | Win Moves (S/L) | Draw Moves (S/L) | Loss Moves (S/L) | Depth (S/L / Norm) | Time (S/L / Norm) | kNPS (S/L / Norm) | Crashes |\n"
    md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    for idx, eng in enumerate(sorted_engines, start=1):
        rating = engine_ratings[eng]
        st = engine_stats[eng]
        spcc = engine_spcc_data[eng]
        
        games = st["played"]
        if games == 0:
            continue
            
        score_pct = (st["points"] / games) * 100.0
        av_op = spcc["opp_rating_sum"] / games
        err = max(2, int(round(160.0 / math.sqrt(games))))
        
        wins_str = f"{st['wins']} [{st['white_wins']}/{st['black_wins']}]"
        losses_str = f"{st['losses']} [{st['white_losses']}/{st['black_losses']}]"
        draws_str = f"{st['draws']} [{st['white_draws']}/{st['black_draws']}]"

        win_range = f"{st['shortest_win']} / {st['longest_win']}" if st['shortest_win'] <= 9999 else "N/A"
        draw_range = f"{st['shortest_draw']} / {st['longest_draw']}" if st['shortest_draw'] <= 9999 else "N/A"
        loss_range = f"{st['shortest_loss']} / {st['longest_loss']}" if st['shortest_loss'] <= 9999 else "N/A"
        
        depth_range = f"{st['min_depth']} / {st['max_depth']}" if st['min_depth'] <= 9999 else "N/A"
        normal_depth = f"{(sum(st['depths_list']) / len(st['depths_list'])):.1f}" if st['depths_list'] else "N/A"
        full_depth = f"{depth_range} / {normal_depth}"
        
        time_range = f"{format_time_display(st['min_time'])} / {format_time_display(st['max_time'])}" if st['min_time'] < 99990.0 else "N/A"
        normal_time = format_time_display(sum(st['times_list']) / len(st['times_list'])) if st['times_list'] else "N/A"
        full_time = f"{time_range} / {normal_time}"
        
        knps_range = f"{st['min_knps']:.1f} / {st['max_knps']:.1f}" if st['min_knps'] <= 9999.0 else "N/A"
        normal_knps = f"{(sum(st['knps_list']) / len(st['knps_list'])):.1f}" if st['knps_list'] else "N/A"
        full_knps = f"{knps_range} / {normal_knps}"

        md += f"| {idx} | **{eng}** | **{rating:.0f}** | ±{err} | {games:,} | {score_pct:.1f}% | {wins_str} | {losses_str} | {draws_str} | {av_op:.0f} | {win_range} | {draw_range} | {loss_range} | {full_depth} | {full_time} | {full_knps} | `{st['crashes']}` |\n"

    index_file_path = os.path.join(OUTPUT_DIR, "index.md")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Successfully generated all version lists tracking index at: {index_file_path}")

if __name__ == "__main__":
    main()
