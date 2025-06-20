from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.checkout = (By.ID, 'checkout')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_Code = (By.ID, 'postal-code')
        self.continue_order = (By.ID, 'continue')
        self.finish = (By.ID, 'finish')

    def checkout_button(self):
        self.wait.until(EC.visibility_of_element_located(self.checkout))
        self.driver.find_element(*self.checkout).click()

    def order_info(self):
        self.wait.until(EC.visibility_of_element_located(self.first_name))
        self.driver.find_element(*self.first_name).send_keys('John')

        self.wait.until(EC.visibility_of_element_located(self.last_name))
        self.driver.find_element(*self.last_name).send_keys('Smith')

        self.wait.until(EC.visibility_of_element_located(self.postal_Code))
        self.driver.find_element(*self.postal_Code).send_keys('1234567890')

    def continue_button(self):
        self.wait.until(EC.visibility_of_element_located(self.continue_order))
        self.driver.find_element(*self.continue_order).click()

    def finish_button(self):
        self.wait.until(EC.visibility_of_element_located(self.finish))
        self.driver.find_element(*self.finish).click()
