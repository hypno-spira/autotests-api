import httpx

# Данные для входа в систему
login_payload = {
    "email": "alena@example.com",
    "password": "alena"
}

# Выполняем POST запрос
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Вывод ответа
print("POST запрос /api/v1/authentication/login\nResponse:", login_response_data)
print("Status Code:", login_response.status_code)

# Получаем accessToken из ответа
access_token = login_response_data["token"]["accessToken"]
print("Получен accessToken:", access_token)

# Выполняем GET запрос с accessToken в заголовке
headers = {"Authorization": f"Bearer {access_token}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
response_data = response.json()

# Вывод ответа
print("\nGET запрос /api/v1/users/me\nResponse:", response_data)
print("Status Code:", response.status_code)
