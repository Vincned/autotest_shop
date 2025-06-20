import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page_v2 import LoginPage

login_password = ("standard_user", "secret_sauce")

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
    login_page.login(*login_password)
    return driver

@pytest.fixture(scope='session')
def base_url():
    return 'https://www.saucedemo.com'

@pytest.fixture
def prepare_checkout_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(*login_password)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), 'Inventory page is loaded'
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()
    return driver