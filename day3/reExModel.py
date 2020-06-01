import re
import urllib.request

url = 'https://finance.naver.com/item/main.nhn?code=066570'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('ms949'))

match = re.findall('(\<dl class=\"blind\">)([\s\S]+?)(<\/dl\>)', html_contents)
# print(match)
lg_stock = match[0]
lg_index = lg_stock[1]
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)",lg_index)

print(index_list)

for index in index_list:
    print(index[1])