import pytest
from selenium import webdriver
from pages.sbis_contact_page import SbisContactPage
from pages.tensor_page import TensorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Путь к драйверу может быть настроен
    yield driver
    driver.quit()

def test_scenario_1(driver):
    sbis_page = SbisContactPage(driver)
    tensor_page = TensorPage(driver)

    # Шаг 1: Перейти на страницу контактов
    sbis_page.open()

    # Шаг 2: Найти баннер Тензор и кликнуть по нему
    sbis_page.click_tensor_banner()

    # Шаг 3: Проверить, что на странице Тензор есть блок "Сила в людях"
    tensor_page.check_force_in_people_block()

    # Шаг 4: Кликнуть на "Подробнее" и проверить переход на страницу about
    tensor_page.click_more()
    tensor_page.verify_about_page()
