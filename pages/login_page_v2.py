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

    def load(self):
        self.driver.get('https://www.saucedemo.com') #Pytest get the link for the use it in the tests

    def login(self, username, password):
        # Here we are unpacking the cortege user_name for the search the element, after that we are sending the username
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_name))
        username_field.send_keys(username)

        # Here we are unpacking the cortege user_password for the search the element, after that we are sending the password
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_password))
        password_field.send_keys(password)
        # Search button and click on it
        button_click =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button))
        button_click.click()

    def get_error_message(self):
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
            return error_message
        except:
            return None

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.burger_menu))
        self.driver.find_element(*self.burger_menu).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button))
        self.driver.find_element(*self.logout_button).click()