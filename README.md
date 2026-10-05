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
| 1 | *[TBD]* | - | - | - | - | - | - | - |
| 2 | *[TBD]* | - | - | - | - | - | - | - |
| 3 | *[TBD]* | - | - | - | - | - | - | - |
| 4 | *[TBD]* | - | - | - | - | - | - | - |
| 5 | *[TBD]* | - | - | - | - | - | - | - |
| 6 | *[TBD]* | - | - | - | - | - | - | - |
| 7 | **Obsidian 16.15** | **3016** | +24 | -24 | 47.7% | +38.1 | 54.5% | 44 |
| 8 | **Pawnocchio 2.0.1** | **3021** | +8 | -8 | 59.3% | +77.6 | 53.4% | 444 |
| 9 | **Hobbes 20260912** | **3062** | +7 | -7 | 63.1% | +18.8 | 48.2% | 510 |
| 10 | **Stormphrax 8.0.0** | **3033** | +13 | -13 | 48.1% | +45.9 | 58.4% | 154 |
| 11 | **Caissa 2.0.5** | **3001** | +24 | -24 | 42.0% | +61.9 | 47.7% | 44 |
| 12 | **Triumviratus 6.0 Dotprod** | **2992** | +7 | -7 | 58.0% | +95.3 | 49.4% | 510 |
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
| 1 | **Stockfish 20260930** | **3149** | 24 | 24 | 44 | 68.2% | 3048 | 50.0% |
| 2 | **Renegade 1.3.1** | **3140** | 10 | 10 | 246 | 55.5% | 3095 | 45.9% |
| 3 | **PZChessBot 7.1** | **3138** | 9 | 9 | 290 | 48.3% | 3111 | 49.7% |
| 4 | **Quanticade 20260908** | **3128** | 15 | 15 | 110 | 54.5% | 3109 | 52.7% |
| 5 | **Tcheran v14.0-dev de755e15** | **3125** | 8 | 8 | 356 | 58.0% | 3090 | 49.7% |
| 6 | **Zangdar 7.25** | **3123** | 8 | 8 | 356 | 52.1% | 3090 | 42.4% |
| 7 | **Icarus 1.1.1 dev 7a05c88** | **3119** | 8 | 8 | 356 | 54.4% | 3084 | 47.5% |
| 8 | **Reckless 20260909** | **3108** | 24 | 24 | 44 | 63.6% | 3051 | 54.5% |
| 9 | **Viridithas 20260921** | **3105** | 15 | 15 | 110 | 49.5% | 3083 | 48.2% |
| 10 | **Astra 20260623** | **3104** | 15 | 15 | 110 | 50.5% | 3109 | 53.6% |
| 11 | **Devre 7.0** | **3098** | 9 | 9 | 290 | 48.6% | 3109 | 48.3% |
| 12 | **Horsie 1.1.8** | **3096** | 15 | 15 | 110 | 40.9% | 3116 | 52.7% |
| 13 | **Alexandria 9.0.14** | **3085** | 15 | 15 | 110 | 48.2% | 3085 | 56.4% |
| 14 | **PlentyChess 8.0.0** | **3083** | 24 | 24 | 44 | 53.4% | 3057 | 56.8% |
| 15 | **Cinder 20261001** | **3078** | 7 | 7 | 554 | 58.8% | 3093 | 44.9% |
| 16 | **Velvet 9.0.0 dev7** | **3075** | 12 | 12 | 180 | 52.5% | 3074 | 46.1% |
| 17 | **Integral 20260929** | **3063** | 24 | 24 | 44 | 50.0% | 3053 | 50.0% |
| 18 | **Altair 7.2.1** | **3062** | 12 | 12 | 180 | 42.8% | 3078 | 47.8% |
| 19 | **Hobbes 20260912** | **3062** | 7 | 7 | 510 | 63.1% | 3080 | 48.2% |
| 20 | **Uralochka 3.42a** | **3058** | 12 | 12 | 180 | 51.7% | 3075 | 52.2% |
| 21 | **Coda 0.9.4-dev+61b5ff2** | **3057** | 7 | 7 | 510 | 62.5% | 3082 | 48.8% |
| 22 | **Halogen 16.7.12** | **3054** | 7 | 7 | 466 | 57.5% | 3088 | 48.1% |
| 23 | **Berserk 20260524** | **3046** | 15 | 15 | 110 | 45.5% | 3085 | 54.5% |
| 24 | **Clover 9.1** | **3036** | 15 | 15 | 110 | 41.8% | 3085 | 54.5% |
| 25 | **Akimbo** | **3035** | 12 | 12 | 180 | 44.4% | 3073 | 56.7% |
| 26 | **Titan 1.1.0** | **3035** | 12 | 12 | 180 | 50.8% | 3075 | 51.7% |
| 27 | **Stormphrax 8.0.0** | **3033** | 13 | 13 | 154 | 48.1% | 3078 | 58.4% |
| 28 | **Pawnocchio 2.0.1** | **3021** | 8 | 8 | 444 | 59.3% | 3099 | 53.4% |
| 29 | **Patricia 5 Dotprod** | **3019** | 19 | 19 | 70 | 40.0% | 3046 | 42.9% |
| 30 | **Obsidian 16.15** | **3016** | 24 | 24 | 44 | 47.7% | 3055 | 54.5% |
| 31 | **Motor 0.9.0** | **3016** | 15 | 15 | 110 | 39.1% | 3115 | 52.7% |
| 32 | **Arasan 26.0** | **3010** | 19 | 19 | 70 | 42.9% | 3048 | 45.7% |
| 33 | **Starzix 6.1** | **3010** | 12 | 12 | 180 | 42.2% | 3079 | 48.9% |
| 34 | **RubiChess 20260917** | **3010** | 15 | 15 | 110 | 39.5% | 3093 | 59.1% |
| 35 | **Black Marlin 9.0 dev 131b860** | **3006** | 19 | 19 | 70 | 46.4% | 3043 | 44.3% |
| 36 | **Elixir 3.0** | **3002** | 14 | 14 | 136 | 48.9% | 3011 | 50.7% |
| 37 | **Caissa 2.0.5** | **3001** | 24 | 24 | 44 | 42.0% | 3063 | 47.7% |
| 38 | **Koivisto 9.2** | **2999** | 15 | 15 | 110 | 36.4% | 3116 | 52.7% |
| 39 | **Eleanor 4.1** | **2995** | 14 | 14 | 136 | 48.2% | 3014 | 44.9% |
| 40 | **Triumviratus 6.0 Dotprod** | **2992** | 7 | 7 | 510 | 58.0% | 3088 | 49.4% |
| 41 | **Avalanche 3.1.0 dev** | **2990** | 14 | 14 | 136 | 44.9% | 3025 | 51.5% |
| 42 | **Lunar 0.4.0 dev** | **2989** | 20 | 20 | 66 | 46.2% | 3000 | 37.9% |
| 43 | **Seer 2.8.0 dev 9d8b602** | **2988** | 19 | 19 | 70 | 49.3% | 3049 | 47.1% |
| 44 | **Igel 3.6.3 Dotprod** | **2987** | 20 | 20 | 66 | 47.0% | 2974 | 42.4% |
| 45 | **Sirius 9.0 Dotprod** | **2985** | 14 | 14 | 136 | 48.5% | 3031 | 44.1% |
| 46 | **Prelude 2.1 dev** | **2985** | 20 | 20 | 66 | 45.5% | 3029 | 39.4% |
| 47 | **Equisetum 1.30 Telmateria** | **2984** | 19 | 19 | 70 | 43.6% | 3041 | 44.3% |
| 48 | **Iris 2.0 dev** | **2983** | 14 | 14 | 136 | 47.1% | 3017 | 38.2% |
| 49 | **Bread 3.0.0 Dotprod** | **2981** | 20 | 20 | 66 | 44.7% | 2998 | 47.0% |
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

## 🏆 Active Stage: Main League

> 📊 **Active Stage Summary:** **264** Total Games Played
> ⚪ **White Wins:** 119 (45.1%) | ⬛ **Black Wins:** 3 (1.1%) | 🤝 **Draws:** 142 (53.8%)

#### 🏆 Standings (TCEC Style)

| Rank | Engine | Games | Points | % | Wins [W/B] | Losses [W/B] | Draws [W/B] | SB | Elo |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Stockfish 20260930** | 44 | **30** | 68.18% | 19 [19/0] | 3 [0/3] | 22 [3/19] | 632 | 3149 |
| 2 | **Reckless 20260909** | 44 | **28** | 63.64% | 16 [16/0] | 4 [0/4] | 24 [6/18] | 590.75 | 3108 |
| 3 | **PlentyChess 8.0.0** | 44 | **23.5** | 53.41% | 11 [11/0] | 8 [1/7] | 25 [10/15] | 502 | 3083 |
| 4 | **Cinder 20261001** | 44 | **23** | 52.27% | 9 [9/0] | 7 [2/5] | 28 [11/17] | 491.75 | 3078 |
| 5 | **Integral 20260929** | 44 | **22** | 50.00% | 11 [9/2] | 11 [0/11] | 22 [13/9] | 467 | 3063 |
| 6 | **Coda 20260929** | 44 | **21.5** | 48.86% | 10 [10/0] | 11 [0/11] | 23 [12/11] | 456.75 | 3057 |
| 7 | **Obsidian 16.15** | 44 | **21** | 47.73% | 9 [9/0] | 11 [0/11] | 24 [13/11] | 452.5 | 3016 |
| 8 | **Pawnocchio 2.0.1** | 44 | **20** | 45.45% | 8 [7/1] | 12 [0/12] | 24 [15/9] | 439 | 3021 |
| 9 | **Hobbes 20260912** | 44 | **20** | 45.45% | 8 [8/0] | 12 [0/12] | 24 [14/10] | 430.75 | 3062 |
| 10 | **Stormphrax 8.0.0** | 44 | **19** | 43.18% | 9 [9/0] | 15 [0/15] | 20 [13/7] | 411.75 | 3033 |
| 11 | **Caissa 2.0.5** | 44 | **18.5** | 42.05% | 8 [8/0] | 15 [0/15] | 21 [14/7] | 399.25 | 3001 |
| 12 | **Triumviratus 20260930** | 44 | **17.5** | 39.77% | 4 [4/0] | 13 [0/13] | 27 [18/9] | 380.5 | 2992 |

