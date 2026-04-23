import requests
import json

url = "http://localhost:8000/api/v1/auth/register"
data = {
    "email": "test_user123@example.com",
    "password": "password123"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Error: {e}")
