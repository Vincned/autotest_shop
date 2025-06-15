import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage  # import of the class with functions to the file for using
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@pytest.mark.parametrize('username, password, should_fail', [
    ("standard_user" ,"secret_sauce", False),
    ('locked_out_user', "secret_sauce", False),
    ('problem_user', "secret_sauce", False)
])

def test_auth(driver, username, password, should_fail):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    assert 'inventory' in driver.current_url, 'Login should be successfull'

def test_logout(login_user):
    driver = login_user
    assert 'saucedemo' in driver.current_url, 'Is not default page'