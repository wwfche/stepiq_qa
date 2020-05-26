from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_to_card()


    def add_to_card(self):
        add_to_card = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        add_to_card.click()



