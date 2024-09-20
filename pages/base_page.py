from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_page_title(self):
        return self.driver.title
