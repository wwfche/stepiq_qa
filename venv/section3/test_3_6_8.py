
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    #находим кнопку по xpath, если кнопки нет - тест падает
    button = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
