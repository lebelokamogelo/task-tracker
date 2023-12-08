import requests
import json

auth_token = 'ACCESS_TOKEN'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
}
data = {
    "title": "Testing",
    "description": "Testing the authentication",
    "completed": False,
    "priority": "Medium"
}

try:
    response = requests.post('http://localhost:8000/api/todos/', headers=headers, json=data)
    response.raise_for_status()

    if response.status_code == 200:
        try:
            result = response.json()
            print(result)
        except json.JSONDecodeError as json_err:
            print(f"JSON decoding error: {json_err}")
    elif response.status_code == 400:
        try:
            error_data = response.json()
            print("Validation errors:", error_data)
        except json.JSONDecodeError as json_err:
            print(f"JSON decoding error for validation errors: {json_err}")

except Exception as e:
    print(f"An error occurred: {e}")
