import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
resp = requests.get(URL)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, 'html.parser')

titles = [re.sub("^\d*[):]\s", "", item.getText()) for item in soup.findAll("h3", class_="title")]
# print(titles)
titles.reverse()
# print(titles)
with open("movies.txt", "w") as file:
    rank = 1
    for movie in titles:
        item = f"{str(rank)}) {movie}\n"
        file.write(item)
        print(item)
        rank += 1

