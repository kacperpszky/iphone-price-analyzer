import pandas as pd
import os
from datetime import datetime

def clean_iphone_data(region, input_path="data/olx_iphones.csv", output_path="data/iphones_only.csv", history_path="data/history_ip.csv"):
    df = pd.read_csv(input_path)
    
    iphone_mask = df["Title"].str.lower().str.contains("iphone")
    df = df[iphone_mask]

    trash_words = [
        "etui", "szkło","hartowane", "ładowarka", "powerbank", "case", "podstawka", "osłona", "hub", "kabel",
        "stacja", "Glass", "interfejs", "Obudowa", "magnetyczny", "baseus", "rower", "wyświetlacz", "bateria"
    ]
    for word in trash_words:
        df = df[~df["Title"].str.lower().str.contains(word)]

    df = df[~df["Price"].str.contains("Zamienię", case=False, na=False)]
    df = df[~df["Price"].str.contains("negocjacji", case=False, na=False)]
    df = df[~df["Title"].str.lower().str.contains("samsung|redmi|huawei|anker", na=False)]
    
    df["Price"] = df["Price"].str.replace("zł", "", regex=False)
    df["Price"] = df["Price"].str.replace(" ", "").str.replace(",", ".")
    df["Location"] = df["Location"].str.split(",").str[0]
    df["Location"] = df["Location"].str.split("-").str[0]
    
    print(f"Cleaned offers in .csv")
    df.to_csv(output_path, index=False)
    
    df["ScrapeDate"] = datetime.today().strftime("%Y-%m-%d")
    df["Region"] = region.lower()
    if os.path.exists(history_path):
        old_df = pd.read_csv(history_path)
        combined = pd.concat([old_df, df], ignore_index=True)
        combined.drop_duplicates(subset=["Title", "Price", "Location"], inplace=True)
        combined.to_csv(history_path, index=False)
    else:
        df.to_csv(history_path, index=False)

    print("Cleaned offers saved. Historical data updated.")