# 📱 Mobile Chess Engine Circuit (MCEC)

Welcome to the official repository for the **Mobile Chess Engine Circuit (MCEC)**!

The MCEC is a dedicated hobbyist Android tournament circuit where world-class chess engines compete on practical, daily-use mobile hardware. The primary goal is to benchmark software efficiency, stability, and playing strength under strict hardware resource limits.

---



<!-- STATS_START -->
### 🏰 MCEC Season 3 Structure & Tournament Flow

MCEC Season 3 is strictly capped at **72 engines** and operates on a core **half-promote / half-relegate** dynamic, divided into **3 core parts and 2 boundary zones**:

#### 📌 Core Structure Parts
* **1–36 | The Foundation:** Multi-tier elite bracket featuring strict 6-to-6 promotion and relegation rules.
* **37–48 | The Gateway:** Entry gate where Gatekeepers and newcomers clash (top half promotes, bottom half relegates).
* **49–72 | The Fringe:** Lower-tier survival circuit where the top 22 retain their spots and others are fully kicked out.

#### 🔄 Boundary Zones & Flows
* **Entry League:** Bridge between Gateway and Foundation.
* **The Survival:** Bridge between Gateway and Fringe.

---

### 🌍 MCEC Season 3 Global Rankings

#### 🏆 The Foundation (1–36)

| Rank | Engine | Elo | + | - | Score | Avg Opp | Draws | Games |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Stockfish 20260930** | **3153** | +13 | -13 | 66.0% | -102.7 | 59.0% | 156 |
| 2 | **Reckless 20260909** | **3142** | +13 | -13 | 60.1% | -84.3 | 59.1% | 154 |
| 3 | **Cinder 20261010** | **3055** | +6 | -6 | 56.7% | +34.1 | 47.6% | 666 |
| 4 | **Pawnocchio 20261007** | **3065** | +7 | -7 | 57.4% | +27.2 | 54.3% | 556 |
| 5 | **PlentyChess 8.0.0** | **3074** | +13 | -13 | 50.3% | -8.8 | 60.4% | 154 |
| 6 | **Integral 20260929** | **3014** | +13 | -13 | 48.7% | +51.6 | 50.0% | 156 |
| 7 | **Hobbes 20260912** | **3037** | +7 | -7 | 61.5% | +40.5 | 49.1% | 576 |
| 8 | **Coda 0.9.4-dev+61b5ff2** | **3038** | +7 | -7 | 60.5% | +41.4 | 50.9% | 576 |
| 9 | **Obsidian 16.15** | **3047** | +15 | -15 | 45.5% | +11.0 | 60.0% | 110 |
| 10 | **Stormphrax 8.0.0** | **3028** | +11 | -11 | 47.7% | +44.2 | 60.9% | 220 |
| 11 | **Caissa 2.0.5** | **3034** | +15 | -15 | 45.0% | +25.6 | 55.5% | 110 |
| 12 | **Triumviratus 6.0 Dotprod** | **2976** | +7 | -7 | 55.8% | +108.3 | 49.8% | 576 |
| 13 | **Viridithas 20260921** | **3105** | +15 | -15 | 49.5% | -22.5 | 48.2% | 110 |
| 14 | **Halogen 16.7.12** | **3054** | +7 | -7 | 57.5% | +33.4 | 48.1% | 466 |
| 15 | **Alexandria 9.0.14** | **3085** | +15 | -15 | 48.2% | +0.2 | 56.4% | 110 |
| 16 | **Berserk 20260524** | **3046** | +15 | -15 | 45.5% | +39.1 | 54.5% | 110 |
| 17 | **Clover 9.1** | **3036** | +15 | -15 | 41.8% | +49.0 | 54.5% | 110 |
| 18 | **RubiChess 20260917** | **3010** | +15 | -15 | 39.5% | +83.6 | 59.1% | 110 |
| 19 | **Quanticade 20260908** | **3128** | +15 | -15 | 54.5% | -19.6 | 52.7% | 110 |
| 20 | **Astra 20260623** | **3104** | +15 | -15 | 50.5% | +5.1 | 53.6% | 110 |
| 21 | **Horsie 1.1.8** | **3096** | +15 | -15 | 40.9% | +20.0 | 52.7% | 110 |
| 22 | **Motor 0.9.0** | **3016** | +15 | -15 | 39.1% | +99.0 | 52.7% | 110 |
| 23 | **Koivisto 9.2** | **2999** | +15 | -15 | 36.4% | +116.4 | 52.7% | 110 |
| 24 | **Clarity 8.0.0** | **2940** | +15 | -15 | 29.1% | +177.1 | 47.3% | 110 |
| 25 | **Tcheran v14.0-dev de755e15** | **3125** | +8 | -8 | 58.0% | -34.5 | 49.7% | 356 |
| 26 | **Zangdar 7.25** | **3123** | +8 | -8 | 52.1% | -32.7 | 42.4% | 356 |
| 27 | **Icarus 1.1.1 dev 7a05c88** | **3119** | +8 | -8 | 54.4% | -35.7 | 47.5% | 356 |
| 28 | **Renegade 1.3.1** | **3140** | +10 | -10 | 55.5% | -45.3 | 45.9% | 246 |
| 29 | **PZChessBot 7.1** | **3138** | +9 | -9 | 48.3% | -27.5 | 49.7% | 290 |
| 30 | **Devre 7.0** | **3098** | +9 | -9 | 48.6% | +11.4 | 48.3% | 290 |
| 31 | **Uralochka 3.42a** | **3058** | +12 | -12 | 51.7% | +17.1 | 52.2% | 180 |
| 32 | **Titan 1.1.0** | **3035** | +12 | -12 | 50.8% | +40.2 | 51.7% | 180 |
| 33 | **Velvet 9.0.0 dev7** | **3075** | +12 | -12 | 52.5% | -0.5 | 46.1% | 180 |
| 34 | **Akimbo** | **3035** | +12 | -12 | 44.4% | +37.7 | 56.7% | 180 |
| 35 | **Altair 7.2.1** | **3062** | +12 | -12 | 42.8% | +16.0 | 47.8% | 180 |
| 36 | **Starzix 6.1** | **3010** | +12 | -12 | 42.2% | +69.5 | 48.9% | 180 |

