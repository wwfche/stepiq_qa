from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #confirm = browser.switch_to.alert
    #confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    button1 = browser.find_element_by_css_selector("[type='submit']").click()







finally:
    time.sleep(5)
    #browser.quit()