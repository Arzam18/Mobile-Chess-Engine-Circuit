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

### 📊 Stage Overview: 01 Gateway
* **Total Games Played:** 531 | **White Wins:** 249 | **Black Wins:** 85 | **Draws:** 197

### 📈 View Full Rating Lists
| Rank | Engine | Start Elo | Current Elo | Δ Elo | Score | Win % | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | **Hobbes 3.0** | 3000.0 | **3180.6** | +180.6 | 28.5/34 | 83.8% | ⚔️ Active |
| 2 | **Renegade 1.3.1** | 3000.0 | **3171.0** | +171.0 | 24.5/30 | 81.7% | ⚔️ Active |
| 3 | **Halogen 16.7.12** | 3000.0 | **3152.7** | +152.7 | 24.5/32 | 76.6% | ⚔️ Active |
| 4 | **Icarus 1.1.1 dev** | 3000.0 | **3083.3** | +83.3 | 23.5/34 | 69.1% | ⚔️ Active |
| 5 | **Coda 0.9.3 AI** | 3000.0 | **3137.0** | +137.0 | 23.0/32 | 71.9% | ⚔️ Active |
| 6 | **Triumviratus 6.0 Dotprod** | 3000.0 | **3155.1** | +155.1 | 21.5/28 | 76.8% | ⚔️ Active |
| 7 | **Minke 6.0.0 Dotprod** | 3000.0 | **3089.2** | +89.2 | 20.0/31 | 64.5% | ⚔️ Active |
| 8 | **Tcheran 14.0 dev** | 3000.0 | **3119.1** | +119.1 | 19.5/28 | 69.6% | ⚔️ Active |
| 9 | **Zangdar 7.0** | 3000.0 | **3041.9** | +41.9 | 19.0/32 | 59.4% | ⚔️ Active |
| 10 | **Iris 2.0 dev** | 3000.0 | **3008.7** | +8.7 | 18.0/34 | 52.9% | ⚔️ Active |
| 11 | **Rice dev 1169a58** | 3000.0 | **3050.7** | +50.7 | 17.5/30 | 58.3% | ⚔️ Active |
| 12 | **Panda 2.0** | 3000.0 | **3010.8** | +10.8 | 17.5/30 | 58.3% | ⚔️ Active |
| 13 | **Ruthorin 1.9.9** | 3000.0 | **3035.4** | +35.4 | 16.0/30 | 53.3% | ⚔️ Active |
| 14 | **Sirius 9.0 Dotprod** | 3000.0 | **3024.2** | +24.2 | 16.0/30 | 53.3% | ⚔️ Active |
| 15 | **Elixir 3.0** | 3000.0 | **3008.0** | +8.0 | 16.0/32 | 50.0% | ⚔️ Active |
| 16 | **Carp 3.0.1** | 3000.0 | **2995.9** | -4.1 | 15.0/32 | 46.9% | ⚔️ Active |
| 17 | **Weiss 2.1 dev e3bf1e5** | 3000.0 | **2992.9** | -7.1 | 15.0/31 | 48.4% | ⚔️ Active |
| 18 | **Avalanche 3.1.0 dev** | 3000.0 | **2968.2** | -31.8 | 15.0/32 | 46.9% | ⚔️ Active |
| 19 | **Igel 3.6.3 Dotprod** | 3000.0 | **2940.6** | -59.4 | 15.0/34 | 44.1% | ⚔️ Active |
| 20 | **Zigqueen 5.8.3 AI** | 3000.0 | **3002.2** | +2.2 | 14.5/30 | 48.3% | ⚔️ Active |
| 21 | **Prelude 2.1 dev** | 3000.0 | **2998.5** | -1.5 | 14.5/30 | 48.3% | ⚔️ Active |
| 22 | **Lunar 0.4.0 dev** | 3000.0 | **2984.7** | -15.3 | 14.5/32 | 45.3% | ⚔️ Active |
| 23 | **Ursus 1.0.0** | 3000.0 | **2978.7** | -21.3 | 14.5/30 | 48.3% | ⚔️ Active |
| 24 | **Tarnished 6.0** | 3000.0 | **2981.3** | -18.7 | 13.5/28 | 48.2% | ⚔️ Active |
| 25 | **Tucano 12.17 Dotprod** | 3000.0 | **2980.1** | -19.9 | 13.0/30 | 43.3% | ⚔️ Active |
| 26 | **Eleanor 4.1** | 3000.0 | **2965.9** | -34.1 | 13.0/32 | 40.6% | ⚔️ Active |
| 27 | **Grail 2.0.1** | 3000.0 | **2936.7** | -63.3 | 12.0/32 | 37.5% | ⚔️ Active |
| 28 | **Bread 3.0.0 Dotprod** | 3000.0 | **2932.9** | -67.1 | 12.0/32 | 37.5% | ⚔️ Active |
| 29 | **Illumina 3 dev 85c Dotprod** | 3000.0 | **2907.4** | -92.6 | 12.0/34 | 35.3% | ⚔️ Active |
| 30 | **Lambergar 1.2** | 3000.0 | **2881.7** | -118.3 | 10.5/32 | 32.8% | ⚔️ Active |
| 31 | **Peacekeeper 0B** | 3000.0 | **2895.6** | -104.4 | 8.5/30 | 28.3% | ⚔️ Active |
| 32 | **Cataphract 1.3 Dotprod** | 3000.0 | **2868.4** | -131.6 | 8.5/32 | 26.6% | ⚔️ Active |
| 33 | **Spaghet 1.1.3** | 3000.0 | **2813.1** | -186.9 | 5.0/30 | 16.7% | ⚔️ Active |
| 34 | **Luna 2.1.0** | 3000.0 | **2707.4** | -292.6 | 0.0/32 | 0.0% | ⚔️ Active |

