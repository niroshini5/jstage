from bs4 import BeautifulSoup
import requests
import sys


def url_links(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'lxml')
    print(soup)

    for vol in soup.find_all("a",class_="bluelink-style vol-link"):
     vol_link=vol['href']
     print(vol)

    with open('jst.txt',"w")as fp:
        link=[]
        for issue in soup.find_all("a",class_="bluelink-style customTooltip"):
            issue_link=issue['href']
            link.append(issue_link)
            print(issue_link)
            if issue_link.startswith("https://www.jstage.jst.go.jp/article/jamdsm/"):
             fp.write(issue_link+"\n")

    with open('jst.txt',"a") as fp:
        for article_link in link:
            article_response=requests.get(article_link)
            article_soup=BeautifulSoup(article_response.content,"lxml")
            for artlink in article_soup.find_all("a",class_="bluelink-style customTooltip"):
                 article=artlink['href']

                 if article.startswith("https://www.jstage.jst.go.jp/article/jamdsm/"):
                        fp.write(article+"\n")

if  __name__ == '__main__':

    url = sys.argv[1]
    url_links(url)


    
    
    
