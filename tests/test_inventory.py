import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page_v2 import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_item_full_check(login_user):
    inventory_page = InventoryPage(login_user)
    inventory_page.open_product_page('Sauce Labs Backpack')
    info = inventory_page.full_info_about_item()
    assert info['name'], 'Item name is empty'
    assert info['desc'], 'Item desc is empty'
    assert info['price'].startswith('$'), 'Price should start with "$"'
    assert info['add_button'].is_displayed(), 'Add to cart button is not visible'

def test_sort_prices_low_to_high(login_user):
    inventory_page = InventoryPage(login_user)
    short_list = inventory_page.sort_price_low_to_high()
    assert short_list == sorted(short_list), 'Prices are not sorted ascending'

def test_sort_prices_high_to_low(login_user):
    inventory_page = InventoryPage(login_user)
    short_list = inventory_page.sort_price_high_to_low()
    assert short_list == sorted(short_list, reverse=True), 'Prices are not sorted ascending'

def test_open_product_page(login_user):
    inventory_page = InventoryPage(login_user)
    inventory_page.open_product_page('Sauce Labs Backpack')
    assert 'inventory-item' in login_user.current_url, 'The URL is not right'

    title_of_product = inventory_page.get_product_title()
    assert 'Sauce Labs Backpack' in title_of_product, 'Wrong product detail page'

@pytest.mark.parametrize('username, password', [
    ('standard_user', 'secret_sauce')
])
def test_add_to_cart(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), 'Inventory page is not ready'

    inventory_page.add_to_cart()

    quantity = inventory_page.shopping_cart_quantity()
    assert quantity == 1, f'Expected 1 item in cart, but got {quantity}'

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    check_cart = cart_page.get_cart_item_name()
    assert check_cart == 'Sauce Labs Backpack', 'Item was not found'

    cart_remove = cart_page.remove_from_cart()
    assert cart_remove, 'Item was not deleted from the cart'

    assert cart_page.return_to_shopping(), 'Failed to return to inventory page'
