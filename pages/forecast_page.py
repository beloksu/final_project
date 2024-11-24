from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ForecastPage:
    def __init__(self, driver):
        """
        Инициализирует страницу прогноза.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_forecast_displayed(self) -> bool:
        """
        Проверяет, отображается ли прогноз погоды на странице.

        :return: True, если прогноз отображается, иначе False.
        :rtype: bool
        """
        with allure.step("Проверка отображения прогноза погоды"):
            forecast_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "current-temp"))
            )
            return forecast_element.is_displayed()
