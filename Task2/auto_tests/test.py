import requests



# Базовый URL API (можно вынести в config.py)
BASE_URL = "https://qa-internship.avito.com/api/1/item"

def test_get_existing_item():
    """
    Тест-кейс: Запрос объявления по существующему id
    """

    # 📌 Входные данные
    item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"
    
    # 📌 1. Отправка GET-запроса
    response = requests.get(f"{BASE_URL}/{item_id}")
    
    # 📌 2. Проверка статус-кода
    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
    
    # 📌 3. Проверка тела ответа
    json_data = response.json()
    
    assert "id" in json_data, "В ответе нет ключа 'id'"
    assert json_data["id"] == item_id, f"ID в ответе {json_data['id']} не совпадает с запрошенным {item_id}"
    
    assert "name" in json_data, "Отсутствует поле 'name'"
    assert "price" in json_data, "Отсутствует поле 'price'"
    
    print("✅ Тест успешно пройден!")

