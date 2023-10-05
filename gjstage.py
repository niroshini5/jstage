import gzip
import requests
from bs4 import BeautifulSoup
import io
import os
import sys


def gzip_collection():
    url_path = "/home/niroshini/Documents/jstage/sample.txt"
    target_path = "out/html/jstage/"
    agent = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"}
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    with open(url_path,'r') as f:
       urls = f.read().splitlines()
    for url in urls:
        url_get3 = requests.get(url, headers=agent, timeout=120)
        name_url = url_get3.url
        print(name_url)
        name = name_url.replace('/', '-')
        url3 = url_get3.text

        soup3 = BeautifulSoup(url3, 'lxml')
        outfilename = target_path + "{}.html.gz".format(name)

        with gzip.open(outfilename, 'wb') as output:

            with io.TextIOWrapper(output, encoding='utf-8') as enc:
                 enc.write(soup3.prettify())
                 print(outfilename, 'contains', os.stat(
                 outfilename).st_size, 'bytes')
                 os.system('file -b --mime {}'.format(outfilename))
                 print("\n" + ('-' * 80) + "\n")

if __name__ == "__main__":

 gzip_collection()