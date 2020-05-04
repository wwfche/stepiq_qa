#поис элемента которого не должно быть на странице
import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
#У кого последний pytest, там устарел параметр  message в строке with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить")

#теперь так
with pytest.raises(NoSuchElementException):
    browser.find_element_by_css_selector("button.btn")
    pytest.fail("Не должно быть кнопки Отправить")