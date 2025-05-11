import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


analyze_result = []

def clean_model_column(df):
    df["Model"] = df["Title"].str.extract(
        r"(iPhone\s?\d{1,2}(?:\s?(?:Pro Max|Pro|Plus|Mini|Max))?)",
        expand=False, flags=re.IGNORECASE
    )
    df["Model"] = df["Model"].str.title()
    df["Model"] = df["Model"].str.replace(r"\s+", " ", regex=True).str.strip()
    df["Model"] = df["Model"].str.replace("ProMax", "Pro Max", regex=False)
    df["Model"] = df["Model"].str.replace(r"(\d{2})Pro", r"\1 Pro", regex=True)
    return df


def analyze_csv(output="default", inputh_file="data/iphones_only.csv"):
    df = pd.read_csv(inputh_file)

    df["Model"] = df["Title"].str.extract(r"(iPhone\s?\d{1,2}(?:\s?(?:Pro|PRO|Pro Max|Plus|Mini|Max))?)", expand=False, flags=re.IGNORECASE)
    df["Model"] = (df["Model"]
    .str.lower()  
    .str.replace("iphone", "iPhone", regex=False)
    .str.replace("pro max", "Pro Max", regex=False)
    .str.replace("pro", "Pro", regex=False)
    .str.replace("plus", "Plus", regex=False)
    .str.replace("mini", "Mini", regex=False).str.title())
    
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    price_stats = df.groupby("Model")["Price"].agg(["count","mean", "min", "max", "median"]).round(2)

    return price_stats.reset_index().to_dict(orient="records")

def plot_model_trend(selected_region, history_file="data/history_ip.csv", min_offers=1):
    df = pd.read_csv(history_file)

    if selected_region:
        df = df[df["Region"].str.lower() == selected_region.lower()]

    if df.empty:
        print(f"Brak danych dla regionu: {selected_region}")
        return

    df = clean_model_column(df)

    model_counts = df["Model"].value_counts()
    popular_models = model_counts[model_counts > min_offers].index
    df = df[df["Model"].isin(popular_models)]

    df["ScrapeDate"] = pd.to_datetime(df["ScrapeDate"])
    trend_df = df.groupby(["ScrapeDate", "Model"]).size().unstack(fill_value=0)

    ax = trend_df.plot(figsize=(12, 6), marker='o')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xticks(rotation=45)

    plt.title(f"Popularność modeli iPhone w czasie – {selected_region}")
    plt.xlabel("Data")
    plt.ylabel("Liczba ogłoszeń")
    plt.legend(title="Model", loc="center left", bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def plot_price_trend(selected_region, history_file="data/history_ip.csv", min_offers=1):
    df = pd.read_csv(history_file)

    if selected_region:
        df = df[df["Region"].str.lower() == selected_region.lower()]

    if df.empty:
        print(f"Brak danych dla regionu: {selected_region}")
        return

    df = clean_model_column(df)

    model_counts = df["Model"].value_counts()
    popular_models = model_counts[model_counts > min_offers].index
    df = df[df["Model"].isin(popular_models)]

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["ScrapeDate"] = pd.to_datetime(df["ScrapeDate"])

    price_trend = df.groupby(["ScrapeDate", "Model"])["Price"].mean().unstack()

    ax = price_trend.plot(figsize=(12, 6), marker='o')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xticks(rotation=45)

    plt.title(f"Średnie ceny modeli iPhone w czasie – {selected_region}")
    plt.xlabel("Data")
    plt.ylabel("Cena [PLN]")
    plt.legend(title="Model", loc="center left", bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()
    plt.show()
