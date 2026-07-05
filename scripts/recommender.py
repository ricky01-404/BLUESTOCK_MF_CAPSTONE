from pathlib import Path
import pandas as pd

# ==========================================================
# Bluestock Mutual Fund Recommendation System
# ==========================================================

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "processed" / "clean_performance.csv"

# Check file exists
if not DATA_PATH.exists():
    print(f"\n❌ Dataset not found!")
    print(f"Expected location:\n{DATA_PATH}")
    exit()

# Load Dataset
funds = pd.read_csv(DATA_PATH)

print("=" * 60)
print("       BLUESTOCK MUTUAL FUND RECOMMENDER")
print("=" * 60)

# Show available risk grades
print("\nAvailable Risk Grades:")
print(sorted(funds["risk_grade"].dropna().unique()))

risk = input(
    "\nEnter Risk Appetite (Low / Moderate / High / Very High): "
).strip()

# Filter
recommendations = funds[
    funds["risk_grade"].str.lower() == risk.lower()
].copy()

if recommendations.empty:

    print("\n❌ No funds found for this risk level.")

else:

    recommendations = recommendations.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    top3 = recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "expense_ratio_pct",
            "morningstar_rating",
        ]
    ].head(3)

    print("\n")
    print("=" * 60)
    print(f"Top 3 Funds for '{risk.title()}' Risk")
    print("=" * 60)
    print(top3.to_string(index=False))

    # Save recommendations
    output_path = BASE_DIR / "reports" / "recommended_funds.csv"

    output_path.parent.mkdir(exist_ok=True)

    top3.to_csv(output_path, index=False)

    print("\n✅ Recommendation saved successfully!")
    print(f"📄 {output_path}")