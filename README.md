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

---

<!-- STATS_START -->
🔄 **Post-Season Relegation & Capped Pool (Executed after Finals)**

Because MCEC maintains a strict cap of 72 engines through dynamic newcomers:

* **The Survival**: Gateway bottom half and matching number of fringe engines fight for survival.
* **The Fringe**: Lower-tier survival league (Ranked 49–72).
* **The Crucible**: Gateway-mirrored sizing (half of gateway size) where fringe engines and kicked-out engines fight to defend or earn their spot in the circuit.

---

## 🏆 Active Stage: Gateway

> 📊 **Active Stage Summary:** **533** Total Games Played
> ⚪ **White Wins:** 249 (46.7%) | ⬛ **Black Wins:** 86 (16.1%) | 🤝 **Draws:** 198 (37.1%)

#### 🏆 Standings

| Rank | Engine | Score |
| :---: | :--- | :---: |
| 1 | **Hobbes 3.0** | **28.5** / 34 |
| 2 | **Renegade 1.3.1** | **24.5** / 30 |
| 3 | **Halogen 16.7.12** | **24.5** / 32 |
| 4 | **Icarus 1.1.1 dev** | **23.5** / 34 |
| 5 | **Coda 0.9.3 AI** | **23.0** / 32 |
| 6 | **Triumviratus 6.0 Dotprod** | **21.5** / 28 |
| 7 | **Minke 6.0.0 Dotprod** | **21.0** / 32 |
| 8 | **Tcheran 14.0 dev** | **19.5** / 28 |
| 9 | **Zangdar 7.0** | **19.0** / 32 |
| 10 | **Panda 2.0** | **18.0** / 31 |
| 11 | **Iris 2.0 dev** | **18.0** / 34 |
| 12 | **Rice dev 1169a58** | **17.5** / 30 |
| 13 | **Ruthorin 1.9.9** | **16.0** / 30 |
| 14 | **Sirius 9.0 Dotprod** | **16.0** / 30 |
| 15 | **Elixir 3.0** | **16.0** / 32 |
| 16 | **Carp 3.0.1** | **15.0** / 32 |
| 17 | **Weiss 2.1 dev e3bf1e5** | **15.0** / 32 |
| 18 | **Ursus 1.0.0** | **15.0** / 31 |
| 19 | **Avalanche 3.1.0 dev** | **15.0** / 32 |
| 20 | **Igel 3.6.3 Dotprod** | **15.0** / 34 |
| 21 | **Zigqueen 5.8.3 AI** | **14.5** / 30 |
| 22 | **Prelude 2.1 dev** | **14.5** / 30 |
| 23 | **Lunar 0.4.0 dev** | **14.5** / 32 |
| 24 | **Tarnished 6.0** | **13.5** / 28 |
| 25 | **Tucano 12.17 Dotprod** | **13.0** / 30 |
| 26 | **Eleanor 4.1** | **13.0** / 32 |
| 27 | **Grail 2.0.1** | **12.0** / 32 |
| 28 | **Bread 3.0.0 Dotprod** | **12.0** / 32 |
| 29 | **Illumina 3 dev 85c Dotprod** | **12.0** / 34 |
| 30 | **Lambergar 1.2** | **10.5** / 32 |
| 31 | **Peacekeeper 0B** | **8.5** / 30 |
| 32 | **Cataphract 1.3 Dotprod** | **8.5** / 32 |
| 33 | **Spaghet 1.1.3** | **5.0** / 30 |
| 34 | **Luna 2.1.0** | **0.0** / 32 |

<details><summary><b>📈 View Full Rating Lists / Full Engines (Elo Updates, Win % & Loss %)</b></summary>

| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win % | Loss % | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| #37 | **Hobbes 3.0** | 3000 | **3181** | `+180.6` | **28.5** / 34 | 67.6% | 0.0% | 🟢 Advanced to Entry League |
| #38 | **Renegade 1.3.1** | 3000 | **3171** | `+171.0` | **24.5** / 30 | 70.0% | 6.7% | 🟢 Advanced to Entry League |
| #39 | **Halogen 16.7.12** | 3000 | **3153** | `+152.7` | **24.5** / 32 | 56.2% | 3.1% | 🟢 Advanced to Entry League |
| #40 | **Icarus 1.1.1 dev** | 3000 | **3083** | `+83.3` | **23.5** / 34 | 47.1% | 8.8% | 🟢 Advanced to Entry League |
| #41 | **Coda 0.9.3 AI** | 3000 | **3137** | `+137.0` | **23.0** / 32 | 50.0% | 6.2% | 🟢 Advanced to Entry League |
| #42 | **Triumviratus 6.0 Dotprod** | 3000 | **3155** | `+155.1` | **21.5** / 28 | 60.7% | 7.1% | 🟢 Advanced to Entry League |
| #43 | **Minke 6.0.0 Dotprod** | 3000 | **3101** | `+100.9` | **21.0** / 32 | 50.0% | 18.8% | 🟢 Advanced to Entry League |
| #44 | **Tcheran 14.0 dev** | 3000 | **3119** | `+119.1` | **19.5** / 28 | 46.4% | 7.1% | 🟢 Advanced to Entry League |
| #45 | **Zangdar 7.0** | 3000 | **3042** | `+41.9` | **19.0** / 32 | 43.8% | 25.0% | 🟢 Advanced to Entry League |
| #46 | **Panda 2.0** | 3000 | **3009** | `+9.3` | **18.0** / 31 | 45.2% | 29.0% | 🟢 Advanced to Entry League |
| #47 | **Iris 2.0 dev** | 3000 | **3009** | `+8.7` | **18.0** / 34 | 35.3% | 29.4% | 🟢 Advanced to Entry League |
| #48 | **Rice dev 1169a58** | 3000 | **3051** | `+50.7` | **17.5** / 30 | 36.7% | 20.0% | 🟢 Advanced to Entry League |
| #49 | **Ruthorin 1.9.9** | 3000 | **3035** | `+35.4` | **16.0** / 30 | 36.7% | 30.0% | 🟢 Advanced to Entry League |
| #50 | **Sirius 9.0 Dotprod** | 3000 | **3024** | `+24.2` | **16.0** / 30 | 40.0% | 33.3% | 🟢 Advanced to Entry League |
| #51 | **Elixir 3.0** | 3000 | **3008** | `+8.0` | **16.0** / 32 | 18.8% | 18.8% | 🟢 Advanced to Entry League |
| #52 | **Carp 3.0.1** | 3000 | **2996** | `-4.1` | **15.0** / 32 | 25.0% | 31.2% | 🟢 Advanced to Entry League |
| #53 | **Weiss 2.1 dev e3bf1e5** | 3000 | **2981** | `-18.7` | **15.0** / 32 | 25.0% | 31.2% | 🟢 Advanced to Entry League |
| #54 | **Ursus 1.0.0** | 3000 | **2980** | `-19.8` | **15.0** / 31 | 29.0% | 32.3% | 🔴 Relegated to The Survival |
| #55 | **Avalanche 3.1.0 dev** | 3000 | **2968** | `-31.8` | **15.0** / 32 | 21.9% | 28.1% | 🔴 Relegated to The Survival |
| #56 | **Igel 3.6.3 Dotprod** | 3000 | **2941** | `-59.4` | **15.0** / 34 | 20.6% | 32.4% | 🔴 Relegated to The Survival |
| #57 | **Zigqueen 5.8.3 AI** | 3000 | **3002** | `+2.2` | **14.5** / 30 | 23.3% | 26.7% | 🔴 Relegated to The Survival |
| #58 | **Prelude 2.1 dev** | 3000 | **2998** | `-1.5` | **14.5** / 30 | 26.7% | 30.0% | 🔴 Relegated to The Survival |
| #59 | **Lunar 0.4.0 dev** | 3000 | **2985** | `-15.3` | **14.5** / 32 | 31.2% | 40.6% | 🔴 Relegated to The Survival |
| #60 | **Tarnished 6.0** | 3000 | **2981** | `-18.7` | **13.5** / 28 | 32.1% | 35.7% | 🔴 Relegated to The Survival |
| #61 | **Tucano 12.17 Dotprod** | 3000 | **2980** | `-19.9` | **13.0** / 30 | 33.3% | 46.7% | 🔴 Relegated to The Survival |
| #62 | **Eleanor 4.1** | 3000 | **2966** | `-34.1` | **13.0** / 32 | 15.6% | 34.4% | 🔴 Relegated to The Survival |
| #63 | **Grail 2.0.1** | 3000 | **2937** | `-63.3` | **12.0** / 32 | 9.4% | 34.4% | 🔴 Relegated to The Survival |
| #64 | **Bread 3.0.0 Dotprod** | 3000 | **2933** | `-67.1` | **12.0** / 32 | 9.4% | 34.4% | 🔴 Relegated to The Survival |
| #65 | **Illumina 3 dev 85c Dotprod** | 3000 | **2907** | `-92.6` | **12.0** / 34 | 14.7% | 44.1% | 🔴 Relegated to The Survival |
| #66 | **Lambergar 1.2** | 3000 | **2882** | `-118.3` | **10.5** / 32 | 21.9% | 56.2% | 🔴 Relegated to The Survival |
| #67 | **Peacekeeper 0B** | 3000 | **2896** | `-104.4` | **8.5** / 30 | 16.7% | 60.0% | 🔴 Relegated to The Survival |
| #68 | **Cataphract 1.3 Dotprod** | 3000 | **2868** | `-131.6` | **8.5** / 32 | 3.1% | 50.0% | 🔴 Relegated to The Survival |
| #69 | **Spaghet 1.1.3** | 3000 | **2813** | `-186.9` | **5.0** / 30 | 10.0% | 76.7% | 🔴 Relegated to The Survival |
| #70 | **Luna 2.1.0** | 3000 | **2707** | `-292.6` | **0.0** / 32 | 0.0% | 100.0% | 🔴 Relegated to The Survival |

