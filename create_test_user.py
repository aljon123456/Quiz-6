#!/usr/bin/env python
import os
import django
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create a test user
try:
    user = User.objects.create_user(
        email='testuser@example.com',
        username='testuser',
        password='testpass123'
    )
    print(f"Created user: {user.email}")
except Exception as e:
    print(f"Error: {e}")

# Try to get all users
users = User.objects.all()
print(f"\nTotal users: {users.count()}")
for user in users:
    print(f"  - {user.email} ({user.username})")
