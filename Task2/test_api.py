import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1/item"

@pytest.mark.parametrize("item_id, expected_status, expected_keys", [
    # TC-01: Успешное получение объявления
    ("7a8fe969-2a57-468e-82c9-1982d22023c5", 200, ["id", "name", "price", "sellerId", "statistics"]),
    
    # TC-02: Запрос с несуществующим ID
    ("invalid-id-123", 404, ["message", "code"]),
    
    # TC-03: Запрос с некорректным ID (не UUID)
    ("!@#$%^&*", 400, ["message", "code"]),
    
    # TC-04: Запрос без ID
    ("", 400, ["message", "code"])
])
def test_get_item(item_id, expected_status, expected_keys):
    """Тест проверяет различные сценарии работы GET /api/1/item/:id"""
    
    url = f"{BASE_URL}/{item_id}" if item_id else BASE_URL
    response = requests.get(url)
    
    # Проверка статус-кода
    assert response.status_code == expected_status, f"Ошибка: Ожидался {expected_status}, получен {response.status_code}"
    
    # Проверка структуры JSON-ответа
    response_json = response.json()
    for key in expected_keys:
        assert key in response_json, f"Ошибка: В ответе отсутствует ключ '{key}'"
