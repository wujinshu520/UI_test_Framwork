from selenium import webdriver
from common.base_page import BasePage

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

element = driver.find_element_by_xpath('//*[@id="s-top-left"]/a[2]')

valaue = element.text
print(valaue)