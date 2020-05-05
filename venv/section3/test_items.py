import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    #добавляем фриз как написано в требовании к задаче п.2
    time.sleep(30)

    #находим кнопку по xpath, если кнопки нет - тест падает

    button = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    #но в задаче попросили воткнуть assert зачем? хз!
    #assert button == browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    assert button.is_enabled()