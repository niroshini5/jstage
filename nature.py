from bs4 import BeautifulSoup
import requests

def scrap_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    page_links = []
    with open('nature.txt','w') as file :
        num_list = []
        base_url ='https://www.nature.com/nri/articles?searchType=journalSearch&sort=PubDate&year=2023&page='

        for page_element in soup.find_all('a',attrs={'class':'c-pagination__link'}):
            href = page_element['href']
            split = href.split("page=")
            num_list.append(split[1])
        lastElement = num_list[-2]
        page_range = range(1,int(lastElement)+1)

        for page in page_range  :
            urls = base_url + str(page)
            print("urls", urls)
            file.write((urls+"\n"))
            page_links.append(urls)

        
    with open('natures.txt',"w") as fp:
        for art in page_links:
            article_response=requests.get(art)
            article_soup=BeautifulSoup(article_response.content,"lxml")
            for artlink in article_soup.find_all("a",class_="c-card__link u-link-inherit"):
                article=artlink['href']
                print(article)
                fp.write(("https://www.nature.com"+article)+"\n")



scrap_links('https://www.nature.com/nri/articles?year=2023')
