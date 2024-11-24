import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.forecast_page import ForecastPage
from utils.environment import BASE_URL
from utils.test_data import CITY_NAME, LATITUDE1, LONGITUDE2


@pytest.fixture
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@allure.feature("UI Tests")
@allure.story("Search Weather by City")
def test_search_weather_by_city(driver):
    with allure.step("Открытие главной страницы"):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

    with allure.step(f"Поиск погоды для города {CITY_NAME}"):
        home_page.search_city(CITY_NAME)

    with allure.step("Проверка отображения прогноза"):
        forecast_page = ForecastPage(driver)
        assert forecast_page.is_forecast_displayed(), (
            "Прогноз не отображается."
        )


@allure.feature("UI Tests")
@allure.story("Navigation to API Documentation")
def test_navigation_to_api_docs(driver):
    with allure.step("Открытие главной страницы"):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

    with allure.step("Переход в раздел документации API"):
        home_page.go_to_api_docs()

    with allure.step("Проверка открытия страницы документации"):
        assert home_page.is_api_docs_page_opened(), (
            "Документация API не открылась."
        )


@allure.feature("UI Tests")
@allure.story("Search Weather by Coordinates")
def test_search_weather_by_coordinates(driver):
    with allure.step("Открытие главной страницы"):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

    with allure.step("Поиск погоды по координатам: "
                     f"широта {LATITUDE1}, долгота {LONGITUDE2}"):
        home_page.search_by_coordinates(LATITUDE1, LONGITUDE2)

    with allure.step("Проверка отображения прогноза"):
        forecast_page = ForecastPage(driver)
        assert forecast_page.is_forecast_displayed(), (
            "Прогноз погоды по координатам не отображается."
        )


@allure.feature("UI Tests")
@allure.story("Check Current Temperature Display")
def test_current_temperature_display(driver):
    """
    Тест на проверку отображения текущей температуры на главной странице.
    """
    with allure.step("Открытие главной страницы"):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

    with allure.step("Проверка отображения текущей температуры"):
        assert home_page.is_current_temperature_displayed(), (
            "Текущая температура не отображается."
        )


@allure.feature("UI Tests")
@allure.story("Search Weather for Non-Existent City")
def test_search_weather_for_non_existent_city(driver):
    """
    Тест на проверку вывода ошибки
    при поиске погоды для несуществующего города.
    """
    non_existent_city = "NonExistentCity"

    with allure.step("Открытие главной страницы"):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)

    with allure.step("Поиск погоды для несуществующего города "
                     f"'{non_existent_city}'"):
        home_page.search_city(non_existent_city)

    with allure.step("Проверка отображения сообщения об ошибке"):
        error_message = home_page.get_error_message()
        expected_message = f"No results for {non_existent_city}"
        assert expected_message in error_message, (
            f"Ожидалось сообщение об ошибке '{expected_message}', "
            f"но получено: {error_message}"
        )
