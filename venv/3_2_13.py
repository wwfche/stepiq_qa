#используем ассерт unitesta из задачи 1.6.7 тест падает на втором тесте
from selenium import webdriver
import time
import unittest

class TestUT(unittest.TestCase):

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        first.send_keys("Dmitriy")

        last = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        last.send_keys("ivanov")
        email = browser.find_element_by_class_name("third")
        email.send_keys("test@test.ru")

        time.sleep(2)
        ...

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        first.send_keys("Dmitriy")

        last = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        last.send_keys("ivanov")
        email = browser.find_element_by_class_name("third")
        email.send_keys("test@test.ru")

        time.sleep(2)
        ...

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
   unittest.main()
