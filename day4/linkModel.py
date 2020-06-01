from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bs_obj = BeautifulSoup(html, 'html.parser')
for link in bs_obj.find('div',{'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki)((?!:).)*$') ):
    if 'href' in link.attrs:
        print(link.attrs['href'])