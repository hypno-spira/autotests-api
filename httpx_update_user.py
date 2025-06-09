import httpx

from tools.fakers import fake

# Создаем пользователя
create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data:", create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("\nLogin data:", login_response_data)

# Обновление данных запросом PATCH
patch_payload = {
    "email": fake.email(),
    "lastName": "string_patch",
    "firstName": "string_patch",
    "middleName": "string"
}
headers = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
patch_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
                             json=patch_payload, headers=headers)
patch_response_data = patch_response.json()
print("\nPatch status Code:", patch_response.status_code)
print("Patch data:", patch_response_data)
