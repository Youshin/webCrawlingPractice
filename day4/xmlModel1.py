from bs4 import BeautifulSoup

with open('books.xml', 'r', encoding='utf8') as books_file:
    books_xml = books_file.read()

bs_obj = BeautifulSoup(books_xml, 'lxml')
# print(bs_obj)

for book_info in bs_obj.findAll('author'):
    print(book_info)
    print(book_info.get_text())