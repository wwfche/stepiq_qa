import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    driver = request.config.getoption("browser")
    language = request.config.getoption("language")
    browser = None
    if driver == "chrome":
        print("\nstart chrome browser for test..")
        #browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif driver == "firefox":
        print("\nstart firefox browser for test..")
        #browser = webdriver.Firefox()
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()