from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checkAddToBaskedButton(browser):
    browser.get(link)
    # Таймер закоменчен для ускорения проверки
    #time.sleep(10)
    """
    # Решение через try except и pytest.fail
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket1")
    except NoSuchElementException:
        pytest.fail("Кнопка \"Добавить в корзину\" не найденна на странице")
    """
    #"""
    # Решение через assert
    addToBaskedButton = len(browser.find_elements(By.CSS_SELECTOR,"button.btn-add-to-basket"))
    assert addToBaskedButton > 0, "Кнопка \"Добавить в корзину\" не найденна на странице"
    #"""
    time.sleep(10)