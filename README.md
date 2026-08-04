# 📱 Mobile Chess Engine Circuit (MCEC)

Welcome to the official repository for the **Mobile Chess Engine Circuit (MCEC)**!

The MCEC is a dedicated hobbyist Android tournament circuit where world-class chess engines compete on practical, daily-use mobile hardware. The primary goal is to benchmark software efficiency, stability, and playing strength under strict hardware resource limits.

---

## 🎯 Season 3: Tournament Structure & Tiers

Following an initial 72-engine baseline benchmark, participant engines are divided into three core tiers:

* **Top 1–36:** The Main Engines
* **Top 37–48:** The Gateway (Gatekeepers)
* **Top 49–72:** The Fringe

---

## ⚔️ How "The Gateway" Works

**The Gateway** serves as the entry point and testing ground for new engines joining the circuit:

* **The Gatekeepers (Ranked 37–48):** 12 engines assigned to defend their positions against newcomers.
* **The Newcomers:** New challengers entering the circuit must fight in The Gateway.
* **The Split:** Upon conclusion of The Gateway, the participant pool is split in half based on performance:
  * **Top Half:** Advances to the **MCEC S3 Entry League** to face the bottom half of the Main Engines (Ranked 19–36).
  * **Bottom Half:** Drops down to face top engines in lower tiers.

---

## 🪜 League Progression Ladder

Surviving engines advance up the competitive ladder toward the championship:

1. **The Gateway:** Entry testing ground (Newcomers vs Gatekeepers)
2. **Entry League:** Gateway Top Half vs Main Engines (Ranked 19–36)
3. **League 4:** 12 Engines | 396 Games | Top 25–36
4. **League 3:** 12 Engines | 396 Games | Top 19–30
5. **League 2:** 12 Engines | 396 Games | Top 13–24
6. **League 1:** 12 Engines | 396 Games | Top 6–17
7. **Main League:** 12 Engines | 660 Games | Top 1–12
8. **Semi-Final:** 6 Engines | 750 Games | Top 1–6
9. **Final:** 2 Engines | 300 Games | Top 1 vs Top 2

### 🔄 Post-Season Relegation & Capped Pool (Executed after Finals)
Because MCEC maintains a strict cap of 72 engines:
* **The Fringe (Ranked 49–66):** Lower-tier survival league.
* **The Crucible (Ranked 67–78):** Kicked-out engines (from rank 72 downward) fight the bottom 6 engines to earn or defend their spot in the circuit.

---

<!-- STATS_START -->
## 🏆 Stage Results & Live Standings

### 📌 Stage: Gateway

> 📊 **Stage Summary:** **408/1,260** Total Games Played
> ⚪ **White Wins:** 182 (44.6%) | ⬛ **Black Wins:** 65 (15.9%) | 🤝 **Draws:** 161 (39.5%)

#### 📊 Leaderboard

