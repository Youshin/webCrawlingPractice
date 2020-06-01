from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import random
_id = 'dragon_1411'
_pw = 'dbtls141!'
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')

""" 방법 1 잘됨.. """ 
time.sleep(1)
driver.find_element_by_class_name("link_login").click()
time.sleep(1)

tag_id = driver.find_element_by_name('id')
tag_id.clear()
time.sleep(1)

tag_id.click()
pyperclip.copy(_id)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

tag_pw = driver.find_element_by_name('pw')
pyperclip.copy(_pw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
""" 방법 2 잘안됨.. ㅠㅠ """
# time.sleep(random.uniform(0.5, 1))

# driver.find_element_by_class_name("link_login").click()
# time.sleep(random.uniform(0.5, 1))

# driver.find_element_by_name('id').click()
# driver.find_element_by_name('id').clear()
# for char in _id:
#     driver.find_element_by_name('id').send_keys(char)
#     time.sleep(random.uniform(0.01, 0.3))
# time.sleep(random.uniform(0.5, 1))
# driver.find_element_by_name('pw').click()
# for char in _pw:
#     driver.find_element_by_name('pw').send_keys(char)
#     time.sleep(random.uniform(0.01, 0.3))
# time.sleep(random.uniform(0.5, 1))

""" 실행 """
# driver.find_element_by_id("log.login").click()
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

from bs4 import BeautifulSoup

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
bs_obj = BeautifulSoup(html, 'html.parser')
print(bs_obj)