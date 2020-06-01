from bs4 import BeautifulSoup
import urllib.request

url = 'https://news.naver.com/'
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')

ul_tag = bs_obj.find('ul',{'class':'hdline_article_list'})
# print(ul_tag)

lis = ul_tag.findAll('li')
for li in lis:
    a_tag = li.find('a')
    print(a_tag.text.strip(), a_tag['href'].strip())