from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser = webdriver.Chrome()
    browser.get(link)
    button_1 = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button')
    button_1.click()





finally:
    time.sleep(5)
    browser.quit()
