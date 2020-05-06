from .pages.press_pages import Press_Pages
#from .pages.press_pages import Press_Main_News
import time

def test_title_news_vasileostrovskiy(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/novosti/vasileostrovskiy-namyv/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_news_uvashaemie(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/novosti/uvazhaemye-klienty-i-posetiteli-nashego-ofisa/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_news_banki(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/novosti/banki-predostavlyayut-ipotechnye-kanikuly-iz-za-koronavirusa/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_events_tihaya_gavan(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/sobytiya/zhk-tikhaya-gavan-byvshiy-zhk-artur-grey-/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_events_tihaya_gavan(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/sobytiya/zhk-tikhaya-gavan-byvshiy-zhk-artur-grey-/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_events_svetliy_mir(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/sobytiya/svetlyy-mir-zhizn-martovskaya-aerosemka/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_events_subbotnik(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/sobytiya/vneplanovyy-subbotnik-u-zhk-svetlyy-mir-ya-romantik-/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_open_perk_na_namyve(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/open_hearts/park-na-namyve/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_open_tihaya_gavan_v_bud(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/open_hearts/zhk-tikhaya-gavan/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

def test_title_open_tihaya_gavan_2(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/open_hearts/zhk-tikhaya-gavan-2/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_element()

#позже допилить проверку: количество тестов в новостях == количеству тайтлов
def test_title_main_news(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_anons()

def test_title_main_sobytiya(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/sobytiya/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_anons()

def test_title_main_open(browser):
    link = "https://nota:media@ssd.notamedia.ru/press-center/open_hearts/"
    page = Press_Pages(browser, link)
    page.open()
    page.should_be_title_anons()