import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage  # import of the class with functions to the file for using
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

import pytest
from pages.login_page_v2 import LoginPage

@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("invalid_user", "secret_sauce", "Epic sadface: Username and password do not match"),
    ("standard_user", "wrong_password", "Epic sadface: Username and password do not match"),
    ("", "", "Epic sadface: Username is required"),
])
def test_auth_invalid(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password, expect_success=False)

    error = login_page.get_error_message()

    assert error is not None, "Expected message about error, but NONE"
    assert expected_error.lower() in error.lower(), f"Expected: '{expected_error}', got: '{error}'"


@allure.title('Logout test after successful login')
def test_logout(login_user):
    login_page = LoginPage(login_user)
    login_page.logout()
    assert 'saucedemo' in login_user.current_url or 'login' in login_user.current_url, 'Is not default page'