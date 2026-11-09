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
| 1 | **Stockfish 20261017** | **3148** | +7 | -7 | 63.5% | -76.4 | 57.3% | 459 |
| 2 | **Reckless 20260909** | **3127** | +7 | -7 | 53.7% | -37.1 | 57.0% | 460 |
| 3 | **PlentyChess 8.0.0** | **3109** | +8 | -8 | 49.7% | -32.6 | 55.6% | 360 |
| 4 | **Pawnocchio 20261007** | **3040** | +6 | -6 | 54.3% | +51.2 | 54.1% | 760 |
| 5 | **Integral 20260929** | **3049** | +8 | -8 | 46.2% | +30.3 | 53.6% | 360 |
| 6 | **Cinder 20261010** | **3029** | +5 | -5 | 53.2% | +60.5 | 49.6% | 871 |
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
| 1 | **Stockfish 20261017** | **3148** | 7 | 7 | 459 | 63.5% | 3072 | 57.3% |
| 2 | **Renegade 1.3.1** | **3140** | 10 | 10 | 246 | 55.5% | 3095 | 45.9% |
| 3 | **PZChessBot 7.1** | **3138** | 9 | 9 | 290 | 48.3% | 3111 | 49.7% |
| 4 | **Quanticade 20260908** | **3128** | 15 | 15 | 110 | 54.5% | 3109 | 52.7% |
| 5 | **Reckless 20260909** | **3127** | 7 | 7 | 460 | 53.7% | 3090 | 57.0% |
| 6 | **Tcheran v14.0-dev de755e15** | **3125** | 8 | 8 | 356 | 58.0% | 3090 | 49.7% |
| 7 | **Zangdar 7.25** | **3123** | 8 | 8 | 356 | 52.1% | 3090 | 42.4% |
| 8 | **Icarus 1.1.1 dev 7a05c88** | **3119** | 8 | 8 | 356 | 54.4% | 3084 | 47.5% |
| 9 | **Igel 3.6.3 Dotprod** | **3110** | 15 | 15 | 116 | 59.5% | 2957 | 41.4% |
| 10 | **PlentyChess 8.0.0** | **3109** | 8 | 8 | 360 | 49.7% | 3077 | 55.6% |
| 11 | **Viridithas 20260921** | **3105** | 15 | 15 | 110 | 49.5% | 3083 | 48.2% |
| 12 | **Astra 20260623** | **3104** | 15 | 15 | 110 | 50.5% | 3109 | 53.6% |
| 13 | **Devre 7.0** | **3098** | 9 | 9 | 290 | 48.6% | 3109 | 48.3% |
| 14 | **Horsie 1.1.8** | **3096** | 15 | 15 | 110 | 40.9% | 3116 | 52.7% |
| 15 | **Cataphract 1.3 Dotprod** | **3095** | 15 | 15 | 116 | 53.9% | 2965 | 37.1% |
| 16 | **Alexandria 9.0.14** | **3085** | 15 | 15 | 110 | 48.2% | 3085 | 56.4% |
| 17 | **Velvet 9.0.0 dev7** | **3075** | 12 | 12 | 180 | 52.5% | 3074 | 46.1% |
| 18 | **Altair 7.2.1** | **3062** | 12 | 12 | 180 | 42.8% | 3078 | 47.8% |
| 19 | **Uralochka 3.42a** | **3058** | 12 | 12 | 180 | 51.7% | 3075 | 52.2% |
| 20 | **Halogen 16.7.12** | **3054** | 7 | 7 | 466 | 57.5% | 3088 | 48.1% |
| 21 | **Integral 20260929** | **3049** | 8 | 8 | 360 | 46.2% | 3080 | 53.6% |
| 22 | **Obsidian 16.15** | **3047** | 15 | 15 | 110 | 45.5% | 3058 | 60.0% |
| 23 | **Berserk 20260524** | **3046** | 15 | 15 | 110 | 45.5% | 3085 | 54.5% |
| 24 | **Pawnocchio 20261007** | **3040** | 6 | 6 | 760 | 54.3% | 3091 | 54.1% |
| 25 | **Coda 0.9.4-dev+61b5ff2** | **3038** | 7 | 7 | 576 | 60.5% | 3079 | 50.9% |
| 26 | **Hobbes 20260912** | **3037** | 7 | 7 | 576 | 61.5% | 3078 | 49.1% |
| 27 | **Clover 9.1** | **3036** | 15 | 15 | 110 | 41.8% | 3085 | 54.5% |
| 28 | **Akimbo** | **3035** | 12 | 12 | 180 | 44.4% | 3073 | 56.7% |
| 29 | **Titan 1.1.0** | **3035** | 12 | 12 | 180 | 50.8% | 3075 | 51.7% |
| 30 | **Caissa 2.0.5** | **3034** | 15 | 15 | 110 | 45.0% | 3060 | 55.5% |
| 31 | **ZigQueen 6.5.0** | **3032** | 23 | 23 | 50 | 65.0% | 2919 | 54.0% |
| 32 | **Spaghet 1.1.3** | **3030** | 15 | 15 | 116 | 38.8% | 2976 | 22.4% |
| 33 | **Cinder 20261010** | **3029** | 5 | 5 | 871 | 53.2% | 3090 | 49.6% |
| 34 | **Stormphrax 8.0.0** | **3028** | 11 | 11 | 220 | 47.7% | 3072 | 60.9% |
| 35 | **Patricia 5 Dotprod** | **3019** | 19 | 19 | 70 | 40.0% | 3046 | 42.9% |
| 36 | **Motor 0.9.0** | **3016** | 15 | 15 | 110 | 39.1% | 3115 | 52.7% |
| 37 | **Arasan 26.0** | **3010** | 19 | 19 | 70 | 42.9% | 3048 | 45.7% |
| 38 | **Starzix 6.1** | **3010** | 12 | 12 | 180 | 42.2% | 3079 | 48.9% |
| 39 | **RubiChess 20260917** | **3010** | 15 | 15 | 110 | 39.5% | 3093 | 59.1% |
| 40 | **Black Marlin 9.0 dev 131b860** | **3006** | 19 | 19 | 70 | 46.4% | 3043 | 44.3% |
| 41 | **Elixir 3.0** | **3002** | 14 | 14 | 136 | 48.9% | 3011 | 50.7% |
| 42 | **Texel 1.13a6** | **3001** | 15 | 15 | 120 | 47.1% | 2994 | 47.5% |
| 43 | **Koivisto 9.2** | **2999** | 15 | 15 | 110 | 36.4% | 3116 | 52.7% |
| 44 | **Eleanor 4.1** | **2995** | 14 | 14 | 136 | 48.2% | 3014 | 44.9% |
| 45 | **Avalanche 3.1.0 dev** | **2990** | 14 | 14 | 136 | 44.9% | 3025 | 51.5% |
| 46 | **Seer 2.8.0 dev 9d8b602** | **2988** | 19 | 19 | 70 | 49.3% | 3049 | 47.1% |
| 47 | **Sirius 9.0 Dotprod** | **2985** | 14 | 14 | 136 | 48.5% | 3031 | 44.1% |
| 48 | **Equisetum 1.30 Telmateria** | **2984** | 19 | 19 | 70 | 43.6% | 3041 | 44.3% |
| 49 | **Iris 2.0 dev** | **2983** | 14 | 14 | 136 | 47.1% | 3017 | 38.2% |
| 50 | **Triumviratus 6.0 Dotprod** | **2976** | 7 | 7 | 576 | 55.8% | 3085 | 49.8% |
| 51 | **Chess.cpp 4.1.0** | **2973** | 23 | 23 | 50 | 56.0% | 2922 | 48.0% |
| 52 | **Turbulence v4 0.0.8** | **2972** | 19 | 19 | 70 | 41.4% | 3050 | 54.3% |
| 53 | **Rice dev 1169a58** | **2961** | 12 | 12 | 186 | 45.7% | 3003 | 46.2% |
| 54 | **Carp 3.0.1** | **2951** | 12 | 12 | 186 | 48.1% | 2994 | 42.5% |
| 55 | **Bread 3.0.0 Dotprod** | **2943** | 15 | 15 | 116 | 48.3% | 2963 | 46.6% |
| 56 | **Winter 5.07a** | **2941** | 23 | 23 | 50 | 52.0% | 2915 | 28.0% |
| 57 | **Minke 6.0.0 Dotprod** | **2940** | 14 | 14 | 136 | 48.2% | 3027 | 40.4% |
| 58 | **Clarity 8.0.0** | **2940** | 15 | 15 | 110 | 29.1% | 3117 | 47.3% |
| 59 | **Willow 4.0** | **2933** | 23 | 23 | 50 | 52.0% | 2919 | 48.0% |
| 60 | **Illumina 3 dev 85c Dotprod** | **2932** | 15 | 15 | 116 | 43.1% | 2960 | 46.6% |
| 61 | **Tarnished 6.0** | **2930** | 15 | 15 | 116 | 48.7% | 2970 | 26.7% |
| 62 | **Prelude 20261214** | **2929** | 15 | 15 | 116 | 47.4% | 2978 | 46.6% |
| 63 | **Ursus 1.1.0** | **2923** | 15 | 15 | 116 | 45.7% | 2960 | 44.8% |
| 64 | **Ruthorin 1.9.9** | **2916** | 12 | 12 | 186 | 44.4% | 3001 | 39.2% |
| 65 | **Yukari 2025.11.1** | **2910** | 23 | 23 | 50 | 45.0% | 2919 | 54.0% |
| 66 | **Pawn 20260225** | **2906** | 23 | 23 | 50 | 45.0% | 2921 | 46.0% |
| 67 | **Peacekeeper 20250717** | **2903** | 15 | 15 | 116 | 32.3% | 2980 | 33.6% |
| 68 | **Zigqueen 5.8.3 AI** | **2902** | 14 | 14 | 136 | 39.3% | 3025 | 44.9% |
| 69 | **Tucano 12.17 Dotprod** | **2876** | 15 | 15 | 116 | 43.1% | 2958 | 32.8% |
| 70 | **Panda 2.0** | **2876** | 12 | 12 | 186 | 42.7% | 3004 | 39.2% |
| 71 | **Lambergar 1.5** | **2876** | 15 | 15 | 116 | 33.2% | 2968 | 37.1% |
| 72 | **Lunar 0.4.0 dev** | **2843** | 15 | 15 | 116 | 42.7% | 2965 | 44.0% |
| 73 | **Weiss 2.1 dev e3bf1e5** | **2837** | 15 | 15 | 116 | 42.7% | 2965 | 35.3% |
| 74 | **Luna 4.1.0** | **2750** | 15 | 15 | 116 | 13.4% | 2976 | 16.4% |
| 75 | **Grail 3.0.0** | **2549** | 15 | 15 | 116 | 20.3% | 2969 | 26.7% |

