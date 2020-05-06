from selenium.webdriver.common.by import By

class ElementLocators():
    TITLE_ELEMENT = (By.CSS_SELECTOR, "[title='test_alt_element']") # ПОМЕНЯТЬ НА TITLE, после того как Макс пофиксит
    TITLE_ANONS = (By.CSS_SELECTOR, "[title='test_title_anons']")
