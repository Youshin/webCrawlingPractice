from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.naver.com'
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')

# print(bs_obj)

top_right = bs_obj.find('div', {'class': 'service_area'})

print(top_right)