---

### 🛠️ Developer Logs
| Engine | Avg Length | Short Loss | Long Loss | Time Losses |
| :--- | :---: | :---: | :---: | :---: |
| **Hobbes 3.0** | 61.8 | N/A | N/A | 0 |
| **Renegade 1.3.1** | 57.0 | 63 | 100 | 0 |
| **Halogen 16.7.12** | 52.5 | 60 | 60 | 1 |
| **Icarus 1.1.1 dev** | 60.7 | 57 | 79 | 0 |
| **Coda 0.9.3 AI** | 58.3 | 59 | 73 | 0 |
| **Triumviratus 6.0 Dotprod** | 58.0 | 74 | 77 | 0 |
| **Minke 6.0.0 Dotprod** | 62.8 | 45 | 85 | 0 |
| **Tcheran 14.0 dev** | 59.8 | 70 | 92 | 0 |
| **Zangdar 7.0** | 57.2 | 32 | 84 | 4 |
| **Iris 2.0 dev** | 59.4 | 33 | 72 | 0 |
| **Rice dev 1169a58** | 61.4 | 45 | 91 | 0 |
| **Panda 2.0** | 62.5 | 47 | 90 | 0 |
| **Ruthorin 1.9.9** | 64.4 | 48 | 93 | 0 |
| **Sirius 9.0 Dotprod** | 56.3 | 48 | 85 | 0 |
| **Elixir 3.0** | 59.8 | 24 | 76 | 0 |
| **Carp 3.0.1** | 71.3 | 41 | 123 | 0 |
| **Weiss 2.1 dev e3bf1e5** | 55.4 | 37 | 67 | 0 |
| **Avalanche 3.1.0 dev** | 68.3 | 33 | 92 | 0 |
| **Igel 3.6.3 Dotprod** | 61.7 | 32 | 83 | 0 |
| **Zigqueen 5.8.3 AI** | 62.8 | 29 | 74 | 0 |
| **Prelude 2.1 dev** | 49.3 | 37 | 103 | 0 |
| **Lunar 0.4.0 dev** | 61.5 | 37 | 110 | 0 |
| **Ursus 1.0.0** | 58.8 | 37 | 59 | 0 |
| **Tarnished 6.0** | 64.5 | 20 | 126 | 0 |
| **Tucano 12.17 Dotprod** | 63.7 | 35 | 89 | 1 |
| **Eleanor 4.1** | 61.7 | 45 | 114 | 0 |
| **Grail 2.0.1** | 69.9 | 36 | 120 | 0 |
| **Bread 3.0.0 Dotprod** | 66.8 | 52 | 94 | 0 |
| **Illumina 3 dev 85c Dotprod** | 61.4 | 42 | 114 | 0 |
| **Lambergar 1.2** | 60.1 | 35 | 112 | 0 |
| **Peacekeeper 0B** | 43.9 | 11 | 92 | 16 |
| **Cataphract 1.3 Dotprod** | 67.6 | 24 | 74 | 0 |
| **Spaghet 1.1.3** | 46.8 | 24 | 109 | 5 |
| **Luna 2.1.0** | 33.4 | 19 | 75 | 0 |

