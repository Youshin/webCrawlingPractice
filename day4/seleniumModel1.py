from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.naver.com')

driver.find_element_by_class_name("link_login").click()

driver.find_element_by_name('id').send_keys('') # id
driver.find_element_by_name('pw').send_keys('') #password


# driver.find_element_by_id("log.login").click()
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()