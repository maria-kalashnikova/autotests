"""
utf-8
Создан 31.03.2022

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №5. UI тесты для opencart
"""
import pytest
from selenium import webdriver


def browser_options(browser_instance):
    options = browser_instance
    options.add_argument('no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.AcceptInsecureCertificates = 'true'
    return options


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action='store',
        default="chrome",
        help="This is browser choice"
    )

    parser.addoption(
        "--url",
        action='store',
        default="http://192.168.0.157:8081",
        help="This is the website address"
    )

    parser.addoption(
        "--driver_path",
        action='store',
        default="C:\\Users\\maria.kalashnikova\\drivers\\chromedriver.exe",
        help="This is the executable path"
    )


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver_path(request):
    return request.config.getoption("--driver_path")

@pytest.fixture()
def init_browser(browser_name, driver_path):
    if browser_name == "chrome":
        instance = webdriver.ChromeOptions()
        options = browser_options(instance)
        driver = webdriver.Chrome(executable_path=driver_path)
        return driver
#     if browser_name == "firefox":
#         instance = webdriver.FirefoxOptions()
#         options = browser_options(instance)
#         driver = webdriver.Firefox(executable_path='', options=options)
#         return driver
#     if browser_name == "opera":
#         instance = webdriver.FirefoxOptions()
#         options = browser_options(instance)
#         driver = webdriver.Firefox(executable_path='', options=options)
#         return driver
#

@pytest.fixture()
def browser(init_browser, base_url):
    init_browser.get(base_url)
    yield init_browser
    init_browser.quit()
