import pandas as pd
import re

analyze_result = []

def analyze_csv(inputh_file="data/iphones_only.csv"):
    df = pd.read_csv(inputh_file)

    df["Model"] = df["Title"].str.extract(r"(iPhone\s?\d{1,2}(?:\s?(?:Pro|Pro Max|Plus|Mini|Max))?)", expand=False, flags=re.IGNORECASE)
    price_stats = df.groupby("Model")["Price"].agg(["count", "mean", "min", "max", "median"]).sort_values(by="mean", ascending=False)
    price_stats = price_stats.round(2)
    analyze_result.append(price_stats)

    return(analyze_result)
