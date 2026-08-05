import os
import glob
import re
import chess.pgn

MAIN_SEASON_DIR = "seasons/season_3/main"
DEFAULT_RATING = 3000.0
TOTAL_STAGE_GAMES = 1260
K_FACTOR = 32.0

Dynamic Ladder Rules
GATEWAY_TOP_RANK = 37
GATEWAY_BOTTOM_RANK = 48
GATEWAY_CAPACITY = 12 # Standard 12 slots (37 to 48)

def calculate_expected_score(r1, r2):
return 1.0 / (1.0 + 10.0 ** ((r2 - r1) / 400.0))

def parse_move_comments(game):
"""Extract move time from PGN comments if available."""
clk_times = []
prev_clk = None

for node in game.mainline():
comment = node.comment
if not comment:
continue

clk_match = re.search(r'[%clk\s+(\d+):(\d+):(\d+(?:.\d+)?)]', comment)
if clk_match:
h, m, s = float(clk_match.group(1)), float(clk_match.group(2)), float(clk_match.group(3))
total_sec = h * 3600 + m * 60 + s
if prev_clk is not None:
used_sec = max(0.0, prev_clk - total_sec)
clk_times.append(used_sec)
prev_clk = total_sec

avg_time = round(sum(clk_times) / len(clk_times), 2) if clk_times else None
return avg_time

def get_dynamic_rank_and_status(idx, total_engines):
"""Calculates global ladder rank and status for the Full Rank List."""
newcomers_count = max(0, total_engines - GATEWAY_CAPACITY)

if idx < newcomers_count:
abs_rank = (GATEWAY_TOP_RANK - newcomers_count) + idx
status = f"🟡 Borrowed Tier (#{abs_rank})"
elif idx < GATEWAY_CAPACITY:
abs_rank = GATEWAY_TOP_RANK + (idx - newcomers_count)
status = f"🟢 Gateway Safe (#{abs_rank})"
else:
abs_rank = GATEWAY_BOTTOM_RANK + (idx - GATEWAY_CAPACITY + 1)
status = f"🔴 Relegated / Cucked (#{abs_rank})"

return abs_rank, status

def process_stage_pgns(pgn_files, global_ratings):
stage_start_ratings = {}
stats = {}
head_to_head = {}
engines_in_stage = set()

total_stage_games = 0
total_white_wins = 0
total_black_wins = 0
total_draws = 0

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

for eng in (white, black):
if eng not in global_ratings:
global_ratings[eng] = DEFAULT_RATING
if eng not in stage_start_ratings:
stage_start_ratings[eng] = global_ratings[eng]
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

r_w, r_b = global_ratings[white], global_ratings[black]
exp_w = calculate_expected_score(r_w, r_b)
exp_b = calculate_expected_score(r_b, r_w)

global_ratings[white] += K_FACTOR * (s_w - exp_w)
global_ratings[black] += K_FACTOR * (s_b - exp_b)

sorted_engines = sorted(
engines_in_stage,
key=lambda x: (stats[x]["points"], global_ratings[x]),
reverse=True
)

total_engines_count = len(sorted_engines)

# 0. STAGE OVERVIEW BANNER
w_pct = (total_white_wins / total_stage_games * 100) if total_stage_games > 0 else 0
b_pct = (total_black_wins / total_stage_games * 100) if total_stage_games > 0 else 0
d_pct = (total_draws / total_stage_games * 100) if total_stage_games > 0 else 0

md = f"> 📊 Stage Summary:{total_stage_games:,}/{TOTAL_STAGE_GAMES:,} Total Games Played\n"
md += f"> ⚪ White Wins: {total_white_wins} ({w_pct:.1f}%) | ⬛ Black Wins: {total_black_wins} ({b_pct:.1f}%) | 🤝 Draws: {total_draws} ({d_pct:.1f}%)\n\n"

# 1. CLEAN, INDEPENDENT STAGE STANDINGS (Pure Stage View 1 to N)
md += "#### 🏆 Standings\n\n"
md += "| Rank | Engine | Score |\n"
md += "| :---: | :--- | :---: |\n"

for idx, eng in enumerate(sorted_engines, start=1):
st = stats[eng]
p, g = st["points"], st["played"]
md += f"| {idx} | {eng} | {p:.1f} / {g} |\n"

# 2. COLLAPSIBLE FULL RANK LISTS (Now contains dynamic global rank, new Elo, win score % & draw score %)
md += "\n<details><summary><b>📊 View Full Rank Lists (Global Rank, New Elo, Win Score % & Draw Score %)</b></summary>\n\n"
md += "| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win Score % | Draw Score % | Status |\n"
md += "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n"

