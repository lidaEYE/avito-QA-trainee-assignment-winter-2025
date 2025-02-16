import requests
from config import BASE_URL, HEADERS

def get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    print(f"GET {url} -> {response.status_code}")  # Лог запроса
    return response

def post_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=data, headers=HEADERS)
    print(f"POST {url} | Data: {data} -> {response.status_code}")  # Лог запроса
    return response
