import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage  # import of the class with functions to the file for using
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@pytest.mark.parametrize('username, password, should_fail', [
    ("standard_user" ,"secret_sauce", False),
    ('locked_out_user', "secret_sauce", True),
    ('problem_user', "secret_sauce", False)
])
@allure.title('Login tests various users')
def test_auth(driver, username, password, should_fail):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    if should_fail:
        error = login_page.get_error_message()
        assert error is not None, f"Expected login to fail for user {username}, but it succeeded"
    else:
        assert login_page.is_login_successful(), f"Login failed for valid user {username}"

@allure.title('Logout test after successful login')
def test_logout(login_user):
    login_page = LoginPage(login_user)
    login_page.logout()
    assert 'saucedemo' in login_user.current_url or 'login' in login_user.current_url, 'Is not default page'