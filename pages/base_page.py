from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.wait = WebDriverWait(driver, timeout)

    def go_to(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)