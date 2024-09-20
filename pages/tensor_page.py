from selenium.webdriver.common.by import By
from .base_page import BasePage

class TensorPage(BasePage):
    FORCE_IN_PEOPLE = (By.CSS_SELECTOR, 'section.force-in-people')
    MORE_BUTTON = (By.LINK_TEXT, 'Подробнее')

    def check_force_in_people_block(self):
        return self.find(self.FORCE_IN_PEOPLE)

    def click_more(self):
        self.click(self.MORE_BUTTON)

    def verify_about_page(self):
        assert "about" in self.driver.current_url, "URL страницы не содержит 'about'"
