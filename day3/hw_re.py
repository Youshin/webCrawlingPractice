import re
import urllib.request

url = 'http://hanbit.co.kr'
full_book_url = '/store/books/full_book_list.html'
html = urllib.request.urlopen(url + full_book_url)
encoding = html.info().get_content_charset(failobj='utf-8')
html_contents = html.read().decode(encoding)


url_list = re.findall(r"(\<table class=\"tbl_type_list\")([\s\S]+?)(<\/table\>)", html_contents)

# print(url_list)
url_list = "".join(url_list[0])
book_list = re.findall(r"(\<a href=)([\s\S]+?)(<\/a\>)", url_list)

"""
한빛 사이트
도서명/링크
"""
# print(book_list)
for book in book_list:
    link, name = book[1].split("\">")
    link = link[1:]
    print(url+ link, name)