for idx, eng in enumerate(sorted_engines):
abs_rank, status_badge = get_dynamic_rank_and_status(idx, total_engines_count)
st = stats[eng]
start_r = stage_start_ratings[eng]
end_r = global_ratings[eng]
diff = end_r - start_r
diff_str = f"+{diff:.1f}" if diff >= 0 else f"{diff:.1f}"
p, g = st["points"], st["played"]

# Calculate Win Score % and Draw Score %
win_score_pct = f"{(st['wins'] / g * 100):.1f}%" if g > 0 else "0.0%"
draw_score_pct = f"{(st['draws'] / g * 100):.1f}%" if g > 0 else "0.0%"

md += f"| #{abs_rank} | {eng} | {start_r:.0f} | {end_r:.0f} | {diff_str} | {p:.1f} / {g} | {win_score_pct} | {draw_score_pct} | {status_badge} |\n"

md += "\n</details>\n\n"

# 3. COLLAPSIBLE DEVELOPER PERFORMANCE LOG
md += "<details><summary><b>🛠️ View Developer Performance Logs (Speed, Percentages & Move Stats)</b></summary>\n\n"
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

md += f"| {eng} | #{idx} | {win_pct_total} | {draw_pct_total} | {w_pct_e} | {b_pct_e} | {avg_len} | {win_range} | {draw_range} | {loss_range} | {st['time_losses']} | {st['crashes']} |\n"

md += "\n</details>\n\n"

# 4. COLLAPSIBLE CUCKED / RELEGATED ENGINES LOG
md += "<details><summary><b>🪦 View Cucked / Relegated Engines (Pushed to Ranks 49-72)</b></summary>\n\n"
md += "| Global Rank | Engine | Score | Win Score % | Forfeits (Crash / Timeout) | Relegation Status |\n"
md += "| :---: | :--- | :---: | :---: | :---: | :--- |\n"

cucked_found = False
for idx, eng in enumerate(sorted_engines):
abs_rank, _ = get_dynamic_rank_and_status(idx, total_engines_count)
if abs_rank > GATEWAY_BOTTOM_RANK:
cucked_found = True
st = stats[eng]
p, g = st["points"], st["played"]
win_score_pct = f"{(st['wins'] / g * 100):.1f}%" if g > 0 else "0.0%"
forfeits = f"{st['crashes']} C / {st['time_losses']} TO"
md += f"| #{abs_rank} | {eng} | {p:.1f} / {g} | {win_score_pct} | {forfeits} | 🚨 Relegated out of Gateway |\n"

if not cucked_found:
md += "| — | No engines relegated past Rank 48 in this stage. | — | — | — | — |\n"

md += "\n</details>\n\n"

# 5. COLLAPSIBLE CROSSTABLE
md += "<details><summary><b>🔍 View Stage Crosstable</b></summary>\n\n"
header_row = "| Engine | " + " | ".join([f"#{i}" for i in range(1, total_engines_count + 1)]) + " |\n"
divider_row = "| :--- | " + " | ".join([":---:"] * total_engines_count) + " |\n"
md += header_row + divider_row

for i, eng1 in enumerate(sorted_engines, start=1):
row = f"| #{i}. {eng1} | "
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
pgn_files = sorted(glob.glob(os.path.join(MAIN_SEASON_DIR, "*.pgn")))

global_ratings = {}
full_md_output = "## 🏆 Stage Results & Live Standings\n\n"
stages_processed = 0

if subdirs:
for stage_path in subdirs:
raw_folder = os.path.basename(stage_path)
stage_title = " ".join(raw_folder.split("")[1:]).title() if "" in raw_folder else raw_folder.title()
stage_pgns = sorted(glob.glob(os.path.join(stage_path, "*.pgn")))

if stage_pgns:
full_md_output += f"### 📌 Stage: {stage_title}\n\n"
full_md_output += process_stage_pgns(stage_pgns, global_ratings) + "\n\n---\n\n"
stages_processed += 1
elif pgn_files:
for pgn_file in pgn_files:
file_name = os.path.splitext(os.path.basename(pgn_file))[0]
stage_title = " ".join(file_name.split("-")).title()
full_md_output += f"### 📌 Stage: {stage_title}\n\n"
full_md_output += process_stage_pgns([pgn_file], global_ratings) + "\n\n---\n\n"
stages_processed += 1

if stages_processed == 0:
print("No PGN files or stage folders found in " + MAIN_SEASON_DIR)
return

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
print("Successfully updated README.md with clean standings and dedicated Full Rank Lists!")

if name == "main":
main()