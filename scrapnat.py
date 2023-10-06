import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
article_elements = soup.find_all("article", class_="c-card")
for article in article_elements:
    title = article.find("h3", class_="c-card__title").text.strip()
    article_url = "https://www.nature.com" + article.find("a", class_="c-card__link u-link-inherit")["href"]
    print("Title:", title)
    print("URL:", article_url)
    print("------")
