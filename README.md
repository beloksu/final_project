# OpenWeatherMap Tests

## Описание
Проект для автоматизированного тестирования сервиса OpenWeatherMap.

## Структура проекта
- `tests/`: Тесты (UI и API).
- `pages/`: Page Object классы для UI-тестов.
- `utils/`: Настройки и тестовые данные.
- `requirements.txt`: Зависимости.

## Установка
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt

## Команды
1. Запуск всех тестов:
   python3 -m pytest tests --alluredir=allure-results
2. Запуск только UI-тестов:
   python3 -m pytest tests/test_ui.py --alluredir=allure-results
3. Запуск только API-тестов:
   python3 -m pytest tests/test_api.py --alluredir=allure-results
4. Просмотр отчета:
   allure serve allure-results
