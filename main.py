from scraping.scraper import get_offers


url = "https://www.olx.pl/oferty/q-iphone/?search%5Border%5D=created_at:desc"

if __name__ == "__main__":
    offers = get_offers(url)
    