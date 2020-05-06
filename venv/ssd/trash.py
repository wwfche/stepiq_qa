from selenium import webdriver

browser = webdriver.Chrome()


link = "https://nota:media@ssd.notamedia.ru/press-center/novosti/vasileostrovskiy-namyv/"

browser.get(link)
browser.find_element_by_css_selector("[title='test_alt_element']")



