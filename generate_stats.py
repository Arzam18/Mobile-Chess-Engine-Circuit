#!/usr/bin/env python3
import os
import re
import math
import glob
from collections import defaultdict
from pathlib import Path

# ==========================================
# CONFIGURATION & CONSTANTS
# ==========================================
DEFAULT_ELO = 3000.0
K_FACTOR = 32.0
STAGE_DIR = "seasons/season_3/main"  # Change this to "pgn" if your folders are in pgn/
README_FILE = "README.md"

# ==========================================
# STAGE STATUS LOGIC (MCEC SEASON 3)
# ==========================================
def get_mcec_stage_status(stage_name: str, rank: int, total_engines: int) -> str:
    stage = stage_name.lower().replace("-", "_").replace(" ", "_")
    half_cutoff = math.ceil(total_engines / 2.0)

    if "gateway" in stage:
        return "🟢 Advanced to Entry League" if rank <= half_cutoff else "🔴 Relegated to The Survival"
    elif "entry" in stage:
        return "🟢 Promoted to League 4" if rank <= half_cutoff else "🔴 Relegated to The Survival"
    elif "league_4" in stage or "league4" in stage or "l4" in stage:
        return "🟢 Promoted to League 3" if rank <= 6 else "🔴 Relegated to Entry League"
    elif "league_3" in stage or "league3" in stage or "l3" in stage:
        return "🟢 Promoted to League 2" if rank <= 6 else "🔴 Relegated to League 4"
    elif "league_2" in stage or "league2" in stage or "l2" in stage:
        return "🟢 Promoted to League 1" if rank <= 6 else "🔴 Relegated to League 3"
    elif "league_1" in stage or "league1" in stage or "l1" in stage:
        return "🟢 Promoted to Main" if rank <= 6 else "🔴 Relegated to League 2"
    elif "main" in stage:
        return "🟢 Advanced to Semi-Final" if rank <= 6 else "🔴 Relegated to League 1"
    elif "semi" in stage:
        return "🟢 Advanced to Final" if rank <= 2 else "🔴 Retained in Main Pool"
    elif "final" in stage:
        if rank == 1: return "🏆 MCEC Champion"
        elif rank == 2: return "🥈 MCEC Runner-Up"
        return "🥉 Podium"
    elif "survival" in stage:
        return "🟢 Advanced to The Fringe" if rank <= half_cutoff else "🔴 Relegated to The Crucible"
    elif "fringe" in stage:
        return "🟢 Retained in Circuit" if rank <= half_cutoff else "🔴 Relegated to The Crucible"
    elif "crucible" in stage:
        return "🟢 Saved (Retained in Circuit)" if rank <= half_cutoff else "❌ Eliminated from Circuit"

    return "⚔️ Active"


# ==========================================
# ELO CALCULATIONS
# ==========================================
def calculate_expected_score(rating_a: float, rating_b: float) -> float:
    return 1.0 / (1.0 + math.pow(10, (rating_b - rating_a) / 400.0))

def update_elo(rating_a: float, rating_b: float, score_a: float) -> tuple[float, float]:
    expected_a = calculate_expected_score(rating_a, rating_b)
    expected_b = 1.0 - expected_a
    score_b = 1.0 - score_a

    new_a = rating_a + K_FACTOR * (score_a - expected_a)
    new_b = rating_b + K_FACTOR * (score_b - expected_b)
    return new_a, new_b


# ==========================================
# PGN PARSER & STATS AGGREGATOR
# ==========================================
def parse_pgn_game(game_text: str):
    headers = dict(re.findall(r'\[(\w+)\s+"([^"]*)"\]', game_text))
    white = headers.get("White", "Unknown").strip()
    black = headers.get("Black", "Unknown").strip()
    result = headers.get("Result", "*").strip()
    termination = headers.get("Termination", "").lower()

    moves = re.findall(r'(\d+)\.\s+', game_text)
    move_count = int(moves[-1]) if moves else 0

    if result == "1-0":
        score_w, score_b = 1.0, 0.0
    elif result == "0-1":
        score_w, score_b = 0.0, 1.0
    elif result in ["1/2-1/2", "0.5-0.5"]:
        score_w, score_b = 0.5, 0.5
    else:
        return None  

    time_loss_w = "time" in termination and score_w == 0.0
    time_loss_b = "time" in termination and score_b == 0.0

    return {
        "white": white,
        "black": black,
        "score_w": score_w,
        "score_b": score_b,
        "moves": move_count,
        "time_loss_w": time_loss_w,
        "time_loss_b": time_loss_b,
    }