#### 🚪 The Gateway (37–48)

| Rank | Engine | Elo | + | - | Score | Avg Opp | Draws | Games |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 37 | **Seer 2.8.0 dev 9d8b602** | **2988** | +19 | -19 | 49.3% | +60.9 | 47.1% | 70 |
| 38 | **Black Marlin 9.0 dev 131b860** | **3006** | +19 | -19 | 46.4% | +37.5 | 44.3% | 70 |
| 39 | **Equisetum 1.30 Telmateria** | **2984** | +19 | -19 | 43.6% | +57.4 | 44.3% | 70 |
| 40 | **Eleanor 4.1** | **2995** | +14 | -14 | 48.2% | +19.4 | 44.9% | 136 |
| 41 | **Sirius 9.0 Dotprod** | **2985** | +14 | -14 | 48.5% | +46.4 | 44.1% | 136 |
| 42 | **Arasan 26.0** | **3010** | +19 | -19 | 42.9% | +38.4 | 45.7% | 70 |
| 43 | **Turbulence v4 0.0.8** | **2972** | +19 | -19 | 41.4% | +78.7 | 54.3% | 70 |
| 44 | **Elixir 3.0** | **3002** | +14 | -14 | 48.9% | +8.8 | 50.7% | 136 |
| 45 | **Patricia 5 Dotprod** | **3019** | +19 | -19 | 40.0% | +27.6 | 42.9% | 70 |
| 46 | **Avalanche 3.1.0 dev** | **2990** | +14 | -14 | 44.9% | +35.4 | 51.5% | 136 |
| 47 | **Iris 2.0 dev** | **2983** | +14 | -14 | 47.1% | +34.5 | 38.2% | 136 |
| 48 | **Minke 6.0.0 Dotprod** | **2940** | +14 | -14 | 48.2% | +86.9 | 40.4% | 136 |

#### ⛺ The Fringe (49–72)

