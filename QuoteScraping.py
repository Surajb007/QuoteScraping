# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup

res = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.select(".quote")
all_quotes = []
for quote in quotes:
    all_quotes.append({
        "text": quote.find(class_ = "text").get_text(),
        "author": quote.find(class_ = "author").get_text()
    })
