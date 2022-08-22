from bs4 import BeautifulSoup
import requests

resp = requests.get("https://news.ycombinator.com/news")
resp.raise_for_status()
yc_web_page = resp.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find("a", class_="titlelink")
# article_title = article_tag.getText()
# article_link = article_tag['href']
# article_score = article_tag.parent.parent.next_sibling.find("span", class_="score").getText()
# print(article_title)
# print(article_link)
# # print(article_tag.parent)
# print(article_score)

# assume that soup returns lists in same order
texts = []
links = []

articles = soup.find_all("a", class_="titlelink")
for item in articles:
    texts.append(item.getText())
    links.append(item['href']) 
    
upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

max_votes = max(upvotes)
max_index = upvotes.index(max_votes)
print(texts[max_index])
print(links[max_index])
print(max_votes)    


# with open("website.html") as site:
#     contents = site.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.find_all(name='a'))
# print(soup.title.string)
# # print(soup.prettify())
