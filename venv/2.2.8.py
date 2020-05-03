from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("1")
    last = browser.find_element_by_css_selector("[name='lastname']")
    last.send_keys("1")
    mail = browser.find_element_by_css_selector("[name='email']")
    mail.send_keys("1")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    a = browser.find_element_by_id('file')
    a.send_keys(file_path)
    #element.send_keys('file_path')



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()