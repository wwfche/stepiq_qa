from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    z = int(x) + int(y)
    print(z)
    w = str(z)
    browser.find_element_by_css_selector("[value='" + w + "']").click()
   # browser.find_element_by_css_selector("[value=w]").click()
    browser.find_element_by_css_selector("[type='submit']").click()
    browser.current_url


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()