---

### ⚔️ Head-to-Head Crosstable
| # | Engine | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Hobbes 3.0** | x | - | - | - | 1.5 | 1.5 | - | 1.5 | 1.5 | - | - | - | 2 | 1.5 | 1.5 | 1.5 | 2 | 1.5 | - | - | - | - | 2 | 1.5 | 2 | 1.5 | - | 1.5 | - | - | - | 2 | 2 | - |
| 2 | **Renegade 1.3.1** | - | x | - | - | - | - | 1.5 | - | - | 1 | 1 | 2 | 2 | 1.5 | - | - | - | - | 1.5 | 1.5 | 1.5 | 1.5 | - | - | - | - | - | - | 2 | 2 | 1.5 | - | 2 | 2 |
| 3 | **Halogen 16.7.12** | - | - | x | - | 1 | 1 | - | 1.5 | 1 | - | - | - | - | 1.5 | 2 | 1.5 | 1.5 | 2 | - | - | - | - | 1.5 | 1 | 2 | 1.5 | - | 1.5 | - | - | - | 2 | 2 | - |
| 4 | **Icarus 1.1.1 dev** | - | - | - | x | 0.5 | 1.5 | - | 1 | 2 | - | 1.5 | - | 1 | 1.5 | - | 1.5 | 0.5 | 1.5 | - | - | - | - | 1.5 | 1.5 | 1.5 | 1 | - | 1.5 | - | - | - | 2 | 2 | - |
| 5 | **Coda 0.9.3 AI** | 0.5 | - | 1 | 1.5 | x | - | - | - | 1.5 | - | - | - | - | - | 1 | 1.5 | 1.5 | 1.5 | 2 | 2 | - | - | 1.5 | - | 1 | 1.5 | 1.5 | 1.5 | - | - | - | 2 | - | - |
| 6 | **Triumviratus 6.0 Dotprod** | 0.5 | - | 1 | 0.5 | - | x | 1.5 | - | - | 1.5 | - | 2 | - | - | 1.5 | - | - | - | 1.5 | - | - | 2 | - | - | - | 2 | 1.5 | - | 2 | 2 | - | - | - | 2 |
| 7 | **Minke 6.0.0 Dotprod** | - | 0.5 | - | - | - | 0.5 | x | 0.5 | - | - | 1.5 | 1.5 | 1 | 1.5 | - | - | 1 | - | - | 1.5 | 1.5 | 1 | 2 | 1 | 1 | - | - | - | - | - | 2 | - | 2 | - |
| 8 | **Tcheran 14.0 dev** | 0.5 | - | 0.5 | 1 | - | - | 1.5 | x | - | 1.5 | - | 1.5 | - | - | 1.5 | - | - | - | 1.5 | - | - | 1 | - | - | - | - | 1.5 | - | 1.5 | 2 | 2 | - | - | 2 |
| 9 | **Zangdar 7.0** | 0.5 | - | 1 | 0 | 0.5 | - | - | - | x | 1 | - | - | - | - | 1 | 1.5 | - | - | 2 | - | - | 1 | - | - | - | 0.5 | 1 | 1.5 | 1.5 | 2 | - | 2 | - | 2 |
| 10 | **Iris 2.0 dev** | - | 1 | - | - | - | 0.5 | - | 0.5 | 1 | x | 0.5 | - | 1 | 1 | - | 1 | 1.5 | 1.5 | - | - | 1 | - | 0.5 | 1.5 | 1 | - | - | 1.5 | - | - | 1.5 | - | 1.5 | - |
| 11 | **Rice dev 1169a58** | - | 1 | - | 0.5 | - | - | 0.5 | - | - | 1.5 | x | 1 | 1 | 1 | - | - | - | - | 0.5 | 0.5 | 1.5 | 1.5 | - | - | - | - | - | - | 1.5 | 1.5 | 2 | - | - | 2 |
| 12 | **Panda 2.0** | - | 0 | - | - | - | 0 | 0.5 | 0.5 | - | - | 1 | x | 2 | 0.5 | - | - | - | - | - | 2 | 1.5 | 2 | - | 1.5 | 0 | - | - | - | - | - | 2 | - | 2 | 2 |
| 13 | **Ruthorin 1.9.9** | 0 | 0 | - | 1 | - | - | 1 | - | - | 1 | 1 | 0 | x | - | - | - | - | - | 1 | 1.5 | 2 | 1.5 | - | - | - | - | - | - | 1 | 1.5 | 1.5 | - | - | 2 |
| 14 | **Sirius 9.0 Dotprod** | 0.5 | 0.5 | 0.5 | 0.5 | - | - | 0.5 | - | - | 1 | 1 | 1.5 | - | x | - | - | - | - | 1.5 | - | 1 | 1.5 | - | - | - | - | - | - | 1 | 2 | 1 | - | - | 2 |
| 15 | **Elixir 3.0** | 0.5 | - | 0 | - | 1 | 0.5 | - | 0.5 | 1 | - | - | - | - | - | x | 2 | 1 | 1 | - | 1 | - | - | 1 | - | 1.5 | 1.5 | 1 | 1 | - | - | - | 1.5 | - | - |
| 16 | **Carp 3.0.1** | 0.5 | - | 0.5 | 0.5 | 0.5 | - | - | - | 0.5 | 1 | - | - | - | - | 0 | x | 1.5 | 1 | 1.5 | 0.5 | - | - | - | - | - | 1.5 | 1.5 | 1.5 | 1.5 | - | - | 1 | - | - |
| 17 | **Weiss 2.1 dev e3bf1e5** | 0 | - | 0.5 | 1.5 | 0.5 | - | 0 | - | - | 0.5 | - | - | - | - | 1 | 0.5 | x | - | 1 | - | - | 2 | - | - | - | 1 | 1.5 | - | 1 | 1 | - | 1 | - | 2 |
| 18 | **Avalanche 3.1.0 dev** | 0.5 | - | 0 | 0.5 | 0.5 | - | - | - | - | 0.5 | - | - | - | - | 1 | 1 | - | x | 1 | 1 | - | - | - | - | - | 1 | 1 | 1 | 1 | 1.5 | - | 1.5 | - | 2 |
| 19 | **Igel 3.6.3 Dotprod** | - | 0.5 | - | - | 0 | 0.5 | - | 0.5 | 0 | - | 1.5 | - | 1 | 0.5 | - | 0.5 | 1 | 1 | x | - | - | - | 1 | 1 | 1 | - | - | 1.5 | - | - | - | 1.5 | 2 | - |
| 20 | **Zigqueen 5.8.3 AI** | - | 0.5 | - | - | 0 | - | 0.5 | - | - | - | 1.5 | 0 | 0.5 | - | 1 | 1.5 | - | 1 | - | x | 1 | - | - | - | - | 1.5 | 1 | 1.5 | - | - | 1.5 | 1.5 | - | - |
| 21 | **Prelude 2.1 dev** | - | 0.5 | - | - | - | - | 0.5 | - | - | 1 | 0.5 | 0.5 | 0 | 1 | - | - | - | - | - | 1 | x | 0 | - | 1.5 | - | - | - | - | 1.5 | 1.5 | 1 | - | 2 | 2 |
| 22 | **Lunar 0.4.0 dev** | - | 0.5 | - | - | - | 0 | 1 | 1 | 1 | - | 0.5 | 0 | 0.5 | 0.5 | - | - | 0 | - | - | - | 2 | x | 1.5 | 1 | 1.5 | - | - | - | - | - | 1.5 | - | 2 | - |
| 23 | **Ursus 1.0.0** | 0 | - | 0.5 | 0.5 | 0.5 | - | 0 | - | - | 1.5 | - | - | - | - | 1 | - | - | - | 1 | - | - | 0.5 | x | - | - | 0.5 | 2 | - | 1.5 | 1.5 | - | 1.5 | - | 2 |
| 24 | **Tarnished 6.0** | 0.5 | - | 1 | 0.5 | - | - | 1 | - | - | 0.5 | - | 0.5 | - | - | - | - | - | - | 1 | - | 0.5 | 1 | - | x | - | - | 1.5 | - | 1 | 1.5 | 1 | - | - | 2 |
| 25 | **Tucano 12.17 Dotprod** | 0 | - | 0 | 0.5 | 1 | - | 1 | - | - | 1 | - | 2 | - | - | 0.5 | - | - | - | 1 | - | - | 0.5 | - | - | x | 1 | 1 | - | 1.5 | 0 | - | - | - | 2 |
| 26 | **Eleanor 4.1** | 0.5 | - | 0.5 | 1 | 0.5 | 0 | - | - | 1.5 | - | - | - | - | - | 0.5 | 0.5 | 1 | 1 | - | 0.5 | - | - | 1.5 | - | 1 | x | 1 | 0.5 | - | - | - | 1.5 | - | - |
| 27 | **Grail 2.0.1** | - | - | - | - | 0.5 | 0.5 | - | 0.5 | 1 | - | - | - | - | - | 1 | 0.5 | 0.5 | 1 | - | 1 | - | - | 0 | 0.5 | 1 | 1 | x | 0.5 | - | - | - | 1 | 1.5 | - |
| 28 | **Bread 3.0.0 Dotprod** | 0.5 | - | 0.5 | 0.5 | 0.5 | - | - | - | 0.5 | 0.5 | - | - | - | - | 1 | 0.5 | - | 1 | 0.5 | 0.5 | - | - | - | - | - | 1.5 | 1.5 | x | 0.5 | 1.5 | - | 0.5 | - | - |
| 29 | **Illumina 3 dev 85c Dotprod** | - | 0 | - | - | - | 0 | - | 0.5 | 0.5 | - | 0.5 | - | 1 | 1 | - | 0.5 | 1 | 1 | - | - | 0.5 | - | 0.5 | 1 | 0.5 | - | - | 1.5 | x | - | - | 1 | 1 | - |
| 30 | **Lambergar 1.2** | - | 0 | - | - | - | 0 | - | 0 | 0 | - | 0.5 | - | 0.5 | 0 | - | - | 1 | 0.5 | - | - | 0.5 | - | 0.5 | 0.5 | 2 | - | - | 0.5 | - | x | 2 | - | 2 | - |
| 31 | **Peacekeeper 0B** | - | 0.5 | - | - | - | - | 0 | 0 | - | 0.5 | 0 | 0 | 0.5 | 1 | - | - | - | - | - | 0.5 | 1 | 0.5 | - | 1 | - | - | - | - | - | 0 | x | - | 1 | 2 |
| 32 | **Cataphract 1.3 Dotprod** | 0 | - | 0 | 0 | 0 | - | - | - | 0 | - | - | - | - | - | 0.5 | 1 | 1 | 0.5 | 0.5 | 0.5 | - | - | 0.5 | - | - | 0.5 | 1 | 1.5 | 1 | - | - | x | - | - |
| 33 | **Spaghet 1.1.3** | 0 | 0 | 0 | 0 | - | - | 0 | - | - | 0.5 | - | 0 | - | - | - | - | - | - | 0 | - | 0 | 0 | - | - | - | - | 0.5 | - | 1 | 0 | 1 | - | x | 2 |
| 34 | **Luna 2.1.0** | - | 0 | - | - | - | 0 | - | 0 | 0 | - | 0 | 0 | 0 | 0 | - | - | 0 | 0 | - | - | 0 | - | 0 | 0 | 0 | - | - | - | - | - | 0 | - | 0 | x |

<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
