Mobile Chess Engine Circuit (MCEC) - Season 3 Structural Architecture & Tournament Flow
​This document outlines the complete structural hierarchy, promotion/relegation logic, and stage-by-stage tournament flow of the Mobile Chess Engine Circuit (MCEC).
​🏗️ Core Architecture & Principles
​MCEC operates on a half-promote and half-relegate dynamic across its structural tiers, divided into 3 main structural parts and 2 boundary transition zones:
​1. The Three Structural Parts
​The Foundation (Ranks 1–36): The elite core of the circuit governed by strict 6-to-6 promotion and relegation rules across its internal leagues.
​The Gateway (Ranks 37–48): The entry point and testing ground where new contenders face off against established Gatekeepers.
​The Fringe (Ranks 49–72): The outer tier where engines fight to retain their standing and defend their ranks against falling challengers.
​2. The Two Boundary Zones
​Entry League: The boundary transition zone sitting between the Gateway and the Foundation.
​Survival League: The boundary transition zone sitting between the Gateway and the Fringe.
​🔄 Stage-by-Stage Tournament Flow
​Stage 1: The Gateway (Ranks 37–48 / Gatekeepers & Newcomers)
​Participants: 12 established Gatekeepers combined with incoming new engines (variable count, e.g., expanding the pool past 12).
​Mechanism: All engines fight within the Gateway.
​Outcome:
​The top half promotes upward toward the Entry League.
​The bottom half is relegated downward toward Survival.
​Note on Disqualifications: If an engine is disqualified, adjustments are made to the count. For instance, if 18 engines are slated to promote, a disqualification reduces the passing pool to 17 engines moving up to the Entry League, leaving the remaining overflow to form the new Gatekeeper baseline and subsequent lower-tier drops.
​Stage 2: Entry League (Boundary: Gateway ↔ Foundation)
​Participants: Mirrors the incoming count from the Gateway (e.g., 17 engines) combined with an equal number called up from the bottom of the Foundation (ranks 36 counting backward, e.g., 17 engines), totaling 34 active engines.
​Purpose: Tests whether the top performers from the Gateway deserve a permanent seat inside the elite Foundation (Top 1–36).
​Outcome:
​Top Half: Promotes directly into the Foundation.
​Bottom Half: Becomes the new official Gatekeepers (occupying ranks 37–48).
​Overflow Management: Because the Gateway capacity is strictly capped at 12 engines, any excess engines beyond 12 from this pool (e.g., 5 excess engines out of 17) are automatically relegated down to The Survival Stage.
​Stages 3–7: The Foundation Internal Leagues (Ranks 1–36)
​The Foundation utilizes a strict 6-promote / 6-relegate format across 12-engine groups playing heavy double-round or multi-game circuits:
​League 4 (Top 25–36): 12 engines | 396 games. Top 6 promote to League 3; bottom 6 stay/defend in League 4.
​League 3 (Top 19–30): 12 engines | 396 games. Top 6 promote to League 2; bottom 6 relegate to League 4.
​League 2 (Top 13–24): 12 engines | 396 games. Top 6 promote to League 1; bottom 6 relegate to League 3.
​League 1 (Top 6–17): 12 engines | 396 games. Top 6 promote to Main; bottom 6 relegate to League 2.
​Main Stage (Top 1–12): 12 engines | 528 games. Top 6 advance to the Semifinals; bottom 6 relegate to League 1.
​Stages 8–9: Championship Phase
​Semifinal (Stage 8): Top 6 engines | 600 games.
​Final (Stage 9): Top 2 engines | 300 games (Head-to-head battle for the Season Crown between Rank 1 and Rank 2).
​Stage 10: The Survival Stage (Boundary: Gateway ↔ Fringe)
​Participants: Composed of the bottom-tier dropouts from the Gateway, the excess Gatekeeper overflow (e.g., 5 engines), and call-ups from the Fringe to cap the tournament stage strictly at 36 engines maximum.
​Purpose: Evaluates whether existing Fringe engines (Ranks 49–72) can successfully defend their positions against falling challengers.
​Outcome:
​The Top 22 engines of this survival battle secure their spots to form the New Fringe (Ranks 49–72).
​All remaining engines below the cutoff are eliminated ("kickout") from the active 1-72 circuit pool.
