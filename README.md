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

> 📊 **Stage Summary:** **340** Total Games Played
> ⚪ **White Wins:** 153 (45.0%) | ⬛ **Black Wins:** 53 (15.6%) | 🤝 **Draws:** 134 (39.4%)

#### 📊 Leaderboard

| Rank | Engine | Start Elo | End Elo | Change (Δ) | Points / Played | <nobr>W - D - L</nobr> | Win % |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Hobbes 3.0** | 3200 | **3361** | `+160.8` | **19.0** / 22 | <nobr>16-6-0</nobr> | 86.4% |
| 2 | **Halogen 16.7.12** | 3200 | **3313** | `+112.9` | **16.5** / 22 | <nobr>12-9-1</nobr> | 75.0% |
| 3 | **Coda 0.9.3 AI** | 3200 | **3312** | `+111.8` | **16.5** / 22 | <nobr>12-9-1</nobr> | 75.0% |
| 4 | **Icarus 1.1.1 dev** | 3200 | **3280** | `+80.1` | **15.5** / 22 | <nobr>10-11-1</nobr> | 70.5% |
| 5 | **Renegade 1.3.1** | 3200 | **3338** | `+137.6` | **15.0** / 18 | <nobr>13-4-1</nobr> | 83.3% |
| 6 | **Triumviratus 6.0 Dotprod** | 3200 | **3286** | `+86.5` | **14.0** / 20 | <nobr>10-8-2</nobr> | 70.0% |
| 7 | **Panda 2.0** | 3200 | **3291** | `+91.0` | **13.0** / 18 | <nobr>11-4-3</nobr> | 72.2% |
| 8 | **Minke 6.0.0 Dotprod** | 3200 | **3283** | `+83.1` | **12.0** / 18 | <nobr>8-8-2</nobr> | 66.7% |
| 9 | **Elixir 3.0** | 3200 | **3235** | `+35.2` | **12.0** / 22 | <nobr>5-14-3</nobr> | 54.5% |
| 10 | **Tcheran 14.0 dev** | 3200 | **3268** | `+67.7` | **11.5** / 18 | <nobr>7-9-2</nobr> | 63.9% |
| 11 | **Sirius 9.0 Dotprod** | 3200 | **3225** | `+24.6` | **11.0** / 20 | <nobr>8-6-6</nobr> | 55.0% |
| 12 | **Iris 2.0 dev** | 3200 | **3187** | `-12.7` | **11.0** / 22 | <nobr>7-8-7</nobr> | 50.0% |
| 13 | **Rice dev 1169a58** | 3200 | **3238** | `+38.2` | **10.5** / 18 | <nobr>6-9-3</nobr> | 58.3% |
| 14 | **Igel 3.6.3 Dotprod** | 3200 | **3174** | `-25.7` | **10.5** / 22 | <nobr>5-11-6</nobr> | 47.7% |
| 15 | **Zigqueen 5.8.3 AI** | 3200 | **3206** | `+5.7` | **10.0** / 20 | <nobr>6-8-6</nobr> | 50.0% |
| 16 | **Ruthorin 1.9.9** | 3200 | **3202** | `+1.8` | **10.0** / 20 | <nobr>7-6-7</nobr> | 50.0% |
| 17 | **Tarnished 6.0** | 3200 | **3208** | `+8.2` | **9.5** / 18 | <nobr>6-7-5</nobr> | 52.8% |
| 18 | **Zangdar 7.0** | 3200 | **3187** | `-13.4` | **9.5** / 20 | <nobr>5-9-6</nobr> | 47.5% |
| 19 | **Carp 3.0.1** | 3200 | **3178** | `-21.7` | **9.5** / 20 | <nobr>5-9-6</nobr> | 47.5% |
| 20 | **Eleanor 4.1** | 3200 | **3164** | `-36.2` | **9.5** / 22 | <nobr>4-11-7</nobr> | 43.2% |
| 21 | **Prelude 2.1 dev** | 3200 | **3192** | `-8.1` | **9.0** / 18 | <nobr>4-10-4</nobr> | 50.0% |
| 22 | **Ursus 1.0.0** | 3200 | **3184** | `-15.9` | **9.0** / 20 | <nobr>5-8-7</nobr> | 45.0% |
| 23 | **Lunar 0.4.0 dev** | 3200 | **3198** | `-2.0` | **8.5** / 18 | <nobr>6-5-7</nobr> | 47.2% |
| 24 | **Weiss 2.1 dev e3bf1e5** | 3200 | **3186** | `-14.4` | **8.5** / 20 | <nobr>3-11-6</nobr> | 42.5% |
| 25 | **Avalanche 3.1.0 dev** | 3200 | **3171** | `-28.5` | **8.5** / 20 | <nobr>3-11-6</nobr> | 42.5% |
| 26 | **Bread 3.0.0 Dotprod** | 3200 | **3170** | `-30.1` | **8.0** / 20 | <nobr>2-12-6</nobr> | 40.0% |
| 27 | **Tucano 12.17 Dotprod** | 3200 | **3157** | `-43.1` | **7.5** / 20 | <nobr>5-5-10</nobr> | 37.5% |
| 28 | **Grail 2.0.1** | 3200 | **3117** | `-83.2` | **7.5** / 22 | <nobr>3-9-10</nobr> | 34.1% |
| 29 | **Illumina 3 dev 85c Dotprod** | 3200 | **3093** | `-106.9` | **6.5** / 22 | <nobr>3-7-12</nobr> | 29.5% |
| 30 | **Cataphract 1.3 Dotprod** | 3200 | **3114** | `-86.2` | **6.0** / 20 | <nobr>1-10-9</nobr> | 30.0% |
| 31 | **Lambergar 1.2** | 3200 | **3100** | `-99.8` | **6.0** / 20 | <nobr>4-4-12</nobr> | 30.0% |
| 32 | **Peacekeeper 0B** | 3200 | **3126** | `-74.1` | **5.0** / 18 | <nobr>2-6-10</nobr> | 27.8% |
| 33 | **Spaghet 1.1.3** | 3200 | **3064** | `-136.1` | **4.0** / 20 | <nobr>2-4-14</nobr> | 20.0% |
| 34 | **Luna 2.1.0** | 3200 | **2993** | `-207.2` | **0.0** / 18 | <nobr>0-0-18</nobr> | 0.0% |