</details>

## 🏆 Active Stage: Fringe

> 📊 **Active Stage Summary:** **650** Total Games Played
> ⚪ **White Wins:** 302 (46.5%) | ⬛ **Black Wins:** 70 (10.8%) | 🤝 **Draws:** 278 (42.8%)

#### 🏆 Standings (TCEC Style)

| Rank | Engine | Games | Points | % | Wins [W/B] | Losses [W/B] | Draws [W/B] | SB | Elo |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **Cataphract 20260925** | 50 | **38.5** | 77.00% | 30 [22/8] | 3 [0/3] | 17 [3/14] | 910 | 3095 |
| 2 | **Igel 3.8.0** | 50 | **38** | 76.00% | 28 [21/7] | 2 [1/1] | 20 [3/17] | 903 | 3110 |
| 3 | **Spaghet 1.1.3** | 50 | **35** | 70.00% | 26 [21/5] | 6 [1/5] | 18 [3/15] | 829.5 | 3030 |
| 4 | **ZigQueen 6.5.0** | 50 | **32.5** | 65.00% | 19 [16/3] | 4 [0/4] | 27 [9/18] | 755 | 3032 |
| 5 | **Texel 1.13a6** | 50 | **30.5** | 61.00% | 18 [13/5] | 7 [0/7] | 25 [12/13] | 696 | 3001 |
| 6 | **Chess.cpp 4.1.0** | 50 | **28** | 56.00% | 16 [14/2] | 10 [0/10] | 24 [11/13] | 653.75 | 2973 |
| 7 | **Rice dev 1169a58** | 50 | **27.5** | 55.00% | 15 [12/3] | 10 [0/10] | 25 [13/12] | 631.75 | 2961 |
| 8 | **Bread 20261024** | 50 | **26.5** | 53.00% | 15 [12/3] | 12 [0/12] | 23 [13/10] | 611.5 | 2943 |
| 9 | **Carp 3.0.1** | 50 | **26.5** | 53.00% | 16 [14/2] | 13 [3/10] | 21 [8/13] | 587.5 | 2951 |
| 10 | **Tarnished 6.0** | 50 | **26** | 52.00% | 18 [17/1] | 16 [0/16] | 16 [8/8] | 612.5 | 2930 |
| 11 | **Winter 5.07a** | 50 | **26** | 52.00% | 19 [16/3] | 17 [2/15] | 14 [7/7] | 592 | 2941 |
| 12 | **Illumina 4.0** | 50 | **26** | 52.00% | 13 [10/3] | 11 [0/11] | 26 [15/11] | 576.25 | 2932 |
| 13 | **Willow 4.0** | 50 | **26** | 52.00% | 14 [13/1] | 12 [4/8] | 24 [8/16] | 573.5 | 2933 |
| 14 | **Ruthorin 1.9.9** | 50 | **25.5** | 51.00% | 14 [12/2] | 13 [2/11] | 23 [11/12] | 569.5 | 2916 |
| 15 | **Ursus 1.1.0** | 50 | **25** | 50.00% | 12 [10/2] | 12 [2/10] | 26 [13/13] | 570 | 2923 |
| 16 | **Prelude 20261214** | 50 | **25** | 50.00% | 11 [8/3] | 11 [1/10] | 28 [16/12] | 569.25 | 2929 |
| 17 | **Peacekeeper 20250717** | 50 | **24** | 48.00% | 12 [10/2] | 14 [2/12] | 24 [13/11] | 549 | 2903 |
| 18 | **Tucano 12.17 Dotprod** | 50 | **22.5** | 45.00% | 12 [11/1] | 17 [4/13] | 21 [10/11] | 515 | 2876 |
| 19 | **Yukari 2025.11.1** | 50 | **22.5** | 45.00% | 9 [8/1] | 14 [1/13] | 27 [16/11] | 514.5 | 2910 |
| 20 | **Pawn 20260225** | 50 | **22.5** | 45.00% | 11 [9/2] | 16 [1/15] | 23 [15/8] | 506.5 | 2906 |
| 21 | **Panda 2.0** | 50 | **21.5** | 43.00% | 11 [9/2] | 18 [4/14] | 21 [12/9] | 471.5 | 2876 |
| 22 | **Lambergar 1.5** | 50 | **20.5** | 41.00% | 8 [5/3] | 17 [4/13] | 25 [16/9] | 452.75 | 2876 |
| 23 | **Weiss 2.1 dev e3bf1e5** | 50 | **19.5** | 39.00% | 13 [10/3] | 24 [6/18] | 13 [9/4] | 414 | 2837 |
| 24 | **Lunar 20260611** | 50 | **19** | 38.00% | 6 [4/2] | 18 [2/16] | 26 [19/7] | 447.25 | 2843 |
| 25 | **Luna 4.1.0** | 50 | **15.5** | 31.00% | 6 [5/1] | 25 [5/20] | 19 [15/4] | 343 | 2750 |
| 26 | **Grail 3.0.0** | 50 | **0** | 0.00% | 0 [0/0] | 50 [25/25] | 0 [0/0] | 0 | 2549 |

