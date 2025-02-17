import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"

# Тестовые данные
valid_item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"
invalid_item_id = "7a8fe969-2a57-468e-82c9-1982d22023c6"
incorrect_item_id = "23456277"
empty_item_id = ""
valid_seller_id = "3452"
invalid_seller_id = "563276234"
incorrect_seller_id = "err332"
negative_seller_id = "-3452"
zero_seller_id = "0"

new_item_data = {
    "name": "Наушники",
    "price": 17500,
    "sellerId": 359176,
    "contacts": 16,
    "like": 50,
    "viewCount": 45
}

negative_price_item = {
    "name": "Бутылка",
    "price": -500,
    "sellerId": 656565,
    "contacts": 50,
    "like": 50,
    "viewCount": 50
}

negative_seller_item = {
    "name": "Шляпа",
    "price": 500,
    "sellerId": -656565,
    "contacts": 50,
    "like": 50,
    "viewCount": 50
}

empty_name_item = {
    "name": "",
    "price": 5000,
    "sellerId": 12345,
    "contacts": 10,
    "like": 5,
    "viewCount": 100
}

negative_values_item = {
    "name": "Ноутбук",
    "price": -40000,
    "sellerId": -345678,
    "contacts": -100,
    "like": -100,
    "viewCount": -100
}

@pytest.mark.parametrize("item_id, expected_status", [
    (valid_item_id, 200),
    (invalid_item_id, 404),
    (incorrect_item_id, 400),
    (empty_item_id, 400),
])
def test_get_item_by_id(item_id, expected_status):
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    assert response.status_code == expected_status


@pytest.mark.parametrize("seller_id, expected_status, expected_response", [
    (valid_seller_id, 200, True),
    (invalid_seller_id, 200, False),
    (incorrect_seller_id, 400, False),
    (negative_seller_id, 400, False),  # Failed test
    (zero_seller_id, 400, False),  # Failed test
])
def test_get_items_by_seller_id(seller_id, expected_status, expected_response):
    response = requests.get(f"{BASE_URL}/{seller_id}/item")
    assert response.status_code == expected_status

    if expected_response:
        assert isinstance(response.json(), list)
    else:
        assert "error" in response.json()


def test_create_valid_item():
    response = requests.post(f"{BASE_URL}/item", json=new_item_data)
    assert response.status_code == 200
    assert "id" in response.json()


@pytest.mark.parametrize("item_data, expected_status", [
    (negative_price_item, 400),  # Failed test
    (negative_seller_item, 400),  # Failed test
    (empty_name_item, 400),  # Failed test
    (negative_values_item, 400),  # Failed test
])
def test_create_invalid_items(item_data, expected_status):
    response = requests.post(f"{BASE_URL}/item", json=item_data)
    assert response.status_code == expected_status
