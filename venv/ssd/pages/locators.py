from selenium.webdriver.common.by import By

class ElementLocators():
    TITLE_ELEMENT = (By.CSS_SELECTOR, "[title='test_title_element']")
    TITLE_ANONS = (By.CSS_SELECTOR, "[title='test_title_anons']")

#локаторы для проектов
    TITLE_ELEMENT_PROJECT_MAIN = (By.CSS_SELECTOR, "[title='test_title_element_project_main']")
    TITLE_ANONS_PROJECT_MAIN = (By.CSS_SELECTOR, "[title='test_title_anons_project_main']")
    TITLE_ELEMENT_PROJECT_SECOND = (By.CSS_SELECTOR, "[title='test_title_element_project_second']")