| Rank | Engine | Elo | + | - | Score | Avg Opp | Draws | Games |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 49 | *[TBD]* | - | - | - | - | - | - | - |
| 50 | *[TBD]* | - | - | - | - | - | - | - |
| 51 | *[TBD]* | - | - | - | - | - | - | - |
| 52 | *[TBD]* | - | - | - | - | - | - | - |
| 53 | *[TBD]* | - | - | - | - | - | - | - |
| 54 | *[TBD]* | - | - | - | - | - | - | - |
| 55 | *[TBD]* | - | - | - | - | - | - | - |
| 56 | *[TBD]* | - | - | - | - | - | - | - |
| 57 | *[TBD]* | - | - | - | - | - | - | - |
| 58 | *[TBD]* | - | - | - | - | - | - | - |
| 59 | *[TBD]* | - | - | - | - | - | - | - |
| 60 | *[TBD]* | - | - | - | - | - | - | - |
| 61 | *[TBD]* | - | - | - | - | - | - | - |
| 62 | *[TBD]* | - | - | - | - | - | - | - |
| 63 | *[TBD]* | - | - | - | - | - | - | - |
| 64 | *[TBD]* | - | - | - | - | - | - | - |
| 65 | *[TBD]* | - | - | - | - | - | - | - |
| 66 | *[TBD]* | - | - | - | - | - | - | - |
| 67 | *[TBD]* | - | - | - | - | - | - | - |
| 68 | *[TBD]* | - | - | - | - | - | - | - |
| 69 | *[TBD]* | - | - | - | - | - | - | - |
| 70 | *[TBD]* | - | - | - | - | - | - | - |
| 71 | *[TBD]* | - | - | - | - | - | - | - |
| 72 | *[TBD]* | - | - | - | - | - | - | - |

---

<details><summary><b>📊 View Official Computer Rating List (SPCC Style)</b></summary>

Ranking engines based on cumulative Elo performance, score percentages, average opponent strength, and draw rates across all stages.

