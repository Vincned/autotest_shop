import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage  # import of the class with functions to the file for using
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@pytest.mark.parametrize('username, password, should_fail', [
    ("", "", True),
    ("aa", "", True),
    ("", "aa", True),
    ("wrong", "wrong", True),
    ("standard_user", "wrong", True),
    ("standard_user" ,"secret_sauce", False)
])

def test_auth(driver, username, password, should_fail):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    #error check
    if should_fail:
        error = login_page.get_error_message()
        assert error is not None, "Error must be displayed while wrong data where used in the test"
        assert 'Epic sadface' in error
    else:
        assert 'inventory' in driver.current_url, 'Login should be successfull'

def test_logout(driver):
    login_page = LoginPage(driver)  # imprort class and driver for using
    login_page.load()  # call the load function
    login_page.login("standard_user", "secret_sauce")
    login_page.logout()

    assert 'saucedemo' in driver.current_url, 'Is not default page'