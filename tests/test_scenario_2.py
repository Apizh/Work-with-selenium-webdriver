import pytest
from selenium import webdriver
from pages.sbis_contact_page import SbisContactPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Путь к драйверу может быть настроен
    yield driver
    driver.quit()

def test_scenario_2(driver):
    sbis_page = SbisContactPage(driver)

    # Шаг 1: Перейти на страницу контактов
    sbis_page.open()

    # Шаг 2: Проверить определение региона
    region = sbis_page.find_region()
    assert region == "Ярославская обл.", f"Ожидался регион 'Ярославская обл.', но был {region}"

    # Шаг 3: Изменить регион на Камчатский край
    sbis_page.change_region("Камчатский край")

    # Шаг 4: Проверить, что регион изменен
    assert "Камчатский край" in driver.title, "Регион не изменился в title"
