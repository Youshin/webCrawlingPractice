import sys, re
from urllib.request import urlopen

uf = urlopen("http://hanbit.co.kr/store/books/full_book_list.html")
# print(uf.read())
byte_content = uf.read()

scanned_text = byte_content[0:1024].decode('ascii', errors='replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
    encoding = match.group(1)
    print(encoding)
else:
    encoding='utf-8'

print('encoding:',encoding, file=sys.stderr)

text = byte_content.decode(encoding)

print(text)