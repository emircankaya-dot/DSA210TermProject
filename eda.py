import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("world_cup_matches_ranked.csv")

os.makedirs("results", exist_ok=True)

print("===== BASIC INFO =====")
print("Number of matches:", len(df))
print("Years:", sorted(df["Year"].unique()))
print("Underdog win rate:", df["underdog_win"].mean())
print()


plt.figure()
sns.histplot(df["abs_ranking_gap"], bins=15)
plt.title("Distribution of Ranking Gap")
plt.xlabel("Ranking Gap")
plt.ylabel("Count")
plt.savefig("results/ranking_gap_distribution.png")
plt.close()


plt.figure()
sns.countplot(x=df["underdog_win"])
plt.title("Underdog Win Distribution")
plt.xlabel("Underdog Win (1 = Yes)")
plt.ylabel("Count")
plt.savefig("results/underdog_distribution.png")
plt.close()

plt.figure()
sns.boxplot(x=df["underdog_win"], y=df["abs_ranking_gap"])
plt.title("Ranking Gap vs Underdog Wins")
plt.savefig("results/boxplot.png")
plt.close()


stage_upsets = df.groupby("Stage")["underdog_win"].mean().sort_values()

plt.figure(figsize=(8,5))
stage_upsets.plot(kind="barh")
plt.title("Underdog Win Rate by Stage")
plt.xlabel("Rate")
plt.savefig("results/stage_upsets.png")
plt.close()

print("EDA tamamlandı. Grafikler 'results' klasörüne kaydedildi.")