import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu, chi2_contingency


df = pd.read_csv("world_cup_matches_ranked.csv")

print("===== HYPOTHESIS TESTS =====\n")


print("Test 1: Ranking Gap vs Underdog Wins")

upset = df[df["underdog_win"] == 1]["abs_ranking_gap"]
normal = df[df["underdog_win"] == 0]["abs_ranking_gap"]

t_stat, p_value = ttest_ind(upset, normal, equal_var=False)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Result: Reject H0 (Significant difference)\n")
else:
    print("Result: Fail to reject H0\n")


print("Test 2: Mann-Whitney U Test")

u_stat, u_p = mannwhitneyu(upset, normal)

print(f"U-statistic: {u_stat}")
print(f"P-value: {u_p}")

if u_p < 0.05:
    print("Result: Significant difference\n")
else:
    print("Result: No significant difference\n")


print("Test 3: Chi-Square Test")

df["gap_category"] = pd.cut(
    df["abs_ranking_gap"],
    bins=[0, 10, 20, 50, 100, 300]
)

contingency = pd.crosstab(df["gap_category"], df["underdog_win"])

chi2, chi_p, _, _ = chi2_contingency(contingency)

print("Contingency Table:")
print(contingency)
print(f"Chi2: {chi2}")
print(f"P-value: {chi_p}")

if chi_p < 0.05:
    print("Result: Reject H0 (Dependent relationship)\n")
else:
    print("Result: Fail to reject H0\n")

print("===== DONE =====")