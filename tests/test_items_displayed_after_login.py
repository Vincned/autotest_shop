import pytest

from pages.inventory_page import InventoryPage
from pages.login_page_v2 import LoginPage

@pytest.mark.parametrize('username, password',[
    ("standard_user", "secret_sauce"),
    ('locked_out_user', "secret_sauce"),
    ('problem_user', "secret_sauce")
])

def test_items(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    is_empty = inventory_page.is_loaded()
    assert is_empty, 'No items on the page'


