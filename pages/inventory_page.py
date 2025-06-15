from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_of_the_item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.add_item_to_cart = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.remove_sauce_labs_backpack = (By.ID, 'remove-sauce-labs-backpack')

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.inventory_of_the_item_name))
        inventory_item_names = self.driver.find_elements(*self.inventory_of_the_item_name)
        return len(inventory_item_names) > 0

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_item_to_cart))
        print('Click add to cart')
        self.driver.find_element(*self.add_item_to_cart).click()
        print('Item was added')

    def shopping_cart_quantity(self):
        try:
            quantity = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.shopping_cart_badge)).text
            return int(quantity)
        except:
            return 0

    def go_to_cart(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.shopping_cart_badge))
            cart.click()
        except:
            return None