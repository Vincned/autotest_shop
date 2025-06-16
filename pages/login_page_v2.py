#The goal of this file - to create class with functions of the logic for the test (what we are searching for, where, etc).

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage: #create class
    def __init__(self,driver): #default config, driver from the conftest file
        self.driver = driver #It is possible to use it in the all file
        self.user_name = (By.ID, 'user-name') #field user name search
        self.user_password = (By.ID, 'password') #field password search
        self.button = (By.ID, 'login-button') #button search
        self.burger_menu = (By.CLASS_NAME, 'bm-burger-button')
        self.logout_button = (By.ID, 'logout_sidebar_link')
        self.wait = WebDriverWait(self.driver, 10)
        self.error_message = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def load(self, url='https://www.saucedemo.com'):
        self.driver.get(url)

    def login(self, username, password):
        # Enter username
        username_field = self.wait.until(EC.visibility_of_element_located(self.user_name))
        username_field.send_keys(username)
        # Password
        password_field = self.wait.until(EC.visibility_of_element_located(self.user_password))
        password_field.send_keys(password)
        # Search button and click on it
        button_click = self.wait.until(EC.element_to_be_clickable(self.button))
        button_click.click()
        self.wait.until(EC.url_contains('inventory'))

    def is_login_successful(self):
        return 'inventory' in self.driver.current_url

    def get_error_message(self):
        try:
            error_message = self.driver.find_element(*self.error_message).text
            return error_message
        except:
            return None

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.burger_menu))
        self.driver.find_element(*self.burger_menu).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_button))
        self.driver.find_element(*self.logout_button).click()
        return True