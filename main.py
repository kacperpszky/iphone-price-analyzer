from scraping.scraper import get_offers
from processing.cleaner import clean_iphone_data

url = "https://www.olx.pl/oferty/q-iphone/?search%5Border%5D=created_at:desc"

# dodac mozliwosc edycji url z requestem aby przyjmowac jedynie rekordy z danej lokalizacji np. sam Gdansk/Gdynia itd i dawac analize jako pomorskie
# zrobic zajebiste GUI najlepiej w czyms praktycznym, moze byc PyQt / streamlit
# export analizy/wykresu na pewno musi sie tu znalezc, wiec dodac w przyszlosci
# co do analizy dodac trend ip, jakie kiedy byly najbardziej popularne itd.....

if __name__ == "__main__":
    offers = get_offers(url)
    clean_iphone_data()