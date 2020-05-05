import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def findByCss(browser, selector):
    return WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

def if_element_exist(browser, selector):
    try:
        findByCss(browser, selector)
    except TimeoutException:
        return False
    return True

def test_busket_button_exist(browser):
    browser.get(link)
    assert if_element_exist(browser, '.btn-add-to-basket'), 'An element has no exist'
    time.sleep(20)