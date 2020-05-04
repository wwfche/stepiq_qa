from selenium import webdriver
import pytest
import time
import math

#answer = math.log(int(time.time()))
#a = str(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()


    yield browser
    print("\nquit browser..")

    browser.quit()


@pytest.mark.parametrize('id', ["236895", "236896", "236897","236898", "236899", "236903", "236904", "236905" ])
def test_guest_should_see_login_link(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)

    time.sleep(5)

    first = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")

    answer = math.log(int(time.time()))
    a = str(answer)
    first.send_keys(a)

    time.sleep(2)

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    time.sleep(2)

    text = browser.find_element_by_class_name("smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = text.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == welcome_text
    time.sleep(1)