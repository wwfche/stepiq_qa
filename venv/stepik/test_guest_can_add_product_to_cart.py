
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time

def test_zaebal(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.solve_quiz_and_get_code()
    page.compare_name()
    page.compare_price()



