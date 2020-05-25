from selenium import webdriver
import math
import time

try:
    link = "https://pics.capitalgroup.ru/pic/%D0%91%D0%BE%D0%B9/%D0%A0%D0%9A_%D0%A1%D0%B0%D0%B9%D1%82_%D0%9E%D0%9A%D0%9E.xml"
    broswer = webdriver.Chrome()
    broswer.get(link)
    vid = broswer.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/div[4]/div[1]/div[2]/div[31]/div[1]/div[2]/div[6]/div[1]/div[2]/div[25]/span[2]').text
    print(vid)

finally:
    time.sleep(5)