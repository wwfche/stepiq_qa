from .base_page import BasePage
from .locators import ElementLocators



class Company_Page(BasePage):
    def should_be_tag_security(self):
        assert self.is_element_present(*ElementLocators.TITLE_IMG_SEC), "Not Title SEC"
        assert self.is_element_present(*ElementLocators.ALT_IMG_SEC), "No ALT SEC"

    def should_be_tag_isp(self):
        assert self.is_element_present(*ElementLocators.TITLE_IMG_ISP), "Not Title ISP"
        assert self.is_element_present(*ElementLocators.ALT_IMG_ISP), "No ALT ISP"

    def should_be_tag_comf(self):
        assert self.is_element_present(*ElementLocators.TITLE_IMG_COMF), "Not Title COMF"
        assert self.is_element_present(*ElementLocators.ALT_IMG_COMF), "No ALT CPMF"

    def should_be_tag_srok(self):
        assert self.is_element_present(*ElementLocators.TITLE_IMG_SROK), "Not Title SROK"
        assert self.is_element_present(*ElementLocators.ALT_IMG_SROK), "No ALT SROK"
