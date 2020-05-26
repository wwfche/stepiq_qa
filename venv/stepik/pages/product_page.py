from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_to_card()


    def add_to_card(self):
        add_to_card = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        add_to_card.click()

    def compare_name(self):
        alert_name = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[0].text
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        assert alert_name == name, "The name in the basket does not match"

    def compare_price(self):
        alert_price = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[2].text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert alert_price == price, "The price in the basket does not match"

    def should_not_be_success_mesage(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented, but should not be"

    def should_be_success_mesage(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is NOT presented, but should  be"