<details><summary><b>📈 View Full Rating Lists / Full Engines (Elo Updates, Win % & Loss %)</b></summary>

| Global Rank | Engine | Start Elo | End Elo | Δ Elo | Points / Played | Win % | Loss % | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| #49 | **Cataphract 20260925** | 2925 | **3095** | `+171.0` | **38.5** / 50 | 60.0% | 6.0% | 🟢 Retained in Circuit |
| #50 | **Igel 3.8.0** | 2987 | **3110** | `+122.3` | **38.0** / 50 | 56.0% | 4.0% | 🟢 Retained in Circuit |
| #51 | **Spaghet 1.1.3** | 2739 | **3030** | `+291.1` | **35.0** / 50 | 52.0% | 12.0% | 🟢 Retained in Circuit |
| #52 | **ZigQueen 6.5.0** | 3000 | **3032** | `+32.4` | **32.5** / 50 | 38.0% | 8.0% | 🟢 Retained in Circuit |
| #53 | **Texel 1.13a6** | 2927 | **3001** | `+74.1` | **30.5** / 50 | 36.0% | 14.0% | 🟢 Retained in Circuit |
| #54 | **Chess.cpp 4.1.0** | 3000 | **2973** | `-27.5` | **28.0** / 50 | 32.0% | 20.0% | 🟢 Retained in Circuit |
| #55 | **Rice dev 1169a58** | 2910 | **2961** | `+50.9` | **27.5** / 50 | 30.0% | 20.0% | 🟢 Retained in Circuit |
| #56 | **Bread 20261024** | 2981 | **2943** | `-37.8` | **26.5** / 50 | 30.0% | 24.0% | 🟢 Retained in Circuit |
| #57 | **Carp 3.0.1** | 2941 | **2951** | `+10.5` | **26.5** / 50 | 32.0% | 26.0% | 🟢 Retained in Circuit |
| #58 | **Tarnished 6.0** | 2960 | **2930** | `-30.2` | **26.0** / 50 | 36.0% | 32.0% | 🟢 Retained in Circuit |
| #59 | **Winter 5.07a** | 3000 | **2941** | `-59.3` | **26.0** / 50 | 38.0% | 34.0% | 🟢 Retained in Circuit |
| #60 | **Illumina 4.0** | 2899 | **2932** | `+33.0` | **26.0** / 50 | 26.0% | 22.0% | 🟢 Retained in Circuit |
| #61 | **Willow 4.0** | 3000 | **2933** | `-66.8` | **26.0** / 50 | 28.0% | 24.0% | 🟢 Retained in Circuit |
| #62 | **Ruthorin 1.9.9** | 2918 | **2916** | `-2.6` | **25.5** / 50 | 28.0% | 26.0% | 🔴 Relegated to Crucible / Out |
| #63 | **Ursus 1.1.0** | 2958 | **2923** | `-34.4` | **25.0** / 50 | 24.0% | 24.0% | 🔴 Relegated to Crucible / Out |
| #64 | **Prelude 20261214** | 2985 | **2929** | `-55.9` | **25.0** / 50 | 22.0% | 22.0% | 🔴 Relegated to Crucible / Out |
| #65 | **Peacekeeper 20250717** | 2774 | **2903** | `+129.2` | **24.0** / 50 | 24.0% | 28.0% | 🔴 Relegated to Crucible / Out |
| #66 | **Tucano 12.17 Dotprod** | 2935 | **2876** | `-58.6` | **22.5** / 50 | 24.0% | 34.0% | 🔴 Relegated to Crucible / Out |
| #67 | **Yukari 2025.11.1** | 3000 | **2910** | `-89.9` | **22.5** / 50 | 18.0% | 28.0% | 🔴 Relegated to Crucible / Out |
| #68 | **Pawn 20260225** | 3000 | **2906** | `-93.8` | **22.5** / 50 | 22.0% | 32.0% | 🔴 Relegated to Crucible / Out |
| #69 | **Panda 2.0** | 2889 | **2876** | `-12.9` | **21.5** / 50 | 22.0% | 36.0% | 🔴 Relegated to Crucible / Out |
| #70 | **Lambergar 1.5** | 2811 | **2876** | `+65.6` | **20.5** / 50 | 16.0% | 34.0% | 🔴 Relegated to Crucible / Out |
| #71 | **Weiss 2.1 dev e3bf1e5** | 2955 | **2837** | `-118.5` | **19.5** / 50 | 26.0% | 48.0% | 🔴 Relegated to Crucible / Out |
| #72 | **Lunar 20260611** | 2989 | **2843** | `-145.9` | **19.0** / 50 | 12.0% | 36.0% | 🔴 Relegated to Crucible / Out |
| #73 | **Luna 4.1.0** | 2573 | **2750** | `+176.4` | **15.5** / 50 | 12.0% | 50.0% | 🔴 Relegated to Crucible / Out |
| #74 | **Grail 3.0.0** | 2871 | **2549** | `-322.6` | **0.0** / 50 | 0.0% | 100.0% | 🔴 Relegated to Crucible / Out |

