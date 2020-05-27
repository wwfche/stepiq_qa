
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException

import time



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page() #ссанина с добавлением в корзину
    #page.solve_quiz_and_get_code()
    #page.is_not_element_present()
    page.should_not_be_success_message()