| Rank | Engine | Start Elo | End Elo | Change (Δ) | Points / Played | W | D | L | Win % |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Hobbes 3.0** | 3000 | **3161** | `+161.0` | **22.0** / 26 | 18 (13-5) | 8 (0-8) | 0 (0-0) | 84.6% |
| 2 | **Halogen 16.7.12** | 3000 | **3132** | `+132.2` | **20.0** / 26 | 15 (11-4) | 10 (2-8) | 1 (0-1) | 76.9% |
| 3 | **Icarus 1.1.1 dev** | 3000 | **3092** | `+91.5` | **18.5** / 26 | 12 (10-2) | 13 (3-10) | 1 (0-1) | 71.2% |
| 4 | **Renegade 1.3.1** | 3000 | **3146** | `+146.0` | **18.0** / 22 | 15 (10-5) | 6 (1-5) | 1 (0-1) | 81.8% |
| 5 | **Triumviratus 6.0 Dotprod** | 3000 | **3119** | `+118.5` | **18.0** / 24 | 14 (9-5) | 8 (3-5) | 2 (0-2) | 75.0% |
| 6 | **Coda 0.9.3 AI** | 3000 | **3112** | `+112.1` | **18.0** / 24 | 13 (11-2) | 10 (1-9) | 1 (0-1) | 75.0% |
| 7 | **Tcheran 14.0 dev** | 3000 | **3089** | `+89.0` | **16.0** / 24 | 10 (6-4) | 12 (6-6) | 2 (0-2) | 66.7% |
| 8 | **Panda 2.0** | 3000 | **3083** | `+82.9` | **15.5** / 22 | 13 (7-6) | 5 (3-2) | 4 (1-3) | 70.5% |
| 9 | **Minke 6.0.0 Dotprod** | 3000 | **3073** | `+72.9` | **15.5** / 24 | 11 (9-2) | 9 (3-6) | 4 (0-4) | 64.6% |
| 10 | **Elixir 3.0** | 3000 | **3041** | `+41.2` | **14.5** / 26 | 6 (4-2) | 17 (8-9) | 3 (1-2) | 55.8% |
| 11 | **Rice dev 1169a58** | 3000 | **3068** | `+67.8` | **14.0** / 22 | 9 (7-2) | 10 (4-6) | 3 (0-3) | 63.6% |
| 12 | **Zangdar 7.0** | 3000 | **3022** | `+22.2` | **13.0** / 24 | 8 (4-4) | 10 (5-5) | 6 (3-3) | 54.2% |
| 13 | **Iris 2.0 dev** | 3000 | **2986** | `-13.9` | **13.0** / 26 | 8 (7-1) | 10 (5-5) | 8 (1-7) | 50.0% |
| 14 | **Sirius 9.0 Dotprod** | 3000 | **3046** | `+46.4` | **12.5** / 22 | 9 (7-2) | 7 (4-3) | 6 (0-6) | 56.8% |
| 15 | **Ursus 1.0.0** | 3000 | **3011** | `+10.8` | **12.0** / 24 | 7 (5-2) | 10 (6-4) | 7 (1-6) | 50.0% |
| 16 | **Tarnished 6.0** | 3000 | **3015** | `+15.0` | **11.5** / 22 | 8 (7-1) | 7 (4-3) | 7 (0-7) | 52.3% |
| 17 | **Ruthorin 1.9.9** | 3000 | **3009** | `+9.5` | **11.5** / 22 | 8 (6-2) | 7 (3-4) | 7 (2-5) | 52.3% |
| 18 | **Zigqueen 5.8.3 AI** | 3000 | **3005** | `+5.0` | **11.5** / 24 | 6 (6-0) | 11 (4-7) | 7 (2-5) | 47.9% |
| 19 | **Igel 3.6.3 Dotprod** | 3000 | **2947** | `-53.4` | **11.5** / 26 | 5 (4-1) | 13 (6-7) | 8 (3-5) | 44.2% |
| 20 | **Lunar 0.4.0 dev** | 3000 | **2982** | `-18.3` | **10.5** / 24 | 7 (5-2) | 7 (5-2) | 10 (2-8) | 43.8% |
| 21 | **Carp 3.0.1** | 3000 | **2974** | `-26.0` | **10.5** / 24 | 5 (4-1) | 11 (6-5) | 8 (2-6) | 43.8% |
| 22 | **Prelude 2.1 dev** | 3000 | **2980** | `-20.3` | **10.0** / 22 | 4 (3-1) | 12 (7-5) | 6 (1-5) | 45.5% |
| 23 | **Avalanche 3.1.0 dev** | 3000 | **2963** | `-37.0` | **10.0** / 24 | 3 (3-0) | 14 (8-6) | 7 (1-6) | 41.7% |
| 24 | **Weiss 2.1 dev e3bf1e5** | 3000 | **2963** | `-37.5` | **10.0** / 24 | 3 (3-0) | 14 (7-7) | 7 (2-5) | 41.7% |
| 25 | **Eleanor 4.1** | 3000 | **2954** | `-46.0` | **10.0** / 24 | 4 (3-1) | 12 (8-4) | 8 (1-7) | 41.7% |
| 26 | **Tucano 12.17 Dotprod** | 3000 | **2940** | `-60.2` | **9.5** / 24 | 7 (6-1) | 5 (3-2) | 12 (3-9) | 39.6% |
| 27 | **Bread 3.0.0 Dotprod** | 3000 | **2965** | `-35.4` | **9.0** / 24 | 2 (2-0) | 14 (10-4) | 8 (0-8) | 37.5% |
| 28 | **Grail 2.0.1** | 3000 | **2916** | `-83.8` | **9.0** / 26 | 3 (1-2) | 12 (10-2) | 11 (2-9) | 34.6% |
| 29 | **Lambergar 1.2** | 3000 | **2925** | `-74.7` | **8.5** / 24 | 6 (3-3) | 5 (5-0) | 13 (4-9) | 35.4% |
| 30 | **Illumina 3 dev 85c Dotprod** | 3000 | **2895** | `-105.1` | **8.0** / 26 | 3 (3-0) | 10 (8-2) | 13 (2-11) | 30.8% |
| 31 | **Cataphract 1.3 Dotprod** | 3000 | **2899** | `-100.6` | **7.0** / 24 | 1 (1-0) | 12 (7-5) | 11 (4-7) | 29.2% |
| 32 | **Peacekeeper 0B** | 3000 | **2897** | `-102.8` | **5.5** / 22 | 2 (1-1) | 7 (4-3) | 13 (6-7) | 25.0% |
| 33 | **Spaghet 1.1.3** | 3000 | **2837** | `-163.5` | **4.0** / 24 | 2 (1-1) | 4 (2-2) | 18 (9-9) | 16.7% |
| 34 | **Luna 2.1.0** | 3000 | **2755** | `-245.4` | **0.0** / 24 | 0 (0-0) | 0 (0-0) | 24 (12-12) | 0.0% |

