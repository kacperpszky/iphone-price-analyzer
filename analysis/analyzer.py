import pandas as pd
import re

analyze_result = []

def analyze_csv(output="default", inputh_file="data/iphones_only.csv"):
    df = pd.read_csv(inputh_file)

    df["Model"] = df["Title"].str.extract(r"(iPhone\s?\d{1,2}(?:\s?(?:Pro|PRO|Pro Max|Plus|Mini|Max))?)", expand=False, flags=re.IGNORECASE)
    df["Model"] = (
    df["Model"]
    .str.lower()  
    .str.replace("iphone", "iPhone", regex=False)
    .str.replace("pro max", "Pro Max", regex=False)
    .str.replace("pro", "Pro", regex=False)
    .str.replace("plus", "Plus", regex=False)
    .str.replace("mini", "Mini", regex=False)
    .str.title()  
    )
    
    
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    price_stats = df.groupby("Model")["Price"].agg(["count","mean", "min", "max", "median"]).round(2)

    return price_stats.reset_index().to_dict(orient="records")