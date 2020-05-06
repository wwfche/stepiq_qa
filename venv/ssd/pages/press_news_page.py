from .base_page import BasePage
from .locators import ElementLocators

class Press_News_Page(BasePage):
    def should_be_title_element(self):
        #self.should_be_title_url()
        #self.should_be_title_tag()
        assert self.is_element_present(*ElementLocators.TITLE_ELEMENT), "No title element "