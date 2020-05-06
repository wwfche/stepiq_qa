from .pages.press_news_page import Press_News_Page
import time

def test_guest_should_title(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/novosti/vasileostrovskiy-namyv/"
    page = Press_News_Page(browser, link)
    page.open()
    page.should_be_title_element()