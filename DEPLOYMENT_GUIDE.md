# Deployment Guide

## 📦 Production Build

### Step 1: Prepare Backend

1. **Install production packages**
```bash
pip install gunicorn whitenoise psycopg2-binary
```

2. **Create production settings**
Create `backend/settings_prod.py`:
```python
from backend.settings import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

3. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

4. **Run migrations on production database**
```bash
python manage.py migrate --settings=backend.settings_prod
```

### Step 2: Build React

1. **Create production build**
```bash
cd frontend
npm run build
```

2. **Output is in `frontend/build/`**

### Step 3: Serve with Gunicorn

1. **Start Gunicorn**
```bash
gunicorn backend.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

2. **Behind Nginx (recommended)**
```nginx
upstream django {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    client_max_body_size 100M;

    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
    }

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }
}
```

## 🐳 Docker Deployment

1. **Create Dockerfile** (in project root)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
```

2. **Create docker-compose.yml**
```yaml
version: '3.9'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mechanic_db
      POSTGRES_USER: mechanic_user
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: .
    command: gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 4
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://mechanic_user:secure_password@db:5432/mechanic_db
      DEBUG: False
      OPENAI_API_KEY: your_key
      PAYPAL_CLIENT_ID: your_id
    depends_on:
      - db
    volumes:
      - media:/app/media

  frontend:
    image: node:16
    working_dir: /app/frontend
    volumes:
      - .:
      - /app/node_modules
    command: npm run build
    environment:
      REACT_APP_API_URL: http://localhost:8000

volumes:
  postgres_data:
  media:
```

3. **Run**
```bash
docker-compose up -d
```

## ☁️ AWS Deployment

### Option 1: Elastic Beanstalk

1. **Install EB CLI**
```bash
pip install awsebcli
```

2. **Initialize**
```bash
eb init -p python-3.11 mechanic-app
eb create mechanic-prod
```

3. **Deploy**
```bash
eb deploy
```

### Option 2: ECS Fargate

1. **Create ECR repository**
```bash
aws ecr create-repository --repository-name mechanic-app
```

2. **Build and push**
```bash
docker build -t mechanic-app .
docker tag mechanic-app:latest your-account.dkr.ecr.region.amazonaws.com/mechanic-app:latest
docker push your-account.dkr.ecr.region.amazonaws.com/mechanic-app:latest
```

3. **Create ECS task definition and service**

## 🔒 Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Enable HTTPS (SSL/TLS)
- [ ] Set secure CORS_ALLOWED_ORIGINS
- [ ] Use strong database password
- [ ] Enable database backups
- [ ] Set up CloudFront for static files
- [ ] Configure Web Application Firewall (WAF)
- [ ] Enable database encryption
- [ ] Set up DDoS protection
- [ ] Monitor logs and errors
- [ ] Regular security updates

## 🔄 CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build and push Docker image
        run: |
          docker build -t app:${{ github.sha }} .
          docker push registry.example.com/app:${{ github.sha }}
      
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster prod \
            --service mechanic-app \
            --force-new-deployment
```

## 📊 Monitoring & Logging

### CloudWatch
```bash
# Monitor logs
aws logs tail /aws/ecs/mechanic-app --follow
```

### Error Tracking (Sentry)
```python
# In settings.py
import sentry_sdk
sentry_sdk.init("your-sentry-dsn")
```

### Performance Monitoring
- Use NewRelic or DataDog
- Monitor database queries
- Track API response times
- Monitor error rates

## 🔧 Maintenance

### Database Backups
```bash
# PostgreSQL backup
pg_dump -U username -h host dbname > backup.sql

# Restore
psql -U username -h host dbname < backup.sql
```

### Log Rotation
```bash
# Configure logrotate for Django logs
/var/log/django/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
}
```

---

For more help, refer to [Django Deployment Docs](https://docs.djangoproject.com/en/5.2/howto/deployment/)
