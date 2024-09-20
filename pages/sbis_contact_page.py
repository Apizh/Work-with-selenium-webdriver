from selenium.webdriver.common.by import By
from .base_page import BasePage

class SbisContactPage(BasePage):
    CONTACTS_URL = "https://sbis.ru/contacts"
    TENSOR_BANNER = (By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')

    def open(self):
        self.driver.get(self.CONTACTS_URL)

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)
