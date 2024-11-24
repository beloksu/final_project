from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException


class HomePage:
    def __init__(self, driver):
        """
        Инициализирует главную страницу.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        """
        Открывает указанную страницу.

        :param url: URL страницы.
        :type url: str
        """
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def search_city(self, city_name: str) -> None:
        """
        Ищет погоду по указанному городу.

        :param city_name: Название города.
        :type city_name: str
        """
        with allure.step(f"Ввод города '{city_name}' в строку поиска"):
            search_field = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Search city']"))
            )
            search_field.clear()
            search_field.send_keys(city_name)
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Search')]"))).click()

    def go_to_api_docs(self) -> None:
        """
        Переходит в раздел документации API.

        :return: None
        """
        with allure.step("Переход в раздел документации API"):
            self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "API"))
            ).click()

    def is_api_docs_page_opened(self) -> bool:
        """
        Проверяет, открылась ли страница документации API.

        :return: True, если страница открылась, иначе False.
        :rtype: bool
        """
        with allure.step("Проверка открытия страницы документации API"):
            return "api" in self.driver.current_url.lower()

    def search_by_coordinates(self, latitude: float, longitude: float) -> None:
        """
        Ищет погоду по координатам.

        :param latitude: Широта.
        :type latitude: float
        :param longitude: Долгота.
        :type longitude: float
        """
        with allure.step("Поиск погоды по координатам: "
                         f"широта {latitude}, долгота {longitude}"):
            self.driver.execute_script(
                (f"window.location.href='/?lat={latitude}&lon={longitude}'")
            )

    def is_current_temperature_displayed(self) -> bool:
        """
        Проверяет, отображается ли текущая температура на главной странице.

        :return: True, если температура отображается, иначе False.
        :rtype: bool
        """
        with allure.step("Проверка отображения блока с текущей температурой"):
            try:
                self.wait.until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "current-temp"))
                )
                return True
            except TimeoutException:
                return False

    def get_error_message(self) -> str:
        """
        Получает сообщение об ошибке, если город не найден.

        :return: Текст сообщения об ошибке.
        :rtype: str
        """
        with allure.step("Получение сообщения об ошибке"):
            try:
                error_message_element = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div.widget-notification span"))
                )
                return error_message_element.text
            except TimeoutException:
                return ""
