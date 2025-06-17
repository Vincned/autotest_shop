from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        # Локаторы для списка товаров
        self.inventory_of_the_item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.add_item_to_cart = (By.ID, 'add-to-cart-sauce-labs-backpack')  # для главной страницы
        self.shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.remove_sauce_labs_backpack = (By.ID, 'remove-sauce-labs-backpack')
        self.sort_dropdown = (By.CLASS_NAME, 'product_sort_container')
        self.active_option = (By.CLASS_NAME, 'active_option')
        self.inventory_item_price = (By.CLASS_NAME, 'inventory_item_price')
        # Локаторы для страницы товара
        self.card_product = (By.CSS_SELECTOR, '.inventory_details_name.large_size')
        self.item_desc = (By.CLASS_NAME, 'inventory_details_desc')
        self.item_add_to_cart_button = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")  # универсальный
        self.price_of_the_item = (By.CLASS_NAME, 'inventory_details_price')

    def full_info_about_item(self):
        item_name = self.wait.until(EC.visibility_of_element_located(self.card_product)).text
        item_desc = self.wait.until(EC.visibility_of_element_located(self.item_desc)).text
        item_price = self.wait.until(EC.visibility_of_element_located(self.price_of_the_item)).text
        item_add_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.item_add_to_cart_button))
        return {
            'name': item_name,
            'desc': item_desc,
            'price': item_price,
            'add_button': item_add_to_cart_button
        }

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.inventory_of_the_item_name))
        inventory_item_names = self.driver.find_elements(*self.inventory_of_the_item_name)
        return len(inventory_item_names) > 0

    def sort_price_low_to_high(self):
        try:
            sorting = Select(self.driver.find_element(*self.sort_dropdown))
            sorting.select_by_value('lohi')
            price_elements_low = self.driver.find_elements(*self.inventory_item_price)
            return [float(el.text.replace('$', '')) for el in price_elements_low]
        except:
            return None

    def sort_price_high_to_low(self):
        try:
            sorting = Select(self.driver.find_element(*self.sort_dropdown))
            sorting.select_by_value('hilo')
            price_elements_high = self.driver.find_elements(*self.inventory_item_price)
            return [float(el.text.replace('$', '')) for el in price_elements_high]
        except:
            return None

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_item_to_cart))
        self.driver.find_element(*self.add_item_to_cart).click()

    def shopping_cart_quantity(self):
        try:
            quantity = self.wait.until(EC.visibility_of_element_located(self.shopping_cart_badge)).text
            return int(quantity)
        except:
            return 0

    def go_to_cart(self):
        try:
            cart = self.wait.until(EC.element_to_be_clickable(self.shopping_cart_badge))
            cart.click()
        except:
            return None

    def get_product_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[data-test='inventory-item-name']").text

    def open_product_page(self, product_name):
        try:
            product_page = self.driver.find_elements(*self.inventory_of_the_item_name)
            for el in product_page:
                if product_name in el.text:
                    el.click()
                    return True
        except Exception as e:
            print(f'This card with item was not found on the page: {e}')
            return False