<details><summary><b>🛠️ View Developer Performance Logs (Speed, Stability & Color Stats)</b></summary>

| Engine | White Win % | Black Win % | Avg Game Length | Time Losses | Illegal/Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Hobbes 3.0** | 100.0% | 69.2% | 127.2 moves | `0` | `0` |
| **Halogen 16.7.12** | 92.3% | 61.5% | 104.6 moves | `1` | `0` |
| **Icarus 1.1.1 dev** | 88.5% | 53.8% | 120.5 moves | `0` | `0` |
| **Renegade 1.3.1** | 95.5% | 68.2% | 103.8 moves | `0` | `0` |
| **Triumviratus 6.0 Dotprod** | 87.5% | 62.5% | 117.2 moves | `0` | `0` |
| **Coda 0.9.3 AI** | 95.8% | 54.2% | 103.1 moves | `0` | `0` |
| **Tcheran 14.0 dev** | 75.0% | 58.3% | 124.2 moves | `0` | `0` |
| **Panda 2.0** | 77.3% | 63.6% | 117.9 moves | `0` | `0` |
| **Minke 6.0.0 Dotprod** | 87.5% | 41.7% | 126.3 moves | `0` | `0` |
| **Elixir 3.0** | 61.5% | 50.0% | 126.7 moves | `0` | `0` |
| **Rice dev 1169a58** | 81.8% | 45.5% | 124.0 moves | `0` | `0` |
| **Zangdar 7.0** | 54.2% | 54.2% | 119.2 moves | `2` | `0` |
| **Iris 2.0 dev** | 73.1% | 26.9% | 119.9 moves | `0` | `0` |
| **Sirius 9.0 Dotprod** | 81.8% | 31.8% | 117.0 moves | `0` | `0` |
| **Ursus 1.0.0** | 66.7% | 33.3% | 121.3 moves | `0` | `0` |
| **Tarnished 6.0** | 81.8% | 22.7% | 125.5 moves | `0` | `0` |
| **Ruthorin 1.9.9** | 68.2% | 36.4% | 131.4 moves | `0` | `0` |
| **Zigqueen 5.8.3 AI** | 66.7% | 29.2% | 124.6 moves | `0` | `0` |
| **Igel 3.6.3 Dotprod** | 53.8% | 34.6% | 116.3 moves | `0` | `0` |
| **Lunar 0.4.0 dev** | 62.5% | 25.0% | 121.7 moves | `0` | `0` |
| **Carp 3.0.1** | 58.3% | 29.2% | 155.3 moves | `0` | `0` |
| **Prelude 2.1 dev** | 59.1% | 31.8% | 106.2 moves | `0` | `0` |
| **Avalanche 3.1.0 dev** | 58.3% | 25.0% | 148.1 moves | `0` | `0` |
| **Weiss 2.1 dev e3bf1e5** | 54.2% | 29.2% | 115.2 moves | `0` | `0` |
| **Eleanor 4.1** | 58.3% | 25.0% | 126.1 moves | `0` | `0` |
| **Tucano 12.17 Dotprod** | 62.5% | 16.7% | 118.9 moves | `1` | `0` |
| **Bread 3.0.0 Dotprod** | 58.3% | 16.7% | 134.2 moves | `0` | `0` |
| **Grail 2.0.1** | 46.2% | 23.1% | 141.0 moves | `0` | `0` |
| **Lambergar 1.2** | 45.8% | 25.0% | 121.1 moves | `0` | `0` |
| **Illumina 3 dev 85c Dotprod** | 53.8% | 7.7% | 117.2 moves | `0` | `0` |
| **Cataphract 1.3 Dotprod** | 37.5% | 20.8% | 133.7 moves | `0` | `0` |
| **Peacekeeper 0B** | 27.3% | 22.7% | 84.6 moves | `12` | `0` |
| **Spaghet 1.1.3** | 16.7% | 16.7% | 87.6 moves | `4` | `0` |
| **Luna 2.1.0** | 0.0% | 0.0% | 68.8 moves | `0` | `0` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** | **25** | **26** | **27** | **28** | **29** | **30** | **31** | **32** | **33** | **34** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Hobbes 3.0** | — | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **2. Halogen 16.7.12** | * | — | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **3. Icarus 1.1.1 dev** | * | * | — | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **4. Renegade 1.3.1** | * | * | * | — | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **5. Triumviratus 6.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | — | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **6. Coda 0.9.3 AI** | * | * | * | * | * | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * |
| **7. Tcheran 14.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | — | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **8. Panda 2.0** | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | — | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **9. Minke 6.0.0 Dotprod** | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | — | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **10. Elixir 3.0** | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | — | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * |
| **11. Rice dev 1169a58** | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | — | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **12. Zangdar 7.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | — | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * |
| **13. Iris 2.0 dev** | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | — | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * |
| **14. Sirius 9.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 0</nobr><br>(0.0) | — | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **15. Ursus 1.0.0** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * |
| **16. Tarnished 6.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | — | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **17. Ruthorin 1.9.9** | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | — | * | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **18. Zigqueen 5.8.3 AI** | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | * | — | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * |
| **19. Igel 3.6.3 Dotprod** | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **20. Lunar 0.4.0 dev** | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | — | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **21. Carp 3.0.1** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | — | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * |
| **22. Prelude 2.1 dev** | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | — | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **23. Avalanche 3.1.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 1</nobr><br>(0.0) | * | — | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * |
| **24. Weiss 2.1 dev e3bf1e5** | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | — | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * |
| **25. Eleanor 4.1** | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * |
| **26. Tucano 12.17 Dotprod** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | — | * | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **27. Bread 3.0.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | — | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * |
| **28. Grail 2.0.1** | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | — | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * |
| **29. Lambergar 1.2** | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | — | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **30. Illumina 3 dev 85c Dotprod** | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | — | * | * | <nobr>½ ½</nobr><br>(0.0) | * |
| **31. Cataphract 1.3 Dotprod** | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | — | * | * | * |
| **32. Peacekeeper 0B** | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | — | * | <nobr>1 1</nobr><br>(+2.0) |
| **33. Spaghet 1.1.3** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | — | <nobr>1 1</nobr><br>(+2.0) |
| **34. Luna 2.1.0** | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | — |

</details>


---


<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
