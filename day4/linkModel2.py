from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bs_obj = BeautifulSoup(html, 'html.parser')
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id='mw-content-text').findAll('p'[0]))
        print(bs_obj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print("no tag")

    for link in bs_obj.findAll('a',href=re.compile('^(/wiki/)') ):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")