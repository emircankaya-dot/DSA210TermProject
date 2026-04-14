import pandas as pd


def standardize_team_names(name: str) -> str:
    if pd.isna(name):
        return name

    name = str(name).strip()

    mapping = {
        "IR Iran": "Iran",
        "USA": "United States",
        "Korea Republic": "South Korea",
        "Korea DPR": "North Korea",
        "Cote d'Ivoire": "Ivory Coast",
        "Côte d'Ivoire": "Ivory Coast",
        "Republic of Ireland": "Ireland",
        "Germany FR": "Germany",
        "German DR": "Germany",
        "Soviet Union": "Russia",
        "Serbia and Montenegro": "Serbia",
        "Curacao": "Curaçao",
    }

    return mapping.get(name, name)


def load_world_cup_matches(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()

    required_cols = [
        "Year",
        "Datetime",
        "Stage",
        "Home Team Name",
        "Away Team Name",
        "Home Team Goals",
        "Away Team Goals",
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in WorldCupMatches.csv: {missing}")

    df = df[required_cols].copy()
    df["match_date"] = pd.to_datetime(df["Datetime"], errors="coerce")
    df = df.dropna(subset=["match_date"])

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)

    df = df[df["Year"] >= 1994].copy()

    df["Home Team Name"] = df["Home Team Name"].apply(standardize_team_names)
    df["Away Team Name"] = df["Away Team Name"].apply(standardize_team_names)

    df["Home Team Goals"] = pd.to_numeric(df["Home Team Goals"], errors="coerce")
    df["Away Team Goals"] = pd.to_numeric(df["Away Team Goals"], errors="coerce")
    df = df.dropna(subset=["Home Team Goals", "Away Team Goals"])

    return df


def load_fifa_rankings(path: str) -> pd.DataFrame:
    rank = pd.read_csv(path)
    rank.columns = [col.strip().lower() for col in rank.columns]

    date_candidates = ["rank_date", "ranking_date", "date"]
    team_candidates = ["country_full", "team", "country"]
    rank_candidates = ["rank", "team_rank"]

    date_col = next((c for c in date_candidates if c in rank.columns), None)
    team_col = next((c for c in team_candidates if c in rank.columns), None)
    rank_col = next((c for c in rank_candidates if c in rank.columns), None)

    if not date_col or not team_col or not rank_col:
        raise ValueError(f"Unexpected columns in fifa_ranking.csv: {list(rank.columns)}")

    rank = rank[[date_col, team_col, rank_col]].copy()
    rank.columns = ["rank_date", "team", "rank"]

    rank["rank_date"] = pd.to_datetime(rank["rank_date"], errors="coerce")
    rank["team"] = rank["team"].apply(standardize_team_names)
    rank["rank"] = pd.to_numeric(rank["rank"], errors="coerce")

    rank = rank.dropna(subset=["rank_date", "team", "rank"])
    rank = rank.sort_values(["team", "rank_date"]).reset_index(drop=True)

    return rank


def attach_rankings(matches: pd.DataFrame, rankings: pd.DataFrame, team_col: str, prefix: str) -> pd.DataFrame:
    temp = matches.sort_values("match_date").copy()
    team_rank = rankings.rename(columns={"team": team_col}).sort_values("rank_date")

    merged = pd.merge_asof(
        temp,
        team_rank,
        left_on="match_date",
        right_on="rank_date",
        by=team_col,
        direction="backward",
    )

    merged = merged.rename(columns={"rank": f"{prefix}_rank"})
    merged = merged.drop(columns=["rank_date"])

    return merged


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    def get_result(row):
        if row["Home Team Goals"] > row["Away Team Goals"]:
            return "Home Win"
        if row["Away Team Goals"] > row["Home Team Goals"]:
            return "Away Win"
        return "Draw"

    df["result"] = df.apply(get_result, axis=1)
    df["goal_diff"] = (df["Home Team Goals"] - df["Away Team Goals"]).abs()
    df["ranking_diff"] = df["away_rank"] - df["home_rank"]
    df["abs_ranking_gap"] = (df["home_rank"] - df["away_rank"]).abs()

    def underdog_win(row):
        if row["result"] == "Draw":
            return 0
        if row["home_rank"] < row["away_rank"] and row["result"] == "Away Win":
            return 1
        if row["away_rank"] < row["home_rank"] and row["result"] == "Home Win":
            return 1
        return 0

    df["underdog_win"] = df.apply(underdog_win, axis=1)

    return df


def build_dataset(
    matches_path: str = "WorldCupMatches.csv",
    rankings_path: str = "fifa_ranking.csv",
    output_path: str = "world_cup_matches_ranked.csv",
) -> pd.DataFrame:
    matches = load_world_cup_matches(matches_path)
    rankings = load_fifa_rankings(rankings_path)

    merged = attach_rankings(matches, rankings, "Home Team Name", "home")
    merged = attach_rankings(merged, rankings, "Away Team Name", "away")

    merged = merged.dropna(subset=["home_rank", "away_rank"]).copy()
    merged = add_features(merged)

    merged = merged[
        [
            "Year",
            "match_date",
            "Stage",
            "Home Team Name",
            "Away Team Name",
            "Home Team Goals",
            "Away Team Goals",
            "home_rank",
            "away_rank",
            "ranking_diff",
            "abs_ranking_gap",
            "goal_diff",
            "result",
            "underdog_win",
        ]
    ].sort_values("match_date").reset_index(drop=True)

    merged.to_csv(output_path, index=False)
    return merged


if __name__ == "__main__":
    df = build_dataset()
    print("Dataset created successfully.")
    print(f"Rows: {len(df)}")
    print(f"Years covered: {sorted(df['Year'].unique())}")
    print(f"Underdog wins: {df['underdog_win'].sum()}")