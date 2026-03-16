# Environment Setup

## Backend (.env)

Create a `.env` file in the `/workspace` directory with your API keys:

```
OPENAI_API_KEY=sk-proj-your_actual_openai_api_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
PAYPAL_CLIENT_ID=your_paypal_sandbox_client_id
```

## Frontend (.env)

Create a `.env` file in the `/workspace/frontend` directory:

```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_PAYPAL_CLIENT_ID=your_paypal_sandbox_client_id
```

## Getting OpenAI API Key (STEP BY STEP)

### For Professors & Students:

1. **Sign Up/Login to OpenAI**
   - Go to: https://platform.openai.com/signup
   - Create account or sign in with existing account
   - Verify your email

2. **Create API Key**
   - Go to: https://platform.openai.com/account/api-keys
   - Click "Create new secret key"
   - Name it: "Mobile Mechanic Project"
   - Copy the key (starts with `sk-proj-`)
   - **⚠️ IMPORTANT: Copy it immediately - you won't be able to see it again!**

3. **Add to Environment**
   - Create `.env` file in workspace root
   - Add: `OPENAI_API_KEY=sk-proj-PASTE_YOUR_KEY_HERE`
   - Save file

4. **Restart Django Server**
   ```bash
   cd /workspace
   .\backend_venv\Scripts\python.exe manage.py runserver
   ```

5. **Test Chat Feature**
   - Go to http://localhost:3000
   - Login with test account
   - Open chat widget and test

### Free Trial Information

- **Free Credit:** OpenAI provides $5 free credit (expires after 3 months)
- **No Auto-Charge:** Requires explicit credit card to enable paid usage
- **Student Discount:** GitHub Student gives $50/month
- **Trial URL:** https://platform.openai.com/account/org-overview

### If No Budget/No Key Available

The chatbot will work in **Demo Mode** with keyword-based responses:
- Responds to questions about booking, pricing, mechanics, services, and payments
- No real AI, but fully functional
- Users can still interact with the application
- Perfect for demonstration purposes

---

## Getting PayPal Sandbox Client ID (Optional)

1. Go to https://developer.paypal.com/dashboard/
2. Create business sandbox account (free)
3. Go to "Apps & Credentials" → "Sandbox"
4. Copy Sandbox Client ID
5. Add to `.env` files

---

## Running the Application

### Backend
```bash
cd /workspace
.\backend_venv\Scripts\python.exe manage.py runserver 8000
```

### Frontend
```bash
cd /workspace/frontend
$env:PORT=3000; npm start
```

---

## Troubleshooting

**Chat says "Service temporarily unavailable"**
- Check if `OPENAI_API_KEY` is in `.env`
- Verify key starts with `sk-proj-`
- Check OpenAI account has no usage limits

**No changes when I update .env?**
- Restart Django server
- Restart React dev server
- Clear browser cache (Ctrl+Shift+Delete)

**Still getting 500 error?**
- Check terminal logs for exact error
- Verify API key is valid
- Try demo mode (works without key)
cd /workspace/frontend
npm install
npm start
```

Both servers should run on:
- Django: http://localhost:8000
- React: http://localhost:3000

## Database

SQLite database is auto-created at `/workspace/db.sqlite3` on first migration.

To reset database:
```bash
rm db.sqlite3
python manage.py migrate
python create_test_user.py
```
