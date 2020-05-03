from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/wait1.html"


try:
    browser.get(link)
    time.sleep(5)
    ver = browser.find_element_by_id("verify").click()
    text_mes = browser.find_element_by_id("verify_message")
    assert text_mes.text == "Verification was successful!"




finally:
    time.sleep(5)
    browser.quit()


