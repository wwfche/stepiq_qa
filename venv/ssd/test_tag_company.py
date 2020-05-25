from .pages.company_page import Company_Page
import time

def test_compant_tag_sec(browser):
    link = "https://nota:media@ssd.notamedia.ru/company/"
    page = Company_Page(browser, link)
    page.open()
    page.should_be_tag_security()


def test_compant_tag_isp(browser):
    link = "https://nota:media@ssd.notamedia.ru/company/"
    page = Company_Page(browser, link)
    page.open()
    page.should_be_tag_isp()


def test_compant_tag_comf(browser):
    link = "https://nota:media@ssd.notamedia.ru/company/"
    page = Company_Page(browser, link)
    page.open()
    page.should_be_tag_comf()


def test_compant_tag_srok(browser):
    link = "https://nota:media@ssd.notamedia.ru/company/"
    page = Company_Page(browser, link)
    page.open()
    page.should_be_tag_srok()

def test_compact_tag_format(browser):
    link = "https://nota:media@ssd.notamedia.ru/company/"
    page = Company_Page(browser, link)
    page.open()
    page.should_be_title_format()