#убираем слипы
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/wait1.html"


try:
    browser.get(link)
    ver = browser.find_element_by_id("verify").click()
    text_mes = browser.find_element_by_id("verify_message")
    assert text_mes.text == "Verification was successful!"




finally:
    time.sleep(5)
    browser.quit()
