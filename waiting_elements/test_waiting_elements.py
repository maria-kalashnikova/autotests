import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize("elem", ["//input[@name='search']", "//div[@class='product-thumb transition']",
                                  "//div[@class='carousel swiper-viewport']", "//h3[text()='Featured']",
                                  "//ul[@class='nav navbar-nav']"])
def test_elements_main_page(browser, elem):
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")


@pytest.mark.parametrize("elem", ["//h2[text()='Laptops & Notebooks']", "//aside[@id='column-left']",
                                  "//ul[@class='breadcrumb']", "//button[@id='grid-view']", "//a[@id='compare-total']"])
def test_elements_catalog_page(browser, base_url, elem):
    browser.get(f"{base_url}/laptop-notebook")
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")


@pytest.mark.parametrize("elem", ["//button[@data-original-title='Add to Wish List']", "//ul[@class='list-unstyled']",
                                  "//h3[text()='Available Options']", "//div[@class='radio']",
                                  "//div[@class='checkbox']"])
def test_elements_card_page(browser, base_url, elem):
    browser.get(f"{base_url}/component/monitor/test")
    browser.implicitly_wait(3)
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")


@pytest.mark.parametrize("elem", ["//label[text()='Username']", "//input[@name='username']",
                                  "//a[text()='Forgotten Password']", "//button[text()=' Login']",
                                  "//input[@name='password']"])
def test_elements_login_adm_page(browser, base_url, elem):
    browser.get(f"{base_url}/admin")
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")


@pytest.mark.parametrize("elem", ["//h1[text()='Register Account']", "//input[@name='firstname']",
                                  "//legend[text()='Your Password']", "//label[@class='radio-inline']",
                                  "//input[@value='Continue']"])
def test_elements_reg_user_page(browser, base_url, elem):
    browser.get(f"{base_url}/index.php?route=account/register")
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, elem)))
    except TimeoutException:
        raise AssertionError(f"Элемент по локатору '{elem}' на странице не найден")
