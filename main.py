import requests
from bs4 import BeautifulSoup

user_input = input("What website would you like to scrape?\n")

data = requests.get(f"https://{user_input}")
formated = BeautifulSoup(data.text,"html.parser").prettify()

print(formated)