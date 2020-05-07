#сделать проверку на странице проектов по xpath у всех проектов
from .pages.project_page import Project_Page
import time
#Тихая
def test_title_element_main_tihaya(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/tihaya-gavan/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_tihaya(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_tihaya(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/tihaya-gavan/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()



def test_title_element_second_2_tihaya(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/tihaya-gavan/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()


#Станция Л
def test_title_element_main_l(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/station-l/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_l(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_l(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/station-l/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()

def test_title_element_second_2_l(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/station-l/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()

#В стремлении к свету
def test_title_element_main_v_stremlenii(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/v-stremlenii-k-svety/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_v_stremlenii(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_v_stremlenii(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/v-stremlenii-k-svety/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()

def test_title_element_second_2_v_stremlenii(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/v-stremlenii-k-svety/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()

#сказочный лес
def test_title_element_main_skaz(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/skazochniyles/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_skaz(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_skaz(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/skazochniyles/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()

def test_title_element_second_2_skaz(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/skazochniyles/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()

#мир внутри
def test_title_element_main_mir(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/mir-vnutri/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_mir(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_mir(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/mir-vnutri/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()

def test_title_element_second_2_mir(browser):
    link = "https://nota:media@ssd.notamedia.ru/projects/mir-vnutri/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()

#юность
def test_title_element_main_unost(browser):
    link = "https://nota:media@ssd.notamedia.ru/realized-projects/o_unost/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_main()

def test_title_anons_main_unost(browser):
    link = "https://nota:media@ssd.notamedia.ru/realized-projects/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_anons_main()

def test_title_element_second_1_unost(browser):
    link = "https://nota:media@ssd.notamedia.ru/realized-projects/o_unost/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_1()

def test_title_element_second_2_unost(browser):
    link = "https://nota:media@ssd.notamedia.ru/realized-projects/o_unost/"
    page = Project_Page(browser, link)
    page.open()
    page.should_be_title_element_second_2()