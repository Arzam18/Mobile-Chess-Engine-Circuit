# Mobile Chess Engine Circuit (MCEC) - User Manual

Welcome to the **Mobile Chess Engine Circuit (MCEC)** repository! This manual provides a complete guide to understanding the project's structure, tournament design, automated workflows, and directory layout.

---

## 📌 Project Overview
The **Mobile Chess Engine Circuit** is an automated tournament management and statistical tracking system designed for mobile and lightweight chess engines. It handles complex multi-tiered promotion and relegation circuits, processes Portable Game Notation (PGN) tournament files via Python scripts, and automatically updates leaderboards, standings, and crosstables using GitHub Actions.

---

## 🏗️ Structural Hierarchy & Circuit Design
MCEC operates on a **half-promote and half-relegate** dynamic across its structural tiers, divided into **3 main structural parts** and **2 boundary transition zones**:

### 1. The Three Structural Parts
* **The Foundation (Ranks 1–36):** The elite core of the circuit governed by strict 6-to-6 promotion and relegation rules across its internal leagues.
* **The Gateway (Ranks 37–48):** The entry point and testing ground where new contenders face off against established Gatekeepers.
* **The Fringe (Ranks 49–72):** The outer tier where engines fight to retain their standing and defend their ranks against falling challengers.

### 2. The Two Boundary Zones
* **Entry League:** The boundary transition zone sitting between the Gateway and the Foundation.
* **Survival Stage:** The boundary transition zone sitting between the Gateway and the Fringe.

---

## 🔄 Stage-by-Stage Tournament Flow

### Stage 1: The Gateway (Ranks 37–48)
* **Purpose:** The entry point where newcomers join and face established Gatekeepers (12 engines baseline + new contenders).
* **Mechanism:** All engines play each other. The **top half** promotes toward the Entry League, while the **bottom half** is relegated toward the Survival Stage.

### Stage 2: Entry League (Gateway ↔ Foundation Boundary)
* **Purpose:** Tests whether top performers from the Gateway deserve a permanent seat inside the elite Foundation.
* **Mechanism:** Mirrors the incoming count from the Gateway and calls up an equal number from the bottom of the Foundation (counting backward from rank 36). 
* **Outcome:** The top half promotes directly into the Foundation. The bottom half becomes the new Gatekeepers (ranks 37–48). Excess engines beyond 12 are automatically pushed down to the Survival Stage.

### Stages 3–7: The Foundation Internal Leagues (Ranks 1–36)
The Foundation utilizes a strict **6-promote / 6-relegate** format across 12-engine groups:
* **League 4 (Top 25–36):** 12 engines | 396 games. Top 6 promote to League 3; bottom 6 stay in League 4.
* **League 3 (Top 19–30):** 12 engines | 396 games. Top 6 promote to League 2; bottom 6 relegate to League 4.
* **League 2 (Top 13–24):** 12 engines | 396 games. Top 6 promote to League 1; bottom 6 relegate to League 3.
* **League 1 (Top 6–17):** 12 engines | 396 games. Top 6 promote to Main; bottom 6 relegate to League 2.
* **Main Stage (Top 1–12):** 12 engines | 528 games. Top 6 advance to Semifinals; bottom 6 relegate to League 1.

### Stages 8–9: Championship Phase
* **Semifinal (Stage 8):** Top 6 engines | 600 games.
* **Final (Stage 9):** Top 2 engines | 300 games (Head-to-head battle for the Season Crown between Rank 1 and Rank 2).

### Stage 10: The Survival Stage (Gateway ↔ Fringe Boundary)
* **Purpose:** Evaluates whether existing Fringe engines (Ranks 49–72) can defend their positions against falling challengers from the Gateway.
* **Mechanism:** Combines bottom dropouts from the Gateway, excess Gatekeeper overflow, and call-ups from the Fringe to cap the stage at 36 engines. The top 22 engines form the new Fringe, while all others are eliminated.

---

## 📂 Repository Structure & Data Flow

* **`seasons/`**: Contains raw tournament game records in `.pgn` format organized by season (e.g., `seasons/season_3/`). Uploading a PGN here triggers automated GitHub workflows.
* **`generate_stats.py`**: Core tournament statistics and standings generator for the main `README.md`.
* **`generate_stats_2.py`**: Independent evaluation statistics script targeting `Mobile-Chess-Engine-Circuit/more_results/main/season_3/`.
* **`generate_stats_3.py`**: Full engine tracking script targeting `Mobile-Chess-Engine-Circuit/more_results/full_engine_results_all_over/`.
* **`generate_stats_4.py`**: All version lists tracking script targeting `Mobile-Chess-Engine-Circuit/more_results/all version lists/`.
* **`.github/workflows/`**: Automated GitHub Actions workflows configured with concurrency control to ensure seamless updates and prevent push conflicts.
