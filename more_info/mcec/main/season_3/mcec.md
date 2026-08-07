📱 The Mobile Chess Engine Circuit (MCEC) is a passion-driven, hobbyist Android tournament inspired by elite desktop events like TCEC and the Chess.com Computer Chess Championship (CCC).

​Born out of curiosity, MCEC explores a fascinating question: How do the world's strongest chess engines actually perform when constrained to a practical, daily-use mobile phone?

​Unlike massive desktop server setups that brute-force thousands of games overnight, MCEC games are run selectively during free time when the device is available. It is a real-world, practical exploration of software efficiency under strict resource limits.


​⏳ MCEC Circuit History

• ​Season 1 (Completed & Success): Established the core structural proof-of-concept for high-stakes mobile tournament ladders on everyday hardware. The format proved highly competitive and successfully ranked our original mobile engine pool.

• ​Season 2 (Halted / Stopped): Due to technical adjustments, real-world scheduling limitations, and the evolution of the mobile engine landscape, Season 2 was prematurely stopped to recalibrate the entire ecosystem.

• ​Season 3 (Now Beginning!): Rebuilt, optimized, and officially launching. Season 3 implements an expanded 72-engine baseline benchmark, strict stability filters, and a clean CCC-style tier framework to accommodate powerful newcomers.


​🎯 Tournament Goals & Focus

• ​The Low-End Gauntlet: To document how elite, world-class chess engines scale down and perform under limited mobile resources.

• ​Elite Threshold: Exclusively features the strongest open-source chess engines capable of reaching 3300+ Elo environments.

• ​The Stability Filter: MCEC is as much about compatibility, stability, and efficiency as it is about raw strength. Engines must handle mobile thermal conditions and OS constraints without crashing.

• ​Performance Tracking: Rather than calculating official Elo ratings (due to the practical limits of resource-constrained testing), MCEC focuses on head-to-head performance data, structural stability, and mobile win-probabilities.

🛠️ MCEC Technical Specifications, Settings & Adjudication

All games are strictly monitored and conducted under identical, controlled conditions. To ensure games run efficiently on mobile hardware without wasting battery on dead-drawn or completely decided positions, the tournament utilizes strict GUI Adjudication Rules:

Setting / RuleConfiguration / Value

Current Stage

Season 3 — Structural Benchmark Phase

Hardware:
Samsung A16 5G (Daily-use personal phone)

Time Control (TC):
1+1 (1 minute base + 1 second increment)

Processor Allocation1 Core / 1 Thread (To isolate single-core efficiency)

Graphical Interface:
ChessEnginesTournament

Opening Book:
UHO Stefan Pohl Book

Engine Settings:
Strict Defaults

Syzygy Tablebases:
Disabled (False)

Pondering:
Disabled (False)

Max Moves per Game:
160 moves

Moves to Start Rules:
40 moves

Fast Win Score:

20.00
Win Score (Greater than):
10.00

Plies to Win:
10 plies

Draw Score:
0.08

Plies to Draw:
10 plies

🤝 Special Acknowledgments
MCEC would not be possible without the incredible support and dedication of the computer chess community. Heartfelt thanks go to:

• The Engine Developers:
The brilliant minds behind the open-source codebases pushing the boundaries of chess science.

• Jim Ablett:
For his high-performance Android engine builds form the absolute backbone of this circuit.

• Archimedes:
For his highly-optimized Android engine compilations.

• Stefan Pohl:
For his outstanding UHO (Unbalanced Human Opening) Books, which provide the perfect, mathematically balanced testing ground to push these engines to their tactical limits.

📜 Our Mission
MCEC is ultimately a passion-project driven by curiosity, learning, and a profound appreciation for computer chess. It operates strictly as a casual, long-term testing sandbox run entirely in my spare time on independent, everyday consumer mobile hardware.