| Rank | Engine | Rating | + | - | Games | Score % | Av. Op. | Draws % |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Stockfish 20260930** | **3153** | 13 | 13 | 156 | 66.0% | 3050 | 59.0% |
| 2 | **Reckless 20260909** | **3142** | 13 | 13 | 154 | 60.1% | 3057 | 59.1% |
| 3 | **Renegade 1.3.1** | **3140** | 10 | 10 | 246 | 55.5% | 3095 | 45.9% |
| 4 | **PZChessBot 7.1** | **3138** | 9 | 9 | 290 | 48.3% | 3111 | 49.7% |
| 5 | **Quanticade 20260908** | **3128** | 15 | 15 | 110 | 54.5% | 3109 | 52.7% |
| 6 | **Tcheran v14.0-dev de755e15** | **3125** | 8 | 8 | 356 | 58.0% | 3090 | 49.7% |
| 7 | **Zangdar 7.25** | **3123** | 8 | 8 | 356 | 52.1% | 3090 | 42.4% |
| 8 | **Icarus 1.1.1 dev 7a05c88** | **3119** | 8 | 8 | 356 | 54.4% | 3084 | 47.5% |
| 9 | **Viridithas 20260921** | **3105** | 15 | 15 | 110 | 49.5% | 3083 | 48.2% |
| 10 | **Astra 20260623** | **3104** | 15 | 15 | 110 | 50.5% | 3109 | 53.6% |
| 11 | **Devre 7.0** | **3098** | 9 | 9 | 290 | 48.6% | 3109 | 48.3% |
| 12 | **Horsie 1.1.8** | **3096** | 15 | 15 | 110 | 40.9% | 3116 | 52.7% |
| 13 | **Alexandria 9.0.14** | **3085** | 15 | 15 | 110 | 48.2% | 3085 | 56.4% |
| 14 | **Velvet 9.0.0 dev7** | **3075** | 12 | 12 | 180 | 52.5% | 3074 | 46.1% |
| 15 | **PlentyChess 8.0.0** | **3074** | 13 | 13 | 154 | 50.3% | 3065 | 60.4% |
| 16 | **Pawnocchio 20261007** | **3065** | 7 | 7 | 556 | 57.4% | 3093 | 54.3% |
| 17 | **Altair 7.2.1** | **3062** | 12 | 12 | 180 | 42.8% | 3078 | 47.8% |
| 18 | **Uralochka 3.42a** | **3058** | 12 | 12 | 180 | 51.7% | 3075 | 52.2% |
| 19 | **Cinder 20261010** | **3055** | 6 | 6 | 666 | 56.7% | 3089 | 47.6% |
| 20 | **Halogen 16.7.12** | **3054** | 7 | 7 | 466 | 57.5% | 3088 | 48.1% |
| 21 | **Obsidian 16.15** | **3047** | 15 | 15 | 110 | 45.5% | 3058 | 60.0% |
| 22 | **Berserk 20260524** | **3046** | 15 | 15 | 110 | 45.5% | 3085 | 54.5% |
| 23 | **Coda 0.9.4-dev+61b5ff2** | **3038** | 7 | 7 | 576 | 60.5% | 3079 | 50.9% |
| 24 | **Hobbes 20260912** | **3037** | 7 | 7 | 576 | 61.5% | 3078 | 49.1% |
| 25 | **Clover 9.1** | **3036** | 15 | 15 | 110 | 41.8% | 3085 | 54.5% |
| 26 | **Akimbo** | **3035** | 12 | 12 | 180 | 44.4% | 3073 | 56.7% |
| 27 | **Titan 1.1.0** | **3035** | 12 | 12 | 180 | 50.8% | 3075 | 51.7% |
| 28 | **Caissa 2.0.5** | **3034** | 15 | 15 | 110 | 45.0% | 3060 | 55.5% |
| 29 | **Stormphrax 8.0.0** | **3028** | 11 | 11 | 220 | 47.7% | 3072 | 60.9% |
| 30 | **Patricia 5 Dotprod** | **3019** | 19 | 19 | 70 | 40.0% | 3046 | 42.9% |
| 31 | **Motor 0.9.0** | **3016** | 15 | 15 | 110 | 39.1% | 3115 | 52.7% |
| 32 | **Integral 20260929** | **3014** | 13 | 13 | 156 | 48.7% | 3066 | 50.0% |
| 33 | **Arasan 26.0** | **3010** | 19 | 19 | 70 | 42.9% | 3048 | 45.7% |
| 34 | **Starzix 6.1** | **3010** | 12 | 12 | 180 | 42.2% | 3079 | 48.9% |
| 35 | **RubiChess 20260917** | **3010** | 15 | 15 | 110 | 39.5% | 3093 | 59.1% |
| 36 | **Black Marlin 9.0 dev 131b860** | **3006** | 19 | 19 | 70 | 46.4% | 3043 | 44.3% |
| 37 | **Elixir 3.0** | **3002** | 14 | 14 | 136 | 48.9% | 3011 | 50.7% |
| 38 | **Koivisto 9.2** | **2999** | 15 | 15 | 110 | 36.4% | 3116 | 52.7% |
| 39 | **Eleanor 4.1** | **2995** | 14 | 14 | 136 | 48.2% | 3014 | 44.9% |
| 40 | **Avalanche 3.1.0 dev** | **2990** | 14 | 14 | 136 | 44.9% | 3025 | 51.5% |
| 41 | **Lunar 0.4.0 dev** | **2989** | 20 | 20 | 66 | 46.2% | 3000 | 37.9% |
| 42 | **Seer 2.8.0 dev 9d8b602** | **2988** | 19 | 19 | 70 | 49.3% | 3049 | 47.1% |
| 43 | **Igel 3.6.3 Dotprod** | **2987** | 20 | 20 | 66 | 47.0% | 2974 | 42.4% |
| 44 | **Sirius 9.0 Dotprod** | **2985** | 14 | 14 | 136 | 48.5% | 3031 | 44.1% |
| 45 | **Prelude 2.1 dev** | **2985** | 20 | 20 | 66 | 45.5% | 3029 | 39.4% |
| 46 | **Equisetum 1.30 Telmateria** | **2984** | 19 | 19 | 70 | 43.6% | 3041 | 44.3% |
| 47 | **Iris 2.0 dev** | **2983** | 14 | 14 | 136 | 47.1% | 3017 | 38.2% |
| 48 | **Bread 3.0.0 Dotprod** | **2981** | 20 | 20 | 66 | 44.7% | 2998 | 47.0% |
| 49 | **Triumviratus 6.0 Dotprod** | **2976** | 7 | 7 | 576 | 55.8% | 3085 | 49.8% |
| 50 | **Turbulence v4 0.0.8** | **2972** | 19 | 19 | 70 | 41.4% | 3050 | 54.3% |
| 51 | **Tarnished 6.0** | **2960** | 20 | 20 | 66 | 46.2% | 3020 | 22.7% |
| 52 | **Ursus 1.0.0** | **2958** | 20 | 20 | 66 | 42.4% | 3006 | 39.4% |
| 53 | **Weiss 2.1 dev e3bf1e5** | **2955** | 20 | 20 | 66 | 45.5% | 3001 | 42.4% |
| 54 | **Carp 3.0.1** | **2941** | 14 | 14 | 136 | 46.3% | 3020 | 42.6% |
| 55 | **Minke 6.0.0 Dotprod** | **2940** | 14 | 14 | 136 | 48.2% | 3027 | 40.4% |
| 56 | **Clarity 8.0.0** | **2940** | 15 | 15 | 110 | 29.1% | 3117 | 47.3% |
| 57 | **Tucano 12.17 Dotprod** | **2935** | 20 | 20 | 66 | 41.7% | 3000 | 25.8% |
| 58 | **Texel 1.13a6** | **2927** | 19 | 19 | 70 | 37.1% | 3058 | 45.7% |
| 59 | **Cataphract 1.3 Dotprod** | **2925** | 20 | 20 | 66 | 36.4% | 2998 | 39.4% |
| 60 | **Ruthorin 1.9.9** | **2918** | 14 | 14 | 136 | 41.9% | 3033 | 36.8% |
| 61 | **Rice dev 1169a58** | **2910** | 14 | 14 | 136 | 42.3% | 3034 | 44.9% |
| 62 | **Zigqueen 5.8.3 AI** | **2902** | 14 | 14 | 136 | 39.3% | 3025 | 44.9% |
| 63 | **Illumina 3 dev 85c Dotprod** | **2899** | 20 | 20 | 66 | 36.4% | 2976 | 42.4% |
| 64 | **Panda 2.0** | **2889** | 14 | 14 | 136 | 42.6% | 3034 | 38.2% |
| 65 | **Grail 2.0.1** | **2871** | 20 | 20 | 66 | 35.6% | 2990 | 47.0% |
| 66 | **Lambergar 1.2** | **2811** | 20 | 20 | 66 | 27.3% | 2990 | 27.3% |
| 67 | **Peacekeeper 0B** | **2774** | 20 | 20 | 66 | 20.5% | 3023 | 22.7% |
| 68 | **Spaghet 1.1.3** | **2739** | 20 | 20 | 66 | 15.2% | 3019 | 12.1% |
| 69 | **Luna 2.1.0** | **2573** | 20 | 20 | 66 | 0.0% | 3003 | 0.0% |

