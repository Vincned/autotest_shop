from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_of_the_item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.add_item_to_cart = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.remove_sauce_labs_backpack = (By.ID, 'remove-sauce-labs-backpack')
        self.wait = (WebDriverWait(self.driver, 10).until)
        self.short_container = (By.CLASS_NAME, 'product_sort_container')
        self.low_to_high = (By.CLASS_NAME, 'product_sort_container')
        self.active_option = (By.CLASS_NAME, 'active_option')
        self.inventory_item_price = (By.CLASS_NAME, 'inventory_item_price')
        self.card_product = (By.CLASS_NAME, 'inventory_item_name ')

    def is_loaded(self):
        self.wait(EC.visibility_of_element_located(self.inventory_of_the_item_name))
        inventory_item_names = self.driver.find_elements(*self.inventory_of_the_item_name)
        return len(inventory_item_names) > 0

    def sort_price_low_to_high(self):
        try:
            shorting = Select(self.driver.find_element(*self.low_to_high))
            shorting.select_by_value('lohi')
            price_elements = self.driver.find_elements(*self.inventory_item_price)
            list_of_prices = [float(el.text.replace('$', '')) for el in price_elements]
            return list_of_prices
        except:
            return None

    def add_to_cart(self):
        self.wait(EC.element_to_be_clickable(self.add_item_to_cart))
        print('Click add to cart')
        self.driver.find_element(*self.add_item_to_cart).click()
        print('Item was added')

    def shopping_cart_quantity(self):
        print('Counting numer of the items in the cart')
        try:
            quantity = self.wait(EC.visibility_of_element_located(self.shopping_cart_badge)).text
            return int(quantity)
        except:
            return 0

    def go_to_cart(self):
        try:
            cart = self.wait(EC.element_to_be_clickable(self.shopping_cart_badge))
            cart.click()
        except:
            return None

    def open_product_page(self):
        try:
            product_page = self.driver.find_elements(*self.card_product)
            for el in product_page:
                if 'Sauce Labs Backpack' in el.text:
                    el.click()
                    return True
        except Exception as e:
            print(f'This card with item was not found on the page:{e}')
            return False