</details>

<details><summary><b>🛠️ View Developer Performance Logs</b></summary>

| Engine | Stage Rank | Win % | Draw % | White Win % | Black Win % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Time Losses | Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hobbes 3.0** | #1 | 67.6% | 32.4% | 100.0% | 67.6% | 61.8 moves | 24 / 92 moves | 40 / 123 moves | N/A | `0` | `0` |
| **Renegade 1.3.1** | #2 | 70.0% | 23.3% | 96.7% | 66.7% | 57.0 moves | 27 / 109 moves | 31 / 85 moves | 63 / 100 moves | `0` | `0` |
| **Halogen 16.7.12** | #3 | 56.2% | 40.6% | 90.6% | 62.5% | 52.5 moves | 31 / 76 moves | 33 / 77 moves | 60 / 60 moves | `1` | `0` |
| **Icarus 1.1.1 dev** | #4 | 47.1% | 44.1% | 88.2% | 50.0% | 60.7 moves | 24 / 87 moves | 36 / 112 moves | 57 / 79 moves | `0` | `0` |
| **Coda 0.9.3 AI** | #5 | 50.0% | 43.8% | 90.6% | 53.1% | 58.3 moves | 37 / 81 moves | 35 / 123 moves | 59 / 73 moves | `0` | `0` |
| **Triumviratus 6.0 Dotprod** | #6 | 60.7% | 32.1% | 89.3% | 64.3% | 58.0 moves | 33 / 81 moves | 27 / 101 moves | 74 / 77 moves | `0` | `0` |
| **Minke 6.0.0 Dotprod** | #7 | 50.0% | 31.2% | 87.5% | 43.8% | 63.7 moves | 24 / 92 moves | 41 / 93 moves | 45 / 85 moves | `0` | `0` |
| **Tcheran 14.0 dev** | #8 | 46.4% | 46.4% | 78.6% | 60.7% | 59.8 moves | 11 / 79 moves | 40 / 154 moves | 70 / 92 moves | `0` | `0` |
| **Zangdar 7.0** | #9 | 43.8% | 31.2% | 59.4% | 59.4% | 57.2 moves | 25 / 65 moves | 44 / 108 moves | 32 / 84 moves | `4` | `0` |
| **Panda 2.0** | #10 | 45.2% | 25.8% | 65.6% | 50.0% | 63.1 moves | 19 / 126 moves | 53 / 161 moves | 47 / 90 moves | `0` | `0` |
| **Iris 2.0 dev** | #11 | 35.3% | 35.3% | 79.4% | 26.5% | 59.4 moves | 22 / 100 moves | 41 / 154 moves | 33 / 72 moves | `0` | `0` |
| **Rice dev 1169a58** | #12 | 36.7% | 43.3% | 80.0% | 36.7% | 61.4 moves | 21 / 67 moves | 41 / 161 moves | 45 / 91 moves | `0` | `0` |
| **Ruthorin 1.9.9** | #13 | 36.7% | 33.3% | 66.7% | 40.0% | 64.4 moves | 26 / 110 moves | 41 / 161 moves | 48 / 93 moves | `0` | `0` |
| **Sirius 9.0 Dotprod** | #14 | 40.0% | 26.7% | 83.3% | 23.3% | 56.3 moves | 27 / 67 moves | 36 / 91 moves | 48 / 85 moves | `0` | `0` |
| **Elixir 3.0** | #15 | 18.8% | 62.5% | 56.2% | 43.8% | 59.8 moves | 36 / 63 moves | 39 / 104 moves | 24 / 76 moves | `0` | `0` |
| **Carp 3.0.1** | #16 | 25.0% | 43.8% | 65.6% | 28.1% | 71.3 moves | 42 / 114 moves | 32 / 161 moves | 41 / 123 moves | `0` | `0` |
| **Weiss 2.1 dev e3bf1e5** | #17 | 25.0% | 43.8% | 59.4% | 34.4% | 56.6 moves | 19 / 68 moves | 33 / 107 moves | 37 / 92 moves | `0` | `0` |
| **Ursus 1.0.0** | #18 | 29.0% | 38.7% | 63.3% | 34.4% | 59.5 moves | 28 / 120 moves | 39 / 129 moves | 37 / 59 moves | `0` | `0` |
| **Avalanche 3.1.0 dev** | #19 | 21.9% | 50.0% | 65.6% | 28.1% | 68.3 moves | 26 / 74 moves | 41 / 161 moves | 33 / 92 moves | `0` | `0` |
| **Igel 3.6.3 Dotprod** | #20 | 20.6% | 47.1% | 55.9% | 32.4% | 61.7 moves | 30 / 94 moves | 27 / 108 moves | 32 / 83 moves | `0` | `0` |
| **Zigqueen 5.8.3 AI** | #21 | 23.3% | 50.0% | 66.7% | 30.0% | 62.8 moves | 24 / 123 moves | 31 / 161 moves | 29 / 74 moves | `0` | `0` |
| **Prelude 2.1 dev** | #22 | 26.7% | 43.3% | 63.3% | 33.3% | 49.3 moves | 24 / 48 moves | 35 / 78 moves | 37 / 103 moves | `0` | `0` |
| **Lunar 0.4.0 dev** | #23 | 31.2% | 28.1% | 59.4% | 31.2% | 61.5 moves | 20 / 103 moves | 35 / 161 moves | 37 / 110 moves | `0` | `0` |
| **Tarnished 6.0** | #24 | 32.1% | 32.1% | 78.6% | 17.9% | 64.5 moves | 19 / 114 moves | 48 / 140 moves | 20 / 126 moves | `0` | `0` |
| **Tucano 12.17 Dotprod** | #25 | 33.3% | 20.0% | 66.7% | 20.0% | 63.7 moves | 33 / 85 moves | 41 / 144 moves | 35 / 89 moves | `1` | `0` |
| **Eleanor 4.1** | #26 | 15.6% | 50.0% | 59.4% | 21.9% | 61.7 moves | 47 / 66 moves | 39 / 161 moves | 45 / 114 moves | `0` | `0` |
| **Grail 2.0.1** | #27 | 9.4% | 56.2% | 46.9% | 28.1% | 69.9 moves | 35 / 44 moves | 31 / 154 moves | 36 / 120 moves | `0` | `0` |
| **Bread 3.0.0 Dotprod** | #28 | 9.4% | 56.2% | 59.4% | 15.6% | 66.8 moves | 50 / 60 moves | 43 / 103 moves | 52 / 94 moves | `0` | `0` |
| **Illumina 3 dev 85c Dotprod** | #29 | 14.7% | 41.2% | 58.8% | 11.8% | 61.4 moves | 25 / 81 moves | 39 / 161 moves | 42 / 114 moves | `0` | `0` |
| **Lambergar 1.2** | #30 | 21.9% | 21.9% | 46.9% | 18.8% | 60.1 moves | 21 / 89 moves | 36 / 129 moves | 35 / 112 moves | `0` | `0` |
| **Peacekeeper 0B** | #31 | 16.7% | 23.3% | 40.0% | 16.7% | 43.9 moves | 25 / 56 moves | 43 / 92 moves | 11 / 92 moves | `16` | `0` |
| **Cataphract 1.3 Dotprod** | #32 | 3.1% | 46.9% | 34.4% | 18.8% | 67.6 moves | 58 / 58 moves | 31 / 161 moves | 24 / 74 moves | `0` | `0` |
| **Spaghet 1.1.3** | #33 | 10.0% | 13.3% | 20.0% | 13.3% | 46.8 moves | 36 / 59 moves | 39 / 114 moves | 24 / 109 moves | `5` | `0` |
| **Luna 2.1.0** | #34 | 0.0% | 0.0% | 0.0% | 0.0% | 33.4 moves | N/A | N/A | 19 / 75 moves | `0` | `0` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **#1** | **#2** | **#3** | **#4** | **#5** | **#6** | **#7** | **#8** | **#9** | **#10** | **#11** | **#12** | **#13** | **#14** | **#15** | **#16** | **#17** | **#18** | **#19** | **#20** | **#21** | **#22** | **#23** | **#24** | **#25** | **#26** | **#27** | **#28** | **#29** | **#30** | **#31** | **#32** | **#33** | **#34** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **#1. Hobbes 3.0** | — | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **#2. Renegade 1.3.1** | * | — | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#3. Halogen 16.7.12** | * | * | — | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **#4. Icarus 1.1.1 dev** | * | * | * | — | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **#5. Coda 0.9.3 AI** | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | — | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * |
| **#6. Triumviratus 6.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | — | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#7. Minke 6.0.0 Dotprod** | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **#8. Tcheran 14.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | — | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#9. Zangdar 7.0** | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | — | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **#10. Panda 2.0** | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | — | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#11. Iris 2.0 dev** | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | * | — | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * |
| **#12. Rice dev 1169a58** | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#13. Ruthorin 1.9.9** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | — | * | * | * | * | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#14. Sirius 9.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | — | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#15. Elixir 3.0** | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | — | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * |
| **#16. Carp 3.0.1** | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | — | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * |
| **#17. Weiss 2.1 dev e3bf1e5** | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | — | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **#18. Ursus 1.0.0** | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | — | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **#19. Avalanche 3.1.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | * | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **#20. Igel 3.6.3 Dotprod** | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **#21. Zigqueen 5.8.3 AI** | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | — | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * |
| **#22. Prelude 2.1 dev** | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#23. Lunar 0.4.0 dev** | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | — | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **#24. Tarnished 6.0** | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 1</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | — | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#25. Tucano 12.17 Dotprod** | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **#26. Eleanor 4.1** | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * |
| **#27. Grail 2.0.1** | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * |
| **#28. Bread 3.0.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | — | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * |
| **#29. Illumina 3 dev 85c Dotprod** | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | — | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * |
| **#30. Lambergar 1.2** | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | — | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **#31. Peacekeeper 0B** | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | — | * | <nobr>0 1</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#32. Cataphract 1.3 Dotprod** | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | — | * | * |
| **#33. Spaghet 1.1.3** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | * | — | <nobr>1 1</nobr><br>(+2.0) |
| **#34. Luna 2.1.0** | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | — |

</details>


---


<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
