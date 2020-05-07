from selenium.webdriver.common.by import By

class ElementLocators():
    TITLE_ELEMENT = (By.CSS_SELECTOR, "[title='test_title_element']")
    TITLE_ANONS = (By.CSS_SELECTOR, "[title='test_title_anons']")

#локаторы для проектов
    TITLE_ELEMENT_PROJECT_MAIN = (By.CSS_SELECTOR, "[title='test_title_element_project_main']")
    TITLE_ANONS_PROJECT_MAIN = (By.CSS_SELECTOR, "[title='test_title_anons_project_main']")
    TITLE_ELEMENT_PROJECT_SECOND_1 = (By.CSS_SELECTOR, "[title='test_title_element_project_second1']")
    TITLE_ELEMENT_PROJECT_SECOND_2 = (By.CSS_SELECTOR, "[title='test_title_element_project_second2']")

#локаторы оснавные характеристики компании
    TITLE_IMG_SEC = (By.CSS_SELECTOR, "[title='test_title_sec']")
    ALT_IMG_SEC = (By.CSS_SELECTOR, "[alt='test_alt_sec']")
    TITLE_IMG_ISP = (By.CSS_SELECTOR, "[title='test_title_isp']")
    ALT_IMG_ISP = (By.CSS_SELECTOR, "[alt='test_alt_isp']")
    TITLE_IMG_COMF = (By.CSS_SELECTOR, "[title='test_title_comf']")
    ALT_IMG_COMF = (By.CSS_SELECTOR, "[alt='test_alt_comf']")
    TITLE_IMG_SROK = (By.CSS_SELECTOR, "[title='test_title_srok']")
    ALT_IMG_SROK = (By.CSS_SELECTOR, "[alt='test_alt_srok']")


