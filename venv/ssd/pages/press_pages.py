from .base_page import BasePage
from .locators import ElementLocators

class Press_Pages(BasePage):
    def should_be_title_element(self):
        #self.should_be_title_url()
        #self.should_be_title_tag()
        assert self.is_element_present(*ElementLocators.TITLE_ELEMENT), "No title element "

    def should_be_title_anons(self):
        #self.should_be_title_url()
        #self.should_be_title_tag()
        assert self.is_element_present(*ElementLocators.TITLE_ANONS), "No title anons "

    def should_be_title_anons_summa(self):
        assert self.is


#class Press_Main_News(BasePage):
#    def should_be_title_anons(self):
#        #self.should_be_title_url()
#        #self.should_be_title_tag()
#        assert self.is_element_present(*ElementLocators.TITLE_ANONS), "No title anons "