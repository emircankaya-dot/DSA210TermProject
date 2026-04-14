
This project investigates whether underdog victories in FIFA World Cup matches can be explained using FIFA rankings and match-level statistics. The analysis focuses on World Cup tournaments from 1994 to 2022, where historical FIFA rankings are available.

Can underdog victories in FIFA World Cup matches be explained or predicted using FIFA rankings?

The project uses two datasets:

- **WorldCupMatches.csv**
  - Match-level data including teams, goals, and tournament stages

- **fifa_ranking.csv**
  - Historical FIFA rankings
  - Rankings are matched to each match based on the closest date before the game

The script `data_collection.py`:
- Cleans and processes match data
- Matches each team with its FIFA ranking before the match
- Creates the final dataset: `world_cup_matches_ranked.csv`

The final dataset includes:

- `home_rank`
- `away_rank`
- `ranking_diff`
- `abs_ranking_gap`
- `goal_diff`
- `result`
- `underdog_win`

An **underdog win** is defined as a match where the lower-ranked team defeats the higher-ranked team.

EDA is performed in `eda.py` and includes:

- Distribution of ranking gaps
- Distribution of underdog wins
- Boxplot comparing ranking gaps for upset vs non-upset matches
- Underdog win rates across tournament stages

All visualizations are saved in the `results/` folder.

Hypothesis testing is conducted in `hypothesis.py`.

- **H0:** There is no significant difference in ranking gaps between upset and non-upset matches  
- **H1:** There is a significant difference  

- Independent two-sample t-test  
- Mann-Whitney U test  
- Chi-square test  

These tests evaluate whether ranking differences influence the likelihood of underdog victories.

## How to Run

Run the scripts in the following order:

```bash
python data_collection.py
python eda.py
python hypothesis.py