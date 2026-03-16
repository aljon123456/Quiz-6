import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from services.models import Service
from decimal import Decimal

User = get_user_model()

# Create test users
print("Creating test users...")

# Admin user
admin, _ = User.objects.get_or_create(
    email='admin@mechanic.app',
    defaults={
        'username': 'admin',
        'role': 'admin',
        'first_name': 'Admin',
        'last_name': 'User',
        'is_staff': True,
        'is_superuser': True,
    }
)
if _:
    admin.set_password('admin123')
    admin.save()
    print("✓ Created admin user: admin@mechanic.app")

# Regular customer
customer, _ = User.objects.get_or_create(
    email='customer@example.com',
    defaults={
        'username': 'johndoe',
        'role': 'user',
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '5551234567',
        'location': 'New York, NY',
        'gender': 'M',
    }
)
if _:
    customer.set_password('customer123')
    customer.save()
    print("✓ Created customer: customer@example.com")

# Mechanic users
mechanic1, _ = User.objects.get_or_create(
    email='mechanic1@example.com',
    defaults={
        'username': 'mike_mechanic',
        'role': 'mechanic',
        'first_name': 'Mike',
        'last_name': 'Johnson',
        'phone_number': '5559876543',
        'location': 'New York, NY',
        'gender': 'M',
        'merchant_id': 'MECHANIC001',
    }
)
if _:
    mechanic1.set_password('mechanic123')
    mechanic1.save()
    print("✓ Created mechanic 1: mechanic1@example.com")

mechanic2, _ = User.objects.get_or_create(
    email='mechanic2@example.com',
    defaults={
        'username': 'sarah_mechanic',
        'role': 'mechanic',
        'first_name': 'Sarah',
        'last_name': 'Williams',
        'phone_number': '5557654321',
        'location': 'New York, NY',
        'gender': 'F',
        'merchant_id': 'MECHANIC002',
    }
)
if _:
    mechanic2.set_password('mechanic123')
    mechanic2.save()
    print("✓ Created mechanic 2: mechanic2@example.com")

# Create test services
print("\nCreating test services...")

services_data = [
    {
        'mechanic': mechanic1,
        'name': 'Oil Change',
        'description': 'Professional oil change service for all vehicle types. Includes oil filter replacement.',
        'price': Decimal('45.00'),
        'duration': '30 minutes',
        'rating': Decimal('4.8'),
    },
    {
        'mechanic': mechanic1,
        'name': 'Tire Replacement',
        'description': 'Replace worn or damaged tires. We have a wide selection of quality tires.',
        'price': Decimal('120.00'),
        'duration': '1 hour',
        'rating': Decimal('4.9'),
    },
    {
        'mechanic': mechanic2,
        'name': 'Brake Service',
        'description': 'Complete brake inspection and service. Includes pad replacement and rotor resurfacing.',
        'price': Decimal('150.00'),
        'duration': '1.5 hours',
        'rating': Decimal('5.0'),
    },
    {
        'mechanic': mechanic2,
        'name': 'Battery Replacement',
        'description': 'Replace your vehicle battery with a quality replacement. Installation included.',
        'price': Decimal('80.00'),
        'duration': '30 minutes',
        'rating': Decimal('4.7'),
    },
    {
        'mechanic': mechanic1,
        'name': 'Air Filter Replacement',
        'description': 'Replace your vehicles air filter for improved performance.',
        'price': Decimal('30.00'),
        'duration': '20 minutes',
        'rating': Decimal('4.6'),
    },
]

for data in services_data:
    service, created = Service.objects.get_or_create(
        mechanic=data['mechanic'],
        service_name=data['name'],
        defaults={
            'description': data['description'],
            'price': data['price'],
            'duration_of_service': data['duration'],
            'rating': data['rating'],
        }
    )
    if created:
        print(f"✓ Created service: {data['name']}")

print("\n✓ Test data created successfully!")
print("\nTest Accounts:")
print("Admin:    admin@mechanic.app / admin123")
print("Customer: customer@example.com / customer123")
print("Mechanic: mechanic1@example.com / mechanic123")
print("Mechanic: mechanic2@example.com / mechanic123")
