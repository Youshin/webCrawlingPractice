import sys
from urllib.request import urlopen

uf = urlopen("http://hanbit.co.kr/store/books/full_book_list.html")
# print(uf.read())

encoding = uf.info().get_content_charset(failobj='utf-8')
print('encoding:', encoding, file=sys.stderr)

text = uf.read().decode(encoding)
print(text)