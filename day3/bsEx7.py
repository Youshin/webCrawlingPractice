from bs4 import BeautifulSoup
import requests

url = 'https://www.eoscanada.com/en/tools/eos-go'

result =requests.get(url)
bs_obj = BeautifulSoup(result.content, 'html.parser')

div_name = bs_obj.find('div',{'class':'hs-menu-wrapper active-branch flyouts hs-menu-flow-horizontal'})
ul_tag = div_name.find('ul')

all_atag = ul_tag.findAll('a')

for a_tag in all_atag:
    link = a_tag['href']
    print('link info:', link)
    print('title:',a_tag.text)

# def get_bp_info(url):
    # result = requests