</details>

<details><summary><b>🛠️ View Developer Performance Logs</b></summary>

| Engine | Stage Rank | Win % | Draw % | Avg Length | Short / Long Win | Short / Long Draw | Short / Long Loss | Short / Long Depth | Normal Depth | Short / Long Time | Normal Time | Short / Long kNPS | Normal kNPS | Time Losses | Crashes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cataphract 20260925** | #1 | 60.0% | 34.0% | 58.3 moves | 8 / 86 moves | 10 / 161 moves | 53 / 108 moves | 12 / 37 | 18.0 | 148ms / 8.6s | 1.6s | 262.0 / 879.4 | 380.8 | `0` | `0` |
| **Igel 3.8.0** | #2 | 56.0% | 40.0% | 60.4 moves | 8 / 99 moves | 38 / 141 moves | 44 / 67 moves | 1 / 33 | 8.7 | 0ms / 4.6s | 1.2s | 1.0 / 657.6 | 103.5 | `0` | `0` |
| **Spaghet 1.1.3** | #3 | 52.0% | 36.0% | 67.0 moves | 8 / 117 moves | 41 / 161 moves | 67 / 96 moves | 10 / 94 | 19.6 | 44ms / 9.2s | 1.5s | 191.4 / 3400.0 | 333.1 | `1` | `0` |
| **ZigQueen 6.5.0** | #4 | 38.0% | 54.0% | 64.7 moves | 8 / 150 moves | 9 / 161 moves | 43 / 53 moves | 1 / 64 | 20.2 | 2ms / 8.2s | 1.5s | 32.0 / 2500.0 | 195.3 | `0` | `0` |
| **Texel 1.13a6** | #5 | 36.0% | 50.0% | 71.1 moves | 8 / 87 moves | 39 / 161 moves | 49 / 156 moves | 2 / 100 | 16.6 | 0ms / 6.3s | 1.2s | 0.0 / 1300.0 | 436.6 | `0` | `0` |
| **Chess.cpp 4.1.0** | #6 | 32.0% | 48.0% | 67.6 moves | 8 / 112 moves | 35 / 161 moves | 47 / 84 moves | 11 / 64 | 20.3 | 1ms / 13.6s | 1.3s | 1.4 / 673.5 | 410.2 | `0` | `0` |
| **Rice dev 1169a58** | #7 | 30.0% | 50.0% | 57.9 moves | 8 / 85 moves | 37 / 127 moves | 42 / 136 moves | 9 / 63 | 18.2 | 10ms / 3.0s | 1.1s | 69.2 / 799.7 | 456.8 | `0` | `0` |
| **Bread 20261024** | #8 | 30.0% | 46.0% | 66.6 moves | 8 / 136 moves | 10 / 135 moves | 54 / 85 moves | 0 / 113 | 15.6 | 1ms / 3.0s | 1.3s | 0.0 / 831.8 | 170.1 | `0` | `0` |
| **Carp 3.0.1** | #9 | 32.0% | 42.0% | 74.6 moves | 8 / 109 moves | 34 / 161 moves | 45 / 150 moves | 10 / 127 | 17.8 | 1ms / 5.5s | 1.3s | 0.0 / 1000.0 | 402.8 | `0` | `0` |
| **Tarnished 6.0** | #10 | 36.0% | 32.0% | 60.5 moves | 8 / 156 moves | 43 / 161 moves | 20 / 66 moves | 1 / 62 | 15.2 | 0ms / 17.4s | 1.7s | 0.0 / 1900.0 | 126.1 | `0` | `1` |
| **Winter 5.07a** | #11 | 38.0% | 28.0% | 66.8 moves | 8 / 143 moves | 41 / 161 moves | 27 / 125 moves | 11 / 128 | 20.0 | 44ms / 3.2s | 1.4s | 105.7 / 1200.0 | 299.4 | `0` | `0` |
| **Illumina 4.0** | #12 | 26.0% | 52.0% | 80.8 moves | 8 / 117 moves | 21 / 161 moves | 44 / 117 moves | 10 / 33 | 20.6 | 4ms / 13.6s | 1.4s | 97.8 / 1900.0 | 539.2 | `1` | `0` |
| **Willow 4.0** | #13 | 28.0% | 48.0% | 66.5 moves | 8 / 124 moves | 28 / 161 moves | 44 / 83 moves | 9999 / 0 | N/A | N/A | N/A | N/A | N/A | `0` | `0` |
| **Ruthorin 1.9.9** | #14 | 28.0% | 46.0% | 66.1 moves | 8 / 89 moves | 21 / 161 moves | 36 / 86 moves | 4 / 128 | 17.5 | 13ms / 9.1s | 1.3s | 2.4 / 305.4 | 117.5 | `1` | `0` |
| **Ursus 1.1.0** | #15 | 24.0% | 52.0% | 62.7 moves | 8 / 81 moves | 9 / 161 moves | 47 / 82 moves | 1 / 128 | 19.8 | 0ms / 7.4s | 1.6s | 0.0 / 963.1 | 266.8 | `0` | `0` |
| **Prelude 20261214** | #16 | 22.0% | 56.0% | 72.6 moves | 8 / 85 moves | 39 / 161 moves | 39 / 143 moves | 12 / 255 | 18.4 | 17ms / 3.2s | 1.3s | 147.3 / 623.9 | 340.2 | `0` | `0` |
| **Peacekeeper 20250717** | #17 | 24.0% | 48.0% | 65.7 moves | 8 / 82 moves | 41 / 161 moves | 40 / 84 moves | 9 / 40 | 16.5 | 58ms / 6.2s | 1.6s | 164.0 / 564.6 | 243.7 | `0` | `0` |
| **Tucano 12.17 Dotprod** | #18 | 24.0% | 42.0% | 69.7 moves | 8 / 96 moves | 9 / 161 moves | 38 / 141 moves | 9 / 120 | 21.8 | 3ms / 6.4s | 1.6s | 258.8 / 6500.0 | 599.2 | `2` | `0` |
| **Yukari 2025.11.1** | #19 | 18.0% | 54.0% | 62.5 moves | 8 / 95 moves | 34 / 161 moves | 34 / 89 moves | 9999 / 0 | N/A | N/A | N/A | N/A | N/A | `1` | `0` |
| **Pawn 20260225** | #20 | 22.0% | 46.0% | 66.6 moves | 8 / 62 moves | 9 / 161 moves | 46 / 106 moves | 12 / 199 | 18.6 | 7ms / 3.9s | 1.3s | 139.6 / 719.3 | 237.8 | `0` | `0` |
| **Panda 2.0** | #21 | 22.0% | 42.0% | 67.4 moves | 8 / 141 moves | 9 / 161 moves | 41 / 119 moves | 12 / 63 | 19.8 | 5ms / 6.2s | 1.5s | 97.4 / 969.7 | 470.3 | `1` | `0` |
| **Lambergar 1.5** | #22 | 16.0% | 50.0% | 67.0 moves | 8 / 117 moves | 9 / 161 moves | 34 / 120 moves | 13 / 99 | 22.5 | 33ms / 6.4s | 1.3s | 53.1 / 2400.0 | 386.3 | `0` | `0` |
| **Weiss 2.1 dev e3bf1e5** | #23 | 26.0% | 26.0% | 60.7 moves | 8 / 67 moves | 25 / 161 moves | 31 / 91 moves | 13 / 100 | 22.8 | 0ms / 6.1s | 1.4s | 0.0 / 1300.0 | 682.4 | `0` | `0` |
| **Lunar 20260611** | #24 | 12.0% | 52.0% | 57.5 moves | 8 / 85 moves | 9 / 161 moves | 8 / 117 moves | 0 / 46 | 14.8 | 0ms / 12.7s | 844ms | 1.0 / 991.0 | 252.3 | `1` | `0` |
| **Luna 4.1.0** | #25 | 12.0% | 38.0% | 62.1 moves | 8 / 63 moves | 9 / 161 moves | 37 / 117 moves | 9 / 64 | 15.6 | 5ms / 2.3s | 1.1s | 46.8 / 540.8 | 281.8 | `0` | `0` |
| **Grail 3.0.0** | #26 | 0.0% | 0.0% | 8.5 moves | 9999 / 0 moves | 9999 / 0 moves | 8 / 9 moves | 9999 / 0 | N/A | N/A | N/A | N/A | N/A | `25` | `25` |

</details>

<details><summary><b>🔍 View Stage Crosstable</b></summary>

| Engine | **#1** | **#2** | **#3** | **#4** | **#5** | **#6** | **#7** | **#8** | **#9** | **#10** | **#11** | **#12** | **#13** | **#14** | **#15** | **#16** | **#17** | **#18** | **#19** | **#20** | **#21** | **#22** | **#23** | **#24** | **#25** | **#26** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **#1. Cataphract 20260925** | — | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#2. Igel 3.8.0** | <nobr>0 1</nobr><br>(0.0) | — | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#3. Spaghet 1.1.3** | <nobr>1 0</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#4. ZigQueen 6.5.0** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#5. Texel 1.13a6** | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#6. Chess.cpp 4.1.0** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#7. Rice dev 1169a58** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#8. Bread 20261024** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#9. Carp 3.0.1** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#10. Tarnished 6.0** | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | — | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#11. Winter 5.07a** | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | — | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#12. Illumina 4.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#13. Willow 4.0** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#14. Ruthorin 1.9.9** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#15. Ursus 1.1.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#16. Prelude 20261214** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#17. Peacekeeper 20250717** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#18. Tucano 12.17 Dotprod** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#19. Yukari 2025.11.1** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#20. Pawn 20260225** | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | — | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#21. Panda 2.0** | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>1 0</nobr><br>(0.0) | — | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#22. Lambergar 1.5** | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | — | <nobr>1 0</nobr><br>(0.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#23. Weiss 2.1 dev e3bf1e5** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | — | <nobr>1 ½</nobr><br>(+1.0) | <nobr>1 1</nobr><br>(+2.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#24. Lunar 20260611** | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>1 ½</nobr><br>(+1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>½ 1</nobr><br>(+1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | — | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 1</nobr><br>(+2.0) |
| **#25. Luna 4.1.0** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 1</nobr><br>(0.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>1 0</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>½ 0</nobr><br>(-1.0) | <nobr>½ ½</nobr><br>(0.0) | <nobr>0 ½</nobr><br>(-1.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>1 ½</nobr><br>(+1.0) | — | <nobr>1 1</nobr><br>(+2.0) |
| **#26. Grail 3.0.0** | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | <nobr>0 0</nobr><br>(-2.0) | — |

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
| **Semifinal** | Completed | 🔗 [View Stage Data](stages/semifinal.md) |
| **Final** | Completed | 🔗 [View Stage Data](stages/final.md) |

<!-- STATS_END -->

---

## 📥 Downloads & Official Releases
* Complete PGN game logs for each stage are stored in the [`/pgn`](./pgn) directory.
* Official stage-by-stage archives, standings, and game logs can also be accessed under the **Releases** tab.

## 📄 License
This project and its accompanying automation tools are open-sourced under the **GNU General Public License v3.0 (GPLv3)**.
