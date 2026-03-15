# Примерны тестов по API
import time
import pytest
import requests
import allure

BASE_URL = "https://httpbin.org/"
BEARER_TOKEN = "bearer_token_123"

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.title("GET запрос с параметрами page и limit")
@allure.suite("API тесты")
def test_api_get():
    response = requests.get(f"{BASE_URL}get?page=2&limit=50")
    assert response.status_code == 200
    assert response.json()["args"]["page"] == '2'
    assert response.json()["args"]["limit"] == '50'

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.title("POST запрос с JSON данными")
@allure.suite("API тесты")
def test_api_post():
    response = requests.post(
        f"{BASE_URL}post",
            json={"name": "John", "age": 30}
            )
    assert response.status_code == 200
    assert response.json()["json"]["name"] == 'John'
    assert response.json()["json"]["age"] == 30
    assert response.headers["content-type"] == "application/json"

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.title("Отправка кастомного заголовка X-Test-Header")
@allure.suite("API тесты")
def test_api_headers():
    response = requests.get(f"{BASE_URL}headers", headers={"X-Test-Header": "HelloWorld"})
    assert response.status_code == 200
    assert response.json()["headers"]["X-Test-Header"] == "HelloWorld"

@allure.title("Проверка статус кодов ответа: {api} -> {code}")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.suite("API тесты")
@pytest.mark.parametrize("api, code", [
    ("status/404", 404),
    ("status/500", 500),
])
def test_api_status_codes(api, code):
    assert requests.get(f"{BASE_URL}{api}").status_code == code

@allure.title("Тест с задержкой ответа (delay 3 секунды)")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.suite("API тесты")
def test_api_delay():
    start = time.perf_counter()
    response = requests.get(f"{BASE_URL}delay/3", timeout=10)
    end = time.perf_counter()
    assert end - start < 5
    assert response.status_code == 200

@allure.title("Базовая аутентификация (Basic Auth)")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.suite("API тесты")
def test_api_auth():
    response = requests.get(f"{BASE_URL}/basic-auth/john/12345", auth=("john", "12345"))
    assert response.status_code == 200
    assert response.json()["authenticated"] == True
    assert response.json()["user"] == "john"

@allure.title("Аутентификация с Bearer токеном")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@allure.suite("API тесты")
def test_bearer_auth():
    response = requests.get(f"{BASE_URL}/bearer", headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
    assert response.status_code == 200
    assert response.json()["authenticated"] == True
    assert response.json()["token"] == BEARER_TOKEN




