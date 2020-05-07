from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


link = "https://nota:media@ssd.notamedia.ru/projects/tihaya-gavan/"

browser.get(link)
time.sleep(5)
#slider = browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[1]/div/div[2]")
#a = slider.get_attribute('title')
#print(a)
#assert a == " Светлый мир  Тихая Гавань... "
browser.find_element_by_css_selector("[title='test_title_element_project_main']")