<details><summary><b>🛠️ View Developer Performance Logs (Speed, Stability & Color Stats)</b></summary>

| Engine | White Win % | Black Win % | Avg Game Length | Time Losses | Illegal/Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Hobbes 3.0** | 100.0% | 72.7% | 125.6 moves | `0` | `0` |
| **Halogen 16.7.12** | 90.9% | 59.1% | 105.3 moves | `1` | `0` |
| **Coda 0.9.3 AI** | 95.5% | 54.5% | 102.6 moves | `0` | `0` |
| **Icarus 1.1.1 dev** | 86.4% | 54.5% | 122.1 moves | `0` | `0` |
| **Renegade 1.3.1** | 94.4% | 72.2% | 109.8 moves | `0` | `0` |
| **Triumviratus 6.0 Dotprod** | 85.0% | 55.0% | 117.7 moves | `0` | `0` |
| **Panda 2.0** | 77.8% | 66.7% | 124.8 moves | `0` | `0` |
| **Minke 6.0.0 Dotprod** | 88.9% | 44.4% | 136.4 moves | `0` | `0` |
| **Elixir 3.0** | 59.1% | 50.0% | 129.3 moves | `0` | `0` |
| **Tcheran 14.0 dev** | 72.2% | 55.6% | 135.1 moves | `0` | `0` |
| **Sirius 9.0 Dotprod** | 80.0% | 30.0% | 117.8 moves | `0` | `0` |
| **Iris 2.0 dev** | 77.3% | 22.7% | 121.1 moves | `0` | `0` |
| **Rice dev 1169a58** | 77.8% | 38.9% | 136.7 moves | `0` | `0` |
| **Igel 3.6.3 Dotprod** | 59.1% | 36.4% | 120.4 moves | `0` | `0` |
| **Zigqueen 5.8.3 AI** | 70.0% | 30.0% | 130.8 moves | `0` | `0` |
| **Ruthorin 1.9.9** | 70.0% | 30.0% | 136.9 moves | `0` | `0` |
| **Tarnished 6.0** | 77.8% | 27.8% | 132.9 moves | `0` | `0` |
| **Zangdar 7.0** | 45.0% | 50.0% | 123.0 moves | `2` | `0` |
| **Carp 3.0.1** | 60.0% | 35.0% | 162.9 moves | `0` | `0` |
| **Eleanor 4.1** | 59.1% | 27.3% | 127.5 moves | `0` | `0` |
| **Prelude 2.1 dev** | 61.1% | 38.9% | 111.4 moves | `0` | `0` |
| **Ursus 1.0.0** | 65.0% | 25.0% | 117.2 moves | `0` | `0` |
| **Lunar 0.4.0 dev** | 66.7% | 27.8% | 126.6 moves | `0` | `0` |
| **Weiss 2.1 dev e3bf1e5** | 55.0% | 30.0% | 118.0 moves | `0` | `0` |
| **Avalanche 3.1.0 dev** | 60.0% | 25.0% | 160.3 moves | `0` | `0` |
| **Bread 3.0.0 Dotprod** | 60.0% | 20.0% | 130.9 moves | `0` | `0` |
| **Tucano 12.17 Dotprod** | 65.0% | 10.0% | 119.3 moves | `0` | `0` |
| **Grail 2.0.1** | 45.5% | 22.7% | 140.7 moves | `0` | `0` |
| **Illumina 3 dev 85c Dotprod** | 54.5% | 4.5% | 119.5 moves | `0` | `0` |
| **Cataphract 1.3 Dotprod** | 40.0% | 20.0% | 134.1 moves | `0` | `0` |
| **Lambergar 1.2** | 40.0% | 20.0% | 112.8 moves | `0` | `0` |
| **Peacekeeper 0B** | 33.3% | 22.2% | 89.5 moves | `9` | `0` |
| **Spaghet 1.1.3** | 20.0% | 20.0% | 91.3 moves | `3` | `0` |
| **Luna 2.1.0** | 0.0% | 0.0% | 66.3 moves | `0` | `0` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** | **25** | **26** | **27** | **28** | **29** | **30** | **31** | **32** | **33** | **34** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Hobbes 3.0** | — | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **2. Halogen 16.7.12** | * | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **3. Coda 0.9.3 AI** | * | * | — | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * |
| **4. Icarus 1.1.1 dev** | * | * | * | — | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **5. Renegade 1.3.1** | * | * | * | * | — | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **6. Triumviratus 6.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | — | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * |
| **7. Panda 2.0** | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | — | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **8. Minke 6.0.0 Dotprod** | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | — | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | * |
| **9. Elixir 3.0** | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | — | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * |
| **10. Tcheran 14.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | — | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * |
| **11. Sirius 9.0 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | — | <nobr>1 0</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **12. Iris 2.0 dev** | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | — | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | * |
| **13. Rice dev 1169a58** | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | — | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **14. Igel 3.6.3 Dotprod** | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | — | * | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * |
| **15. Zigqueen 5.8.3 AI** | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | — | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * |
| **16. Ruthorin 1.9.9** | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>0 1</nobr><br>(0.0) | * | — | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **17. Tarnished 6.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | — | * | * | * | * | * | * | * | * | * | * | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | * | <nobr>1 1</nobr><br>(+2.0) |
| **18. Zangdar 7.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | * | * | — | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) | * | * | * | * |
| **19. Carp 3.0.1** | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | — | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * |
| **20. Eleanor 4.1** | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | — | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * |
| **21. Prelude 2.1 dev** | * | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | — | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 1</nobr><br>(+2.0) |
| **22. Ursus 1.0.0** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | — | * | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * |
| **23. Lunar 0.4.0 dev** | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | <nobr>1 1</nobr><br>(+2.0) | * | — | * | * | * | * | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **24. Weiss 2.1 dev e3bf1e5** | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | — | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * |
| **25. Avalanche 3.1.0 dev** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>1 0</nobr><br>(0.0) | * | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | — | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * |
| **26. Bread 3.0.0 Dotprod** | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | — | * | <nobr>1 ½</nobr><br>(+1.0) | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * |
| **27. Tucano 12.17 Dotprod** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | <nobr>0 1</nobr><br>(0.0) | * | <nobr>0 1</nobr><br>(0.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | * | * | * | * | * | — | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | * | * |
| **28. Grail 2.0.1** | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | — | * | * | * | * | <nobr>½ 1</nobr><br>(+1.0) | * |
| **29. Illumina 3 dev 85c Dotprod** | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | — | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * |
| **30. Cataphract 1.3 Dotprod** | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | * | * | * | — | * | * | * | * |
| **31. Lambergar 1.2** | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | * | * | * | — | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | * |
| **32. Peacekeeper 0B** | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | * | * | * | * | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>½ 0</nobr><br>(-1.0) | * | * | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | — | * | <nobr>1 1</nobr><br>(+2.0) |
| **33. Spaghet 1.1.3** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | * | * | <nobr>0 ½</nobr><br>(-1.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | — | <nobr>1 1</nobr><br>(+2.0) |
| **34. Luna 2.1.0** | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | <nobr>0 0</nobr><br>(-2.0) | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | * | * | * | <nobr>0 0</nobr><br>(-2.0) | * | * | * | * | * | * | * | * | * | * | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | — |

</details>


---


<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
