#!/usr/bin/env python
import os
import django
import requests
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

BASE_URL = 'http://localhost:8000'

# Test 1: Register a new user
print("Test 1: Register a new user")
register_data = {
    'email': 'newuser@example.com',
    'username': 'newuser',
    'first_name': 'Test',
    'last_name': 'User',
    'password': 'testpass123',
    'confirm_password': 'testpass123',
    'phone_number': '1234567890',
    'location': 'Test City',
    'gender': 'M',
}

try:
    response = requests.post(f'{BASE_URL}/api/v1/users/register/', json=register_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Login with registered user
print("\nTest 2: Login")
login_data = {
    'email': 'testuser@example.com',
    'password': 'testpass123',
}

try:
    response = requests.post(f'{BASE_URL}/api/v1/users/login/', json=login_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

# Test 3: Get user profile with token
print("\nTest 3: Get user profile (with token)")
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExMzU4NzU5LCJpYXQiOjE3MTEzNTUxNTksImp0aSI6IjQ0ZDkzMjY1NTZmOTQ2ODhhMGFjZTYwNWZlZTQzMzliIiwidXNlcl9pZCI6MSwiZW1haWwiOiJ0ZXN0dXNlckBleGFtcGxlLmNvbSIsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRfaWQiOm51bGwsInVzZXJuYW1lIjoidGVzdHVzZXIifQ.p-rM1Zb8yvN2X0K0L8q3M5N6O7P8Q9R0S1T2U3V4W5'
}

try:
    response = requests.get(f'{BASE_URL}/api/v1/users/profile/', headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
