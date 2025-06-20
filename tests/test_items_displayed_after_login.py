import pytest

from pages.inventory_page import InventoryPage
from pages.login_page_v2 import LoginPage

@pytest.mark.parametrize('username, password, should_fail',[
    ("standard_user", "secret_sauce", False),
])

def test_items(driver, username, password, should_fail):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    is_empty = inventory_page.is_loaded()
    assert is_empty, 'No items on the page'


