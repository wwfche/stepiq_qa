from selenium import webdriver

globals driver = webdriver.Chrome()

def yandex():
    driver.get('https://ya.ru')