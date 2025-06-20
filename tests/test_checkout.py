import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage
from pages.checkout_page import Checkout

def test_full_checkout(driver,prepare_checkout_user):
    driver = prepare_checkout_user
    checkout_page = Checkout(driver)

    checkout_page.checkout_button()
    checkout_page.order_info()
    assert 'checkout-step-one' in driver.current_url, 'Not on the Your Information page'
    checkout_page.continue_button()
    assert 'checkout-step-two' in driver.current_url, f'Not on final checkout step, current link is {driver.current_url}'
    checkout_page.finish_button()
    assert 'checkout-complete' in driver.current_url, 'Checkout not completed'