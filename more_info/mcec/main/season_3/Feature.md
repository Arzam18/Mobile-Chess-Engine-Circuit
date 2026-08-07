​📊 Available Views, Rankings, and Statistics Reports
​The repository's automated scripts process raw PGNs to generate several detailed analytical views and tracking lists, organized across the project's output directories:
​1. Standings & Crosstables
​Standings: The core leaderboards for each stage and league (Gateway, Entry League, Leagues 4 through 1, Main, Semifinal, Final, and Survival). They display wins, losses, draws, points, and rank progression.
​Crosstables: Head-to-head matchup matrices for each league. They show exactly how many points each engine scored against every other specific opponent in its group.
​2. Rating & Ranking Lists
​Official Ratings Lists: Calculated performance ratings (using standard chess rating formulas like Elo) derived strictly from tournament outcomes within the circuit.
​Full Rating Lists: Comprehensive lists covering all active engines, providing insight into their numerical strength and progression over time.
​Global Ranking: The master leaderboard that aggregates overall performance across tiers, giving a bird's-eye view of who the absolute top-performing mobile chess engines are in the entire circuit.
​3. Engine & Version Tracking Lists
​Full Engine Lists: Complete inventories of all engines participating in the circuit, mapping out their history, stats, and longevity.
​All Version Lists: Managed by generate_stats_4.py, these specialized lists track how different iterations, updates, or builds of the same engine perform relative to one another over time.
​Full Engine Tracking Results: Managed by generate_stats_3.py, this view aggregates performance data comprehensively across all matches to ensure no engine's history is lost.
​4. Separate Lists & Independent Evaluations
​Independent Evaluations: Managed by generate_stats_2.py and housed in more_results/main/season_3/, these separate lists offer isolated performance evaluations and alternative metrics independent of the primary tournament standings.
​Segmented Output Folders: Results are cleanly separated into dedicated directories under more_results/ (e.g., all version lists/, full_engine_results_all_over/), allowing users to easily navigate between official tournament standings, multi-version breakdowns, and independent analytical reports.