def process_stage_directory(stage_path: str, global_elos: dict) -> dict:
    pgn_files = glob.glob(os.path.join(stage_path, "*.pgn"))
    
    wins = defaultdict(int)
    draws = defaultdict(int)
    losses = defaultdict(int)
    points = defaultdict(float)
    games_played = defaultdict(int)
    total_moves = defaultdict(int)
    time_losses = defaultdict(int)
    
    short_loss = {}
    long_loss = {}
    
    start_elos = {engine: global_elos[engine] for engine in global_elos}
    current_elos = dict(global_elos)

    crosstable = defaultdict(lambda: defaultdict(lambda: {"pts": 0.0, "games": 0}))

    total_stage_games = 0
    white_wins = 0
    black_wins = 0
    draw_count = 0

    for file_path in sorted(pgn_files):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        raw_games = re.split(r'\n(?=\[Event )', content)
        for raw_game in raw_games:
            if not raw_game.strip():
                continue

            game = parse_pgn_game(raw_game)
            if not game:
                continue

            w, b = game["white"], game["black"]
            sw, sb = game["score_w"], game["score_b"]
            moves = game["moves"]

            if w not in current_elos:
                start_elos[w] = DEFAULT_ELO
                current_elos[w] = DEFAULT_ELO
            if b not in current_elos:
                start_elos[b] = DEFAULT_ELO
                current_elos[b] = DEFAULT_ELO

            total_stage_games += 1
            games_played[w] += 1
            games_played[b] += 1
            points[w] += sw
            points[b] += sb
            total_moves[w] += moves
            total_moves[b] += moves

            if sw == 1.0:
                white_wins += 1
                wins[w] += 1
                losses[b] += 1
                long_loss[b] = max(long_loss.get(b, 0), moves)
                short_loss[b] = min(short_loss.get(b, float('inf')), moves)
            elif sb == 1.0:
                black_wins += 1
                wins[b] += 1
                losses[w] += 1
                long_loss[w] = max(long_loss.get(w, 0), moves)
                short_loss[w] = min(short_loss.get(w, float('inf')), moves)
            else:
                draw_count += 1
                draws[w] += 1
                draws[b] += 1

            if game["time_loss_w"]:
                time_losses[w] += 1
            if game["time_loss_b"]:
                time_losses[b] += 1

            crosstable[w][b]["pts"] += sw
            crosstable[w][b]["games"] += 1
            crosstable[b][w]["pts"] += sb
            crosstable[b][w]["games"] += 1

            new_ew, new_eb = update_elo(current_elos[w], current_elos[b], sw)
            current_elos[w] = new_ew
            current_elos[b] = new_eb

    for engine, elo in current_elos.items():
        global_elos[engine] = elo

    all_stage_engines = sorted(
        current_elos.keys(),
        key=lambda e: (points[e], current_elos[e]),
        reverse=True
    )

    return {
        "engines": all_stage_engines,
        "start_elos": start_elos,
        "current_elos": current_elos,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "points": points,
        "games_played": games_played,
        "total_moves": total_moves,
        "time_losses": time_losses,
        "short_loss": short_loss,
        "long_loss": long_loss,
        "crosstable": crosstable,
        "total_games": total_stage_games,
        "white_wins": white_wins,
        "black_wins": black_wins,
        "draws_count": draw_count,
    }


