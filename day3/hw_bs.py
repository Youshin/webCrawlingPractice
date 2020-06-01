from bs4 import BeautifulSoup
import requests

url = 'http://hanbit.co.kr'
full_book_url = '/store/books/full_book_list.html'

result =requests.get(url+full_book_url)
bs_obj = BeautifulSoup(result.content, 'html.parser')

table_name = bs_obj.find('table',{'class':'tbl_type_list'})
t_body = table_name.find('tbody')


all_atag = t_body.findAll('a')

# print(tr_tag)
for a_tag in all_atag:
    link = a_tag['href']
    print('link info:', url+link)
    print('title:',a_tag.text)

# def get_bp_info(url):
    # result = requests