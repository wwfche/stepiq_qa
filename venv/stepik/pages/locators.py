from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTR_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')
    xyz = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_CARD = (By.CSS_SELECTOR, "[href='/ru/basket/']")