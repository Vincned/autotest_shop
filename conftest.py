import pytest
from selenium import webdriver
from pages.login_page_v2 import LoginPage

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    return driver

@pytest.fixture(scope='session')
def base_url():
    return 'https://www.saucedemo.com'