<details><summary><b>📈 View Full Rating Lists / Full Engines (Elo Updates, Win % & Loss %)</b></summary>

| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win % | Loss % | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| #1 | **Stockfish 20260930** | 3000 | **3149** | `+148.8` | **30.0** / 44 | 43.2% | 6.8% | 🟢 Advanced to Semi-Final |
| #2 | **Reckless 20260909** | 3000 | **3108** | `+108.0` | **28.0** / 44 | 36.4% | 9.1% | 🟢 Advanced to Semi-Final |
| #3 | **PlentyChess 8.0.0** | 3000 | **3083** | `+82.9` | **23.5** / 44 | 25.0% | 18.2% | 🟢 Advanced to Semi-Final |
| #4 | **Cinder 20261001** | 3142 | **3078** | `-64.0` | **23.0** / 44 | 20.5% | 15.9% | 🟢 Advanced to Semi-Final |
| #5 | **Integral 20260929** | 3000 | **3063** | `+62.5` | **22.0** / 44 | 25.0% | 25.0% | 🟢 Advanced to Semi-Final |
| #6 | **Coda 20260929** | 3117 | **3057** | `-59.7` | **21.5** / 44 | 22.7% | 25.0% | 🟢 Advanced to Semi-Final |
| #7 | **Obsidian 16.15** | 3000 | **3016** | `+16.5` | **21.0** / 44 | 20.5% | 25.0% | 🔴 Relegated |
| #8 | **Pawnocchio 2.0.1** | 3087 | **3021** | `-65.8` | **20.0** / 44 | 18.2% | 27.3% | 🔴 Relegated |
| #9 | **Hobbes 20260912** | 3125 | **3062** | `-63.3` | **20.0** / 44 | 18.2% | 27.3% | 🔴 Relegated |
| #10 | **Stormphrax 8.0.0** | 3083 | **3033** | `-49.9` | **19.0** / 44 | 20.5% | 34.1% | 🔴 Relegated |
| #11 | **Caissa 2.0.5** | 3000 | **3001** | `+1.3` | **18.5** / 44 | 18.2% | 34.1% | 🔴 Relegated |
| #12 | **Triumviratus 20260930** | 3110 | **2992** | `-117.3` | **17.5** / 44 | 9.1% | 29.5% | 🔴 Relegated |