# ==========================================
# MARKDOWN BUILDER
# ==========================================
def generate_markdown(stage_name: str, stats: dict, is_complete: bool) -> str:
    engines = stats["engines"]
    total_engines = len(engines)
    
    md = []
    
    md.append(f"### 📊 Stage Overview: {stage_name.replace('_', ' ').title()}")
    md.append(
        f"* **Total Games Played:** {stats['total_games']} | "
        f"**White Wins:** {stats['white_wins']} | "
        f"**Black Wins:** {stats['black_wins']} | "
        f"**Draws:** {stats['draws_count']}\n"
    )

    # 1. Rating & Standings Table
    md.append("### 📈 View Full Rating Lists")
    md.append("| Rank | Engine | Start Elo | Current Elo | Δ Elo | Score | Win % | Status |")
    md.append("| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |")

    for rank, engine in enumerate(engines, 1):
        s_elo = stats["start_elos"][engine]
        c_elo = stats["current_elos"][engine]
        diff = c_elo - s_elo
        diff_str = f"+{diff:.1f}" if diff >= 0 else f"{diff:.1f}"
        
        pts = stats["points"][engine]
        gp = stats["games_played"][engine]
        win_pct = (pts / gp * 100.0) if gp > 0 else 0.0
        
        status = get_mcec_stage_status(stage_name, rank, total_engines) if is_complete else "⚔️ Active"
        
        md.append(
            f"| {rank} | **{engine}** | {s_elo:.1f} | **{c_elo:.1f}** | {diff_str} | "
            f"{pts:.1f}/{gp} | {win_pct:.1f}% | {status} |"
        )

    md.append("\n---\n")

    # 2. Developer Logs Table
    md.append("### 🛠️ Developer Logs")
    md.append("| Engine | Avg Length | Short Loss | Long Loss | Time Losses |")
    md.append("| :--- | :---: | :---: | :---: | :---: |")

    for engine in engines:
        gp = stats["games_played"][engine]
        avg_len = (stats["total_moves"][engine] / gp) if gp > 0 else 0.0
        
        s_loss = stats["short_loss"].get(engine)
        l_loss = stats["long_loss"].get(engine)
        
        s_loss_str = str(s_loss) if s_loss is not None and s_loss != float('inf') else "N/A"
        l_loss_str = str(l_loss) if l_loss is not None and l_loss > 0 else "N/A"
        
        t_losses = stats["time_losses"][engine]

        md.append(f"| **{engine}** | {avg_len:.1f} | {s_loss_str} | {l_loss_str} | {t_losses} |")

    md.append("\n---\n")

    # 3. Crosstable Matrix
    md.append("### ⚔️ Head-to-Head Crosstable")
    header_row = "| # | Engine | " + " | ".join(f"{i+1}" for i in range(total_engines)) + " |"
    divider_row = "| :---: | :--- | " + " | ".join(":---:" for _ in range(total_engines)) + " |"
    md.append(header_row)
    md.append(divider_row)

    for i, e1 in enumerate(engines):
        row = [f"{i+1}", f"**{e1}**"]
        for j, e2 in enumerate(engines):
            if i == j:
                row.append("x")
            else:
                cell = stats["crosstable"][e1][e2]
                if cell["games"] > 0:
                    pts = cell["pts"]
                    row.append(f"{pts:g}")
                else:
                    row.append("-")
        md.append("| " + " | ".join(row) + " |")

    return "\n".join(md)


# ==========================================
# MAIN EXECUTION ROUTINE
# ==========================================
def main():
    base_dir = Path(STAGE_DIR)
    print(f"🔍 Looking for stage folders in: '{STAGE_DIR}'...")
    
    if not base_dir.exists():
        print(f"❌ ERROR: Directory '{STAGE_DIR}' not found!")
        return

    stage_dirs = sorted([d for d in base_dir.iterdir() if d.is_dir()])
    if not stage_dirs:
        print(f"❌ ERROR: No stage subdirectories found inside '{STAGE_DIR}/'!")
        return

    global_elos = defaultdict(lambda: DEFAULT_ELO)
    all_markdown = []

    total_stages = len(stage_dirs)
    for idx, stage_dir in enumerate(stage_dir for stage_dir in stage_dirs):
        stage_name = stage_dir.name
        is_latest_stage = (idx == total_stages - 1)
        
        print(f"⚙️ Processing Stage [{idx+1}/{total_stages}]: {stage_name}...")
        
        stats = process_stage_directory(str(stage_dir), global_elos)
        stage_md = generate_markdown(stage_name, stats, is_complete=not is_latest_stage)
        
        all_markdown.append(stage_md)

    final_output = "\n\n".join(all_markdown)

    # Update README.md safely using markers
    if not os.path.exists(README_FILE):
        print(f"❌ ERROR: '{README_FILE}' not found in root directory!")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- STATS_START -->"
    end_marker = "<!-- STATS_END -->"

    if start_marker not in content or end_marker not in content:
        print(f"❌ ERROR: Markers '{start_marker}' and/or '{end_marker}' are missing from your README.md!")
        print("👉 Please add these markers to your README.md where you want the tables to appear.")
        return

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]
    new_content = f"{before}{start_marker}\n\n{final_output}\n\n{end_marker}{after}"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ SUCCESS: Successfully updated statistics inside {README_FILE}!")


if __name__ == "__main__":
    main()

