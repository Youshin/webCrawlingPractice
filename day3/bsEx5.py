from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.naver.com'
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')

ul_tag = bs_obj.find('ul',{'class':'list_nav type_fix'})
# print(ul_tag)

lis = ul_tag.findAll('li')

for li in lis:
    a_tag = li.find('a')
    print(a_tag.text)