"""
API Quick Reference

## Authentication
POST   /api/v1/users/login/
POST   /api/v1/users/register/
POST   /api/v1/users/token/refresh/
GET    /api/v1/users/profile/

## Services
GET    /api/v1/services/list/          - List all services (paginated)
GET    /api/v1/services/{id}/          - Get single service
GET    /api/v1/services/manage/        - List user's services (mechanic only)
POST   /api/v1/services/manage/create/ - Create service (mechanic)
PATCH  /api/v1/services/manage/{id}/   - Update service (mechanic)
DELETE /api/v1/services/manage/{id}/   - Delete service (mechanic)

## Mechanic Applications
POST   /api/v1/applications/apply/     - Apply as mechanic
GET    /api/v1/applications/list/      - List applications (admin)
POST   /api/v1/applications/{id}/approve/ - Approve application (admin)
POST   /api/v1/applications/{id}/decline/ - Decline application (admin)

## Orders/Bookings
POST   /api/v1/orders/create/          - Create booking
GET    /api/v1/orders/history/         - Get user's bookings

## Reviews
POST   /api/v1/reviews/service/{id}/review/ - Create review
GET    /api/v1/reviews/service/{id}/reviews/ - Get reviews

## Chat
POST   /api/v1/chat/ask/               - Ask AI chatbot

## Health
GET    /health/                        - Health check endpoint

## Admin (Protected)
GET    /api/v1/users/admin/users/      - List all users
GET    /api/v1/users/admin/users/{id}/ - Get user details
PATCH  /api/v1/users/admin/users/{id}/ - Update user
DELETE /api/v1/users/admin/users/{id}/ - Delete user


## Example Requests

### Register
POST /api/v1/users/register/
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepass123",
  "confirm_password": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}

### Login
POST /api/v1/users/login/
{
  "email": "user@example.com",
  "password": "securepass123"
}

### Create Service (as mechanic)
POST /api/v1/services/manage/create/
Content-Type: multipart/form-data

{
  "service_name": "Oil Change",
  "description": "Professional oil change",
  "price": "45.00",
  "duration_of_service": "30 minutes",
  "sample_image": <image_file>
}

### Book Service (with PayPal)
POST /api/v1/orders/create/
{
  "service": 1,
  "paypal_transaction_id": "20J123456789ABC",
  "total_cost": "45.00",
  "scheduled_date": "2024-03-20",
  "location": "123 Main St, New York, NY"
}

### Create Review
POST /api/v1/reviews/service/1/review/
{
  "rating": 5,
  "comment": "Great service, very professional!"
}

### Chat with AI
POST /api/v1/chat/ask/
{
  "message": "How much does an oil change cost?"
}


## Response Codes
200 - OK
201 - Created
204 - No Content
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Server Error


## Authentication Header
Authorization: Bearer <access_token>
"""
