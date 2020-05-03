from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    print(x)
    y = calc(x)
    print(y)
    a = browser.find_element_by_id("answer")
    a.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    submit = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()