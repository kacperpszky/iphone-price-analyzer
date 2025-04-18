import pandas as pd
from bs4 import BeautifulSoup as bs
import requests, csv

def get_offers(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(url, headers=headers)   
    soup = bs(req.text, "html.parser")   
    offers = soup.find_all('div', class_="css-l9drzq")
    data = []

    for offer in offers:
        try:
            title = offer.find("h4").text  
            price = offer.find("p", class_="css-uj7mm0").text
            location = offer.find("p", class_="css-vbz67q").text
            condition = offer.find("span", class_="css-iudov9")["title"]
            print(f"Appending {title}, {price}, {location}, {condition}")
            data.append([title, price, location, condition])
        except Exception as e:
            continue  # możesz też dodać "print(e)" do debugowania


    with open(".\\data\\olx_iphones.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Location", "Condition"])
        writer.writerows(data)
        
    