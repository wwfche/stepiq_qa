from selenium import webdriver

browser = webdriver.Chrome()


link = "https://nota:media@ssd.notamedia.ru/press-center/open_hearts/"

browser.get(link)
browser.find_element_by_css_selector("[title='test_title_anons']")
assert browser.find_elements_by_css_selector("[title='test_title_anons']").count



