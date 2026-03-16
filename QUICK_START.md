# 🚀 Quick Start Guide - 5 Minutes to Launch

## For Windows Users

### Step 1: Run Setup (1 minute)
```bash
cd /workspace
setup.bat
```

This automatically:
- Creates virtual environment
- Installs Python packages
- Installs Node packages
- Runs migrations

### Step 2: Configure Environment (1 minute)

Create `.env` file in `/workspace`:
```
OPENAI_API_KEY=sk-your-key-here
PAYPAL_CLIENT_ID=your-sandbox-client-id
DEBUG=True
```

Create `.env` file in `/workspace/frontend`:
```
REACT_APP_PAYPAL_CLIENT_ID=your-sandbox-client-id
```

### Step 3: Load Demo Data (1 minute)
```bash
python seed_test_data.py
```

Creates test accounts:
- Admin: admin@mechanic.app / admin123
- Customer: customer@example.com / customer123
- Mechanic: mechanic1@example.com / mechanic123

### Step 4: Start Backend (1 minute)
```bash
python manage.py runserver 8000
```

### Step 5: Start Frontend (1 minute)
```bash
cd frontend
npm start
```

**Then visit:** http://localhost:3000

---

## For macOS/Linux Users

### Step 1: Run Setup
```bash
cd /workspace
chmod +x setup.sh
./setup.sh
```

### Steps 2-5: Same as Windows above

---

## 🧪 Test the App

### Login as Customer
- Email: `customer@example.com`
- Password: `customer123`

Actions:
1. Browse services
2. Click service → "Proceed to Payment"
3. Click PayPal button (sandbox only, doesn't charge)
4. View booking in Profile

### Login as Mechanic
- Email: `mechanic1@example.com`
- Password: `mechanic123`

Actions:
1. Go to Dashboard
2. Create new service
3. Upload image
4. Edit/delete services

### Login as Admin
- Email: `admin@mechanic.app`
- Password: `admin123`

Actions:
1. Go to Admin Panel
2. View pending applications
3. Approve or decline with reason

---

## 📝 Key Features to Try

- [ ] Register new account
- [ ] Upload profile image
- [ ] Browse available services
- [ ] View service details & reviews
- [ ] Book service with fake PayPal
- [ ] View order history
- [ ] Chat with AI (💬 button)
- [ ] Apply as mechanic
- [ ] Create service (as mechanic)
- [ ] Approve application (as admin)

---

## 🔗 Important URLs

| Page | URL |
|------|-----|
| Home | http://localhost:3000 |
| Services | http://localhost:3000 |
| Sign In | http://localhost:3000/signin |
| Sign Up | http://localhost:3000/register |
| My Profile | http://localhost:3000/profile |
| Apply Mechanic | http://localhost:3000/apply-mechanic |
| Mechanic Dashboard | http://localhost:3000/mechanic/dashboard |
| Admin Panel | http://localhost:3000/admin |
| Backend API | http://localhost:8000 |
| Admin Panel (Django) | http://localhost:8000/admin |

---

## ⚠️ Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### Module Not Found
```bash
# Reinstall Python packages
pip install -r requirements.txt

# Reinstall Node packages
cd frontend && npm install
```

### Database Issues
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
python seed_test_data.py
```

### Clear Browser Cache
- DevTools → Application → localStorage → Clear all

---

## 📚 Full Documentation

For detailed info, see:
- `README.md` - Project overview
- `DEPLOYMENT_GUIDE.md` - Production setup
- `API_REFERENCE.md` - All API endpoints
- `ENV_SETUP.md` - Environment configuration
- `PROJECT_COMPLETION_REPORT.md` - Feature checklist

---

## 🎉 You're All Set!

The application is fully functional. All 5 stages completed.

**Happy testing!** 🚀
