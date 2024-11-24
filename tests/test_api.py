import allure
import requests
from utils.environment import API_URL, API_KEY
from utils.test_data import CITY_NAME, LATITUDE, LONGITUDE


@allure.feature("API Tests")
@allure.story("Get Current Weather")
def test_get_current_weather():
    """
    Тест получения текущей погоды для города.
    """
    url = f"{API_URL}/weather"
    params = {"q": CITY_NAME, "appid": API_KEY}

    with allure.step("Отправка GET-запроса "
                     f"для текущей погоды в городе {CITY_NAME}"):
        response = requests.get(url, params=params)

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200, "Ожидался 200, "
        f"получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        json_data = response.json()
        assert "main" in json_data, "Ответ не содержит ключ 'main'."


@allure.feature("API Tests")
@allure.story("Hourly Forecast")
def test_hourly_forecast():
    """
    Тест получения почасового прогноза погоды.
    """
    url = f"{API_URL}/forecast"
    params = {"q": CITY_NAME, "appid": API_KEY}

    with allure.step("Отправка GET-запроса "
                     f"для почасового прогноза в городе {CITY_NAME}"):
        response = requests.get(url, params=params)

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200, "Ожидался 200, получен "
        f"{response.status_code}"

    with allure.step("Проверка структуры ответа"):
        json_data = response.json()
        assert "list" in json_data, "Ответ не содержит ключ 'list'."


@allure.feature("API Tests")
@allure.story("Air Pollution Data")
def test_air_pollution_data():
    """
    Тест получения данных о загрязнении воздуха.
    """
    url = f"{API_URL}/air_pollution"
    params = {"lat": LATITUDE, "lon": LONGITUDE, "appid": API_KEY}

    with allure.step("Отправка GET-запроса для получения данных о загрязнении "
                     f"воздуха по координатам ({LATITUDE}, {LONGITUDE})"):
        response = requests.get(url, params=params)

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200, "Ожидался 200, "
        f"получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        json_data = response.json()
        assert "list" in json_data, "Ответ не содержит ключ 'list'."
        if json_data["list"]:
            first_entry = json_data["list"][0]
            assert "main" in first_entry, "Элемент списка "
            "не содержит ключ 'main'."
            assert "components" in first_entry, "Элемент списка "
            "не содержит ключ 'components'."


@allure.feature("API Tests")
@allure.story("Get Current Weather by Coordinates")
def test_get_current_weather_by_coordinates():
    """
    Тест получения текущей погоды для города по координатам.
    """
    url = f"{API_URL}/weather"
    params = {"lat": LATITUDE, "lon": LONGITUDE, "appid": API_KEY}

    with allure.step("Отправка GET-запроса для текущей погоды "
                     f"по координатам ({LATITUDE}, {LONGITUDE})"):
        response = requests.get(url, params=params)

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200, "Ожидался 200, "
        f"получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        json_data = response.json()
        assert "main" in json_data, "Ответ не содержит ключ 'main'."
        assert "coord" in json_data, "Ответ не содержит ключ 'coord'."
        assert json_data["coord"]["lat"] == LATITUDE, "Широта в ответе "
        f"не совпадает с ожиданием: {LATITUDE}"
        assert json_data["coord"]["lon"] == LONGITUDE, "Долгота в ответе "
        f"не совпадает с ожиданием: {LONGITUDE}"


@allure.feature("API Tests")
@allure.story("Air Pollution Data with Invalid Coordinates")
def test_air_pollution_invalid_coordinates():
    """
    Тест получения данных о загрязнении воздуха с некорректными координатами.
    """
    url = f"{API_URL}/air_pollution"
    params = {"lat": 9999, "lon": 9999, "appid": API_KEY}

    with allure.step("Отправка GET-запроса для данных о загрязнении воздуха "
                     "с некорректными координатами (9999, 9999)"):
        response = requests.get(url, params=params)

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 400, "Ожидался 400, "
        f"получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        json_data = response.json()
        assert "message" in json_data, "Ответ не содержит ключ 'message'."
        assert json_data["message"] == "wrong latitude", "Сообщение об ошибке "
        "не соответствует ожидаемому."