</details>

<details><summary><b>🛠️ View Developer Performance Logs</b></summary>

| Engine | Stage Rank | Win % | Draw % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Short / Long Depth | Normal Depth | Short / Long Time | Normal Time | Short / Long kNPS | Normal kNPS | Time Losses | Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Stockfish 20260930** | #1 | 43.2% | 50.0% | 57.3 moves | 42 / 85 moves | 32 / 74 moves | 54 / 73 moves | 1 / 245 | 21.8 | 1ms / 14.0s | 1.6s | 8.3 / 2500.0 | 213.8 | `0` | `0` |
| **Reckless 20260909** | #2 | 36.4% | 54.5% | 60.9 moves | 54 / 119 moves | 24 / 80 moves | 63 / 91 moves | 7 / 239 | 18.2 | 4ms / 23.9s | 1.7s | 35.7 / 1100.0 | 273.3 | `0` | `0` |
| **PlentyChess 8.0.0** | #3 | 25.0% | 56.8% | 63.2 moves | 44 / 134 moves | 41 / 120 moves | 36 / 78 moves | 11 / 56 | 18.7 | 322ms / 11.2s | 1.7s | 108.3 / 886.3 | 209.1 | `0` | `0` |
| **Cinder 20261001** | #4 | 20.5% | 63.6% | 60.0 moves | 36 / 78 moves | 33 / 100 moves | 62 / 73 moves | 0 / 73 | 16.8 | 0ms / 10.9s | 1.7s | 0.0 / 515.5 | 162.3 | `0` | `0` |
| **Integral 20260929** | #5 | 25.0% | 50.0% | 62.0 moves | 51 / 77 moves | 41 / 116 moves | 48 / 92 moves | 11 / 100 | 18.3 | 6ms / 15.4s | 1.5s | 28.6 / 1300.0 | 176.6 | `0` | `0` |
| **Coda 20260929** | #6 | 22.7% | 52.3% | 65.9 moves | 48 / 104 moves | 41 / 100 moves | 44 / 119 moves | 1 / 100 | 18.9 | 3ms / 5.1s | 1.3s | 18.4 / 671.1 | 183.4 | `0` | `0` |
| **Obsidian 16.15** | #7 | 20.5% | 54.5% | 67.6 moves | 55 / 119 moves | 24 / 104 moves | 64 / 119 moves | 10 / 123 | 18.1 | 1ms / 13.0s | 1.5s | 87.2 / 3100.0 | 254.6 | `0` | `0` |
| **Pawnocchio 2.0.1** | #8 | 18.2% | 54.5% | 62.3 moves | 68 / 110 moves | 40 / 120 moves | 37 / 83 moves | 9 / 152 | 17.1 | 199ms / 11.2s | 1.7s | 48.1 / 903.6 | 219.2 | `0` | `0` |
| **Hobbes 20260912** | #9 | 18.2% | 54.5% | 72.9 moves | 37 / 86 moves | 41 / 161 moves | 47 / 134 moves | 9 / 256 | 18.6 | 13ms / 12.7s | 1.7s | 61.0 / 1700.0 | 202.1 | `0` | `0` |
| **Stormphrax 8.0.0** | #10 | 20.5% | 45.5% | 65.1 moves | 51 / 92 moves | 24 / 91 moves | 55 / 119 moves | 8 / 248 | 18.5 | 3ms / 19.0s | 1.7s | 108.0 / 2100.0 | 219.0 | `0` | `0` |
| **Caissa 2.0.5** | #11 | 18.2% | 47.7% | 60.6 moves | 48 / 119 moves | 24 / 91 moves | 42 / 100 moves | 10 / 255 | 18.9 | 18ms / 9.5s | 1.7s | 172.8 / 1200.0 | 296.7 | `0` | `0` |
| **Triumviratus 20260930** | #12 | 9.1% | 61.4% | 64.2 moves | 55 / 81 moves | 31 / 161 moves | 51 / 103 moves | 1 / 64 | 17.2 | 1ms / 15.1s | 1.8s | 2.0 / 475.9 | 133.3 | `0` | `0` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **#1** | **#2** | **#3** | **#4** | **#5** | **#6** | **#7** | **#8** | **#9** | **#10** | **#11** | **#12** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **#1. Stockfish 20260930** | — | <nobr>0 1 0 1</nobr><br>(0.0) | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ ½ 1 ½</nobr><br>(+1.0) | <nobr>½ 1 0 1</nobr><br>(+1.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) |
| **#2. Reckless 20260909** | <nobr>1 0 1 0</nobr><br>(0.0) | — | <nobr>½ 1 0 ½</nobr><br>(0.0) | <nobr>½ ½ ½ ½</nobr><br>(0.0) | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) | <nobr>0 1 ½ 1</nobr><br>(+1.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ 1 ½ ½</nobr><br>(+1.0) | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) |
| **#3. PlentyChess 8.0.0** | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | <nobr>½ 0 1 ½</nobr><br>(0.0) | — | <nobr>1 ½ 1 0</nobr><br>(+1.0) | <nobr>½ 0 ½ 1</nobr><br>(0.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ ½ ½ ½</nobr><br>(0.0) | <nobr>0 1 ½ ½</nobr><br>(0.0) | <nobr>½ ½ 1 0</nobr><br>(0.0) | <nobr>1 ½ ½ 0</nobr><br>(0.0) | <nobr>½ ½ ½ 1</nobr><br>(+1.0) | <nobr>½ ½ ½ 1</nobr><br>(+1.0) |
| **#4. Cinder 20261001** | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ ½ ½ ½</nobr><br>(0.0) | <nobr>0 ½ 0 1</nobr><br>(-1.0) | — | <nobr>½ ½ 0 ½</nobr><br>(-1.0) | <nobr>1 0 ½ ½</nobr><br>(0.0) | <nobr>½ 1 0 1</nobr><br>(+1.0) | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ 1 ½ ½</nobr><br>(+1.0) | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>½ 1 ½ ½</nobr><br>(+1.0) | <nobr>½ ½ 1 ½</nobr><br>(+1.0) |
| **#5. Integral 20260929** | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | <nobr>½ 1 ½ 0</nobr><br>(0.0) | <nobr>½ ½ 1 ½</nobr><br>(+1.0) | — | <nobr>1 0 ½ ½</nobr><br>(0.0) | <nobr>½ ½ 1 0</nobr><br>(0.0) | <nobr>½ ½ ½ 1</nobr><br>(+1.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>0 1 0 1</nobr><br>(0.0) | <nobr>½ ½ ½ 0</nobr><br>(-1.0) | <nobr>1 0 1 ½</nobr><br>(+1.0) |
| **#6. Coda 20260929** | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>0 1 ½ ½</nobr><br>(0.0) | <nobr>0 1 ½ ½</nobr><br>(0.0) | — | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>½ ½ 0 1</nobr><br>(0.0) | <nobr>½ ½ 1 0</nobr><br>(0.0) | <nobr>½ 1 0 1</nobr><br>(+1.0) | <nobr>½ 0 1 ½</nobr><br>(0.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) |
| **#7. Obsidian 16.15** | <nobr>½ ½ 0 ½</nobr><br>(-1.0) | <nobr>1 0 ½ 0</nobr><br>(-1.0) | <nobr>½ ½ ½ ½</nobr><br>(0.0) | <nobr>½ 0 1 0</nobr><br>(-1.0) | <nobr>½ ½ 0 1</nobr><br>(0.0) | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | — | <nobr>1 ½ 1 ½</nobr><br>(+2.0) | <nobr>½ ½ ½ 0</nobr><br>(-1.0) | <nobr>1 0 ½ ½</nobr><br>(0.0) | <nobr>½ 1 ½ 1</nobr><br>(+2.0) | <nobr>½ ½ 1 0</nobr><br>(0.0) |
| **#8. Pawnocchio 2.0.1** | <nobr>½ 0 1 0</nobr><br>(-1.0) | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>1 0 ½ ½</nobr><br>(0.0) | <nobr>1 ½ ½ ½</nobr><br>(+1.0) | <nobr>½ ½ ½ 0</nobr><br>(-1.0) | <nobr>½ ½ 1 0</nobr><br>(0.0) | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | — | <nobr>½ 1 0 ½</nobr><br>(0.0) | <nobr>0 1 ½ ½</nobr><br>(0.0) | <nobr>1 ½ 1 0</nobr><br>(+1.0) | <nobr>½ ½ 0 ½</nobr><br>(-1.0) |
| **#9. Hobbes 20260912** | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>½ ½ 0 1</nobr><br>(0.0) | <nobr>½ 0 ½ ½</nobr><br>(-1.0) | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>½ ½ 0 1</nobr><br>(0.0) | <nobr>½ ½ ½ 1</nobr><br>(+1.0) | <nobr>½ 0 1 ½</nobr><br>(0.0) | — | <nobr>1 ½ ½ 0</nobr><br>(0.0) | <nobr>0 1 0 1</nobr><br>(0.0) | <nobr>½ ½ 1 ½</nobr><br>(+1.0) |
| **#10. Stormphrax 8.0.0** | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | <nobr>½ 0 ½ ½</nobr><br>(-1.0) | <nobr>0 ½ ½ 1</nobr><br>(0.0) | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | <nobr>1 0 1 0</nobr><br>(0.0) | <nobr>½ 0 1 0</nobr><br>(-1.0) | <nobr>0 1 ½ ½</nobr><br>(0.0) | <nobr>1 0 ½ ½</nobr><br>(0.0) | <nobr>0 ½ ½ 1</nobr><br>(0.0) | — | <nobr>½ 0 1 0</nobr><br>(-1.0) | <nobr>½ 1 ½ ½</nobr><br>(+1.0) |
| **#11. Caissa 2.0.5** | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>0 ½ 0 ½</nobr><br>(-2.0) | <nobr>½ ½ ½ 0</nobr><br>(-1.0) | <nobr>½ 0 ½ ½</nobr><br>(-1.0) | <nobr>½ ½ ½ 1</nobr><br>(+1.0) | <nobr>½ 1 0 ½</nobr><br>(0.0) | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>0 ½ 0 1</nobr><br>(-1.0) | <nobr>1 0 1 0</nobr><br>(0.0) | <nobr>½ 1 0 1</nobr><br>(+1.0) | — | <nobr>½ 0 1 ½</nobr><br>(0.0) |
| **#12. Triumviratus 20260930** | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>½ 0 ½ 0</nobr><br>(-2.0) | <nobr>½ ½ ½ 0</nobr><br>(-1.0) | <nobr>½ ½ 0 ½</nobr><br>(-1.0) | <nobr>0 1 0 ½</nobr><br>(-1.0) | <nobr>0 ½ ½ ½</nobr><br>(-1.0) | <nobr>½ ½ 0 1</nobr><br>(0.0) | <nobr>½ ½ 1 ½</nobr><br>(+1.0) | <nobr>½ ½ 0 ½</nobr><br>(-1.0) | <nobr>½ 0 ½ ½</nobr><br>(-1.0) | <nobr>½ 1 0 ½</nobr><br>(0.0) | — |

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

<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
