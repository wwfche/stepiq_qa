from .base_page import BasePage
from .locators import ElementLocators

class Project_Page(BasePage):
    def should_be_title_element_main(self):
        assert self.is_element_present(*ElementLocators.TITLE_ELEMENT_PROJECT_MAIN), "No title element MAIN"

    def should_be_title_anons_main(self):
        assert self.is_element_present(*ElementLocators.TITLE_ANONS_PROJECT_MAIN), "No title anons MAIN"

    def should_be_title_element_second(self):
        assert self.is_element_present(*ElementLocators.TITLE_ELEMENT_PROJECT_SECOND), "No title element SECOND"
