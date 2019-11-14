# http://quotes.toscrape.com/
# Importing
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

# Looping through all the pages
while url:
    res = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_ = "text").get_text(),
            "author": quote.find(class_ = "author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn = soup.find(class_ = "next")
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep(1)

# Code for the game
quote = choice(all_quotes)
remaining_guesses = 4
guess = ""
print("Here's a quote: ")
print(quote["text"])
print(quote["author"])
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses} \n")
    if guess.lower() == quote["author"].lower():
        print("You got it right!")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date  = soup.find(class_ = "author-born-date").get_text()
        birth_place = soup.find(class_ = "author-born-location").get_text()
        print(f"Here's a Hint: Author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a Hint: Author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(f"Here's a Hint: Author's last name starts with: {last_initial}")
    else:
        print(f"Sorry, you ran out of guesses. The answer was {quote['author']}")