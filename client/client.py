import json

import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTAxNDI1LCJpYXQiOjE3MDU0OTk2MjUsImp0aSI6ImIzNTk2NjVhMjg3YzQxODhiYjIxYTZiMjdjOWEwZDJjIiwidXNlcl9pZCI6MX0.BDoPiLpngwGzbPNzxRRzE5NbVQhJuoDldvCdPGewbZc'
}

try:
    response = requests.get('http://localhost:8000/api/todos/', headers=headers)
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
