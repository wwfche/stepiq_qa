from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


link = "https://nota:media@ssd.notamedia.ru/company/"

browser.get(link)
time.sleep(5)
slider = browser.find_element_by_xpath("/html/body/div[5]/div/div[3]/div/div[1]/div[1]/img")
a = slider.get_attribute('title')
print(a)
assert a == "test_title_anons"






