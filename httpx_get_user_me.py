import httpx

login_payload = {
    "email": "mikka@mik.ka",
    "password": "mikka123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Status code: ", login_response.status_code)
print("Login response: ", login_response_data)

access_token = login_response_data["token"]["accessToken"]

print("---" * 12)
print("Получен токен: Bearer", access_token)
print("---" * 12)
print("Получаем данные о пользователе...")
print()

header_user = {
    "Authorization": f"Bearer {access_token}"
}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=header_user)
print("Status code: ", user_response.status_code)
print("User response: ", user_response.json())
