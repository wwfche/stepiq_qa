from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))
a = str(answer)

try:
    link = "https://stepik.org/lesson/236896/step/1"
    browser = webdriver.Chrome()
    browser.get(link)

    # first = browser.find_element_by_class_name("first")
    time.sleep(5)
    first = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
    first.send_keys(a)
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    text = browser.find_element_by_class_name("smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = text.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()