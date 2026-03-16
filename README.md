# Mobile Mechanic Service Marketplace

A full-stack web application connecting customers with mobile mechanics for quick, affordable vehicle services. Built with Django REST Framework and React.

## 🎯 Features

### For Customers
- ✅ Browse available mechanics and services
- ✅ View detailed service information with reviews
- ✅ Book services with PayPal integration
- ✅ Schedule appointments at preferred locations
- ✅ Track order history and status
- ✅ Leave reviews and ratings
- ✅ AI chatbot support

### For Mechanics
- ✅ Apply to become a mechanic
- ✅ Manage services and pricing
- ✅ View service requests/orders
- ✅ Track earnings and customer ratings
- ✅ Professional profile with reviews

### For Admins
- ✅ Approve/decline mechanic applications
- ✅ Manage users and permissions
- ✅ Monitor platform statistics
- ✅ Handle disputes and support

## 📋 Technology Stack

**Backend:**
- Django 5.2.12
- Django REST Framework 3.16.1
- PostgreSQL (production) / SQLite (development)
- OpenAI API (gpt-4o-mini)
- PayPal SDK

**Frontend:**
- React (Create React App)
- Redux Toolkit
- Axios
- React Router v6
- PayPal React Components

**DevOps:**
- Docker & Docker Compose
- Gunicorn (production server)
- Nginx (reverse proxy)
- AWS (deployment ready)

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- npm or yarn
- PostgreSQL 12+ (for production)

### Backend Setup

1. **Create virtual environment**
```bash
cd /workspace
python -m venv backend_venv
.\backend_venv\Scripts\activate  # Windows
source backend_venv/bin/activate  # macOS/Linux
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
Create `.env` in project root:
```
OPENAI_API_KEY=your_openai_key
PAYPAL_CLIENT_ID=your_paypal_sandbox_id
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Start server**
```bash
python manage.py runserver 8000
```

### Frontend Setup

1. **Install dependencies**
```bash
cd frontend
npm install
```

2. **Configure environment**
Create `.env` in `/frontend`:
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_PAYPAL_CLIENT_ID=your_paypal_sandbox_id
```

3. **Start development server**
```bash
npm start
```

## � API Keys Setup (For Professors & Students)

### OpenAI API Key (Required for AI Chat)

The chatbot works in **demo mode** without an API key, but for real AI responses:

1. **Get a Free OpenAI API Key**
   - Sign up: https://platform.openai.com/signup
   - Go to: https://platform.openai.com/account/api-keys
   - Click "Create new secret key"
   - Copy immediately and keep it secret!

2. **Add to .env**
   ```
   OPENAI_API_KEY=sk-proj-your_actual_key_here
   ```

3. **Restart Django server**
   ```bash
   python manage.py runserver 8000
   ```

**No budget?** Demo mode works fine - chatbot responds with keyword-based answers about bookings, pricing, services, etc.

**For Students:** GitHub Student Developers get $50/month OpenAI credit
- Apply: https://education.github.com/students

### PayPal Client ID (Optional - for payment testing)

1. Sign up: https://developer.paypal.com/
2. Create sandbox account
3. Copy Sandbox Client ID to `.env` files

---

## �📁 Project Structure

```
/workspace
├── manage.py
├── db.sqlite3
├── requirements.txt
├── ENV_SETUP.md
├── MOBILE_MECHANIC_IMPLEMENTATION_PLAN.md
│
├── backend/                    # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── users/                      # User authentication app
│   ├── models.py              # CustomUser model
│   ├── views.py               # Auth endpoints
│   ├── serializers.py
│   └── urls.py
│
├── services/                   # Services/mechanics listing
│   ├── models.py              # Service model
│   ├── views.py               # Service CRUD
│   ├── serializers.py
│   └── urls.py
│
├── applications/              # Mechanic applications
│   ├── models.py              # MechanicApplication
│   ├── views.py               # Apply/approve/decline
│   └── urls.py
│
├── orders/                     # Bookings & payments
│   ├── models.py              # Order model
│   ├── views.py               # Order creation
│   └── urls.py
│
├── reviews/                    # Service reviews
│   ├── models.py              # ServiceReview
│   ├── views.py               # Create/get reviews
│   └── urls.py
│
├── chat/                       # AI chatbot
│   ├── views.py               # OpenAI integration
│   └── urls.py
│
├── frontend/                   # React application
│   ├── public/
│   ├── src/
│   │   ├── screens/           # Page components
│   │   │   ├── HomeScreen
│   │   │   ├── SignIn/SignUp
│   │   │   ├── ServiceDetailScreen
│   │   │   ├── UserProfileScreen
│   │   │   ├── AdminScreen
│   │   │   ├── MechanicDashboardScreen
│   │   │   └── ...
│   │   │
│   │   ├── components/        # Reusable components
│   │   │   ├── Navbar
│   │   │   ├── Chatbot
│   │   │   ├── ErrorBoundary
│   │   │   ├── Loading
│   │   │   ├── Modal
│   │   │   └── ...
│   │   │
│   │   ├── actions/           # Redux async thunks
│   │   ├── reducers/          # Redux state management
│   │   ├── constants/         # Action type constants
│   │   ├── utils/             # Helper functions
│   │   └── axiosInstance.js   # HTTP client
│   │
│   ├── package.json
│   └── .env
│
└── backend_venv/              # Python virtual environment
```

## 🔧 API Endpoints

### Authentication
- `POST /api/v1/users/login/` - Login with email/password
- `POST /api/v1/users/register/` - Create new account
- `POST /api/v1/users/token/refresh/` - Refresh JWT token
- `GET /api/v1/users/profile/` - Get logged-in user profile

### Services
- `GET /api/v1/services/list/` - List all services
- `GET /api/v1/services/{id}/` - Get service details
- `GET /api/v1/services/manage/` - List user's services (mechanics)
- `POST /api/v1/services/manage/create/` - Create new service
- `PATCH /api/v1/services/manage/{id}/` - Update service
- `DELETE /api/v1/services/manage/{id}/` - Delete service

### Applications
- `POST /api/v1/applications/apply/` - Apply as mechanic
- `GET /api/v1/applications/list/` - List applications (admin)
- `POST /api/v1/applications/{id}/approve/` - Approve application
- `POST /api/v1/applications/{id}/decline/` - Decline application

### Orders
- `POST /api/v1/orders/create/` - Create booking order
- `GET /api/v1/orders/history/` - Get user's orders

### Reviews
- `POST /api/v1/reviews/service/{id}/review/` - Create review
- `GET /api/v1/reviews/service/{id}/reviews/` - Get service reviews

### Chat
- `POST /api/v1/chat/ask/` - Chat with AI support

## 🔐 Authentication

The application uses JWT (JSON Web Tokens) for authentication:

1. User logs in with email/password
2. Backend returns `access_token` and `refresh_token`
3. Token stored in localStorage
4. All requests include: `Authorization: Bearer <token>`
5. Token auto-refreshes when expired
6. 401 responses redirect to login

## 💳 Payment Integration

PayPal integration for service payments:

1. User books service and selects PayPal
2. PayPal button appears on checkout
3. User approves payment in PayPal popup
4. Transaction ID returned to backend
5. Order created with status "pending"
6. Mechanic notified of new booking

## 🤖 AI Chatbot

OpenAI gpt-4o-mini powers the AI chatbot:

- Constrained to mobile mechanic service topics
- Helps with booking questions
- Service information
- Account help
- Floating widget on all pages

## 📊 Database Schema

### CustomUser
```
- id (PK)
- email (unique, USERNAME_FIELD)
- username
- password
- role (user/mechanic/admin)
- merchant_id (for PayPal)
- created_at, updated_at
```

### Service
```
- id (PK)
- mechanic (FK → CustomUser)
- service_name
- description
- price
- duration
- image
- rating (avg from reviews)
- created_at, updated_at
```

### Order
```
- id (PK)
- customer (FK → CustomUser)
- service (FK → Service)
- paypal_transaction_id (unique)
- total_cost
- scheduled_date
- location
- status (pending/completed/cancelled)
- date_purchased
```

### ServiceReview
```
- id (PK)
- service (FK → Service)
- reviewer (FK → CustomUser)
- rating (1-5)
- comment
- created_at
```

## 🧪 Testing

### Backend Tests
```bash
python manage.py test
```

### API Tests
```bash
python test_api.py
```

## 📝 User Roles & Permissions

| Action | User | Mechanic | Admin |
|--------|------|----------|-------|
| Browse services | ✅ | ✅ | ✅ |
| Book service | ✅ | ❌ | ❌ |
| Create service | ❌ | ✅ | ✅ |
| Apply as mechanic | ✅ | ❌ | ❌ |
| Approve applications | ❌ | ❌ | ✅ |
| View all users | ❌ | ❌ | ✅ |
| Delete users | ❌ | ❌ | ✅ |

## 🚢 Production Deployment

### Docker Setup
```bash
docker-compose up -d
```

### Environment Variables
Create `.env.production`:
```
DJANGO_SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@host/db
OPENAI_API_KEY=production_key
PAYPAL_CLIENT_ID=production_id
```

### AWS Deployment
1. Push to ECR
2. Deploy with ECS/EKS
3. Configure RDS PostgreSQL
4. Set up CloudFront CDN
5. Configure domain with Route53

## 🐛 Troubleshooting

### Common Issues

**CORS Errors**
- Check `CORS_ALLOWED_ORIGINS` in settings.py
- Ensure frontend URL matches

**JWT Token Issues**
- Clear browser cache and localStorage
- Check token expiration time
- Verify SECRET_KEY in production

**PayPal Sandbox Issues**
- Use correct sandbox Client ID
- Ensure redirect URLs are configured
- Test buyer/seller accounts

**Database Issues**
- Run `python manage.py migrate`
- Check database credentials
- Verify database is running

## 📚 Additional Resources

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [React Router Docs](https://reactrouter.com/)
- [PayPal Integration Guide](https://developer.paypal.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)

## 📄 License

This project is proprietary and confidential.

## 👥 Support

For issues and questions, contact support@mobilemechanic.app

---

**Version:** 1.0.0  
**Last Updated:** March 2026  
**Status:** Production Ready ✅
