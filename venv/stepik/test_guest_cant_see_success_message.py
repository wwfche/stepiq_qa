from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_other_stuped(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    #page.should_be_product_page() #ссанина с добавлением в корзину
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()