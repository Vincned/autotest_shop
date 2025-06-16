from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.sauce_labs_backpack = (By.ID, 'item_4_title_link')
        self.removed_cart_item = (By.ID, 'remove-sauce-labs-backpack')
        self.continue_shopping = (By.ID, 'continue-shopping')

    def get_cart_item_name(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sauce_labs_backpack))
            backpack_name = self.driver.find_element(*self.sauce_labs_backpack).text
            return backpack_name
        except:
            return None

    def remove_from_cart(self):
        try:
            remove_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.removed_cart_item))
            remove_item.click()
            print('Item was deleted from the cart')
            return True
        except:
            print(f'Item for removing was not found')
            return False

    def return_to_shopping(self):
        print(f'Current URL:', self.driver.current_url)
        try:
            self.driver.find_element(*self.continue_shopping).click()

            WebDriverWait(self.driver, 10).until(EC.url_contains('inventory'))
            print(f'Returned to the URL:', self.driver.current_url)
            return True
        except Exception as e:
            print(f'Not returned to the shopping page, Error: {e}, current url:{self.driver.current_url}')
            return False