</details>

## 🏆 Active Stage: Semifinal

> 📊 **Active Stage Summary:** **136** Total Games Played
> ⚪ **White Wins:** 56 (41.2%) | ⬛ **Black Wins:** 1 (0.7%) | 🤝 **Draws:** 79 (58.1%)

#### 🏆 Standings (TCEC Style)

| Rank | Engine | Games | Points | % | Wins [W/B] | Losses [W/B] | Draws [W/B] | SB | Elo |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Stockfish 260930** | 46 | **30** | 65.22% | 16 [16/0] | 2 [0/2] | 28 [7/21] | 629.5 | 3153 |
| 2 | **Reckless 20260909** | 44 | **25** | 56.82% | 12 [11/1] | 6 [0/6] | 26 [11/15] | 528 | 3142 |
| 3 | **Cinder 20261010** | 46 | **22.5** | 48.91% | 9 [9/0] | 10 [0/10] | 27 [14/13] | 494.5 | 3055 |
| 4 | **Pawnocchio 20261007** | 46 | **22** | 47.83% | 9 [9/0] | 11 [1/10] | 26 [13/13] | 486.5 | 3065 |
| 5 | **PlentyChess 8.0.0** | 44 | **19** | 43.18% | 6 [6/0] | 12 [0/12] | 26 [16/10] | 430.5 | 3074 |
| 6 | **Integral 20260929** | 46 | **17.5** | 38.04% | 5 [5/0] | 16 [0/16] | 25 [18/7] | 416.5 | 3014 |

<details><summary><b>📈 View Full Rating Lists / Full Engines (Elo Updates, Win % & Loss %)</b></summary>

| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win % | Loss % | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| #1 | **Stockfish 260930** | 3144 | **3153** | `+8.7` | **30.0** / 46 | 34.8% | 4.3% | 🟢 Advanced to Final |
| #2 | **Reckless 20260909** | 3121 | **3142** | `+20.5` | **25.0** / 44 | 27.3% | 13.6% | 🟢 Advanced to Final |
| #3 | **Cinder 20261010** | 2991 | **3055** | `+63.7` | **22.5** / 46 | 19.6% | 21.7% | 🔴 Retained in Main Pool |
| #4 | **Pawnocchio 20261007** | 3088 | **3065** | `-22.7` | **22.0** / 46 | 19.6% | 23.9% | 🔴 Retained in Main Pool |
| #5 | **PlentyChess 8.0.0** | 3071 | **3074** | `+3.4` | **19.0** / 44 | 13.6% | 27.3% | 🔴 Retained in Main Pool |
| #6 | **Integral 20260929** | 3088 | **3014** | `-73.7` | **17.5** / 46 | 10.9% | 34.8% | 🔴 Retained in Main Pool |

</details>

<details><summary><b>🛠️ View Developer Performance Logs</b></summary>

| Engine | Stage Rank | Win % | Draw % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Short / Long Depth | Normal Depth | Short / Long Time | Normal Time | Short / Long kNPS | Normal kNPS | Time Losses | Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Stockfish 260930** | #1 | 34.8% | 60.9% | 60.2 moves | 55 / 99 moves | 35 / 79 moves | 95 / 95 moves | 1 / 245 | 21.1 | 2ms / 13.7s | 1.6s | 18.5 / 2600.0 | 236.8 | `0` | `0` |
| **Reckless 20260909** | #2 | 27.3% | 59.1% | 63.3 moves | 54 / 96 moves | 33 / 81 moves | 62 / 89 moves | 7 / 83 | 17.6 | 90ms / 19.1s | 1.7s | 51.9 / 954.4 | 277.4 | `1` | `0` |
| **Cinder 20261010** | #3 | 19.6% | 58.7% | 62.5 moves | 51 / 95 moves | 41 / 89 moves | 55 / 99 moves | 0 / 54 | 17.1 | 0ms / 9.0s | 1.7s | 0.0 / 574.8 | 175.4 | `0` | `0` |
| **Pawnocchio 20261007** | #4 | 19.6% | 56.5% | 67.3 moves | 62 / 97 moves | 31 / 132 moves | 55 / 87 moves | 9 / 48 | 17.0 | 212ms / 19.1s | 1.7s | 57.3 / 1100.0 | 258.4 | `0` | `0` |
| **PlentyChess 8.0.0** | #5 | 13.6% | 59.1% | 67.3 moves | 60 / 89 moves | 41 / 132 moves | 54 / 94 moves | 12 / 249 | 19.1 | 3ms / 10.4s | 1.7s | 113.1 / 1500.0 | 217.5 | `0` | `0` |
| **Integral 20260929** | #6 | 10.9% | 54.3% | 62.3 moves | 55 / 95 moves | 31 / 85 moves | 51 / 96 moves | 10 / 100 | 18.7 | 5ms / 16.4s | 1.6s | 39.8 / 1800.0 | 205.6 | `0` | `0` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **#1** | **#2** | **#3** | **#4** | **#5** | **#6** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **#1. Stockfish 260930** | — | <nobr>1 ½ 1 ½ ½ ½ 1 ½</nobr><br>(+3.0) | <nobr>½ 1 ½ 1 0 ½ ½ 1 ½ 1</nobr><br>(+3.0) | <nobr>½ 1 ½ ½ ½ ½ ½ ½</nobr><br>(+1.0) | <nobr>1 ½ 1 ½ 1 ½ 1 ½ ½ ½</nobr><br>(+4.0) | <nobr>½ 1 ½ 1 ½ ½ ½ 1 0 1</nobr><br>(+3.0) |
| **#2. Reckless 20260909** | <nobr>0 ½ 0 ½ ½ ½ 0 ½</nobr><br>(-3.0) | — | <nobr>½ ½ 1 ½ ½ 0 1 ½</nobr><br>(+1.0) | <nobr>½ ½ 1 0 1 ½ ½ 1 1 ½</nobr><br>(+3.0) | <nobr>½ ½ ½ 1 ½ 1 ½ ½</nobr><br>(+2.0) | <nobr>½ 1 0 ½ ½ 1 ½ 1 ½ 1</nobr><br>(+3.0) |
| **#3. Cinder 20261010** | <nobr>½ 0 ½ 0 1 ½ ½ 0 ½ 0</nobr><br>(-3.0) | <nobr>½ ½ 0 ½ ½ 1 0 ½</nobr><br>(-1.0) | — | <nobr>½ 1 ½ ½ 0 1 ½ 1 0 ½</nobr><br>(+1.0) | <nobr>½ ½ ½ ½ 1 0 ½ ½</nobr><br>(0.0) | <nobr>½ ½ 1 ½ ½ ½ 1 0 1 ½</nobr><br>(+2.0) |
| **#4. Pawnocchio 20261007** | <nobr>½ 0 ½ ½ ½ ½ ½ ½</nobr><br>(-1.0) | <nobr>½ ½ 0 1 0 ½ ½ 0 0 ½</nobr><br>(-3.0) | <nobr>½ 0 ½ ½ 1 0 ½ 0 1 ½</nobr><br>(-1.0) | — | <nobr>1 ½ 1 0 1 ½ ½ ½ 1 0</nobr><br>(+2.0) | <nobr>½ 1 ½ 1 0 ½ ½ ½</nobr><br>(+1.0) |
| **#5. PlentyChess 8.0.0** | <nobr>0 ½ 0 ½ 0 ½ 0 ½ ½ ½</nobr><br>(-4.0) | <nobr>½ ½ ½ 0 ½ 0 ½ ½</nobr><br>(-2.0) | <nobr>½ ½ ½ ½ 0 1 ½ ½</nobr><br>(0.0) | <nobr>0 ½ 0 1 0 ½ ½ ½ 0 1</nobr><br>(-2.0) | — | <nobr>½ ½ 1 0 1 ½ 1 ½</nobr><br>(+2.0) |
| **#6. Integral 20260929** | <nobr>½ 0 ½ 0 ½ ½ ½ 0 1 0</nobr><br>(-3.0) | <nobr>½ 0 1 ½ ½ 0 ½ 0 ½ 0</nobr><br>(-3.0) | <nobr>½ ½ 0 ½ ½ ½ 0 1 0 ½</nobr><br>(-2.0) | <nobr>½ 0 ½ 0 1 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ ½ 0 1 0 ½ 0 ½</nobr><br>(-2.0) | — |

</details>


---

### 📦 Archived Stages & Pre-releases

| Stage Name | Status | Full Details File |
| :--- | :---: | :--- |
| **Gateway** | Completed | 🔗 [View Stage Data](stages/gateway.md) |
| **Entry League** | Completed | 🔗 [View Stage Data](stages/entry-league.md) |
| **League4** | Completed | 🔗 [View Stage Data](stages/league4.md) |
| **League 3** | Completed | 🔗 [View Stage Data](stages/league-3.md) |
| **League 2** | Completed | 🔗 [View Stage Data](stages/league-2.md) |
| **League 1** | Completed | 🔗 [View Stage Data](stages/league-1.md) |
| **Main League** | Completed | 🔗 [View Stage Data](stages/main-league.md) |

<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
