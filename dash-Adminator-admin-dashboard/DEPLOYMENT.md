# Deployment Guide - Adminator Dash Dashboard

Complete instructions for deploying the Adminator Dash application to various hosting platforms.

## Table of Contents
1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [DigitalOcean Deployment](#digitalocean-deployment)
6. [Render Deployment](#render-deployment)

---

## Local Development

### Setup
```bash
# Clone or navigate to the project
cd dash-admin

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python index.py
```

Access the app at `http://localhost:8050`

---

## Docker Deployment

### 1. Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DASH_APP_NAME=adminator
ENV PORT=8050

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8050", "wsgi:app.server"]
```

### 2. Create .dockerignore
```
__pycache__
.git
.gitignore
.env
venv
.DS_Store
```

### 3. Build and Run
```bash
# Build image
docker build -t adminator-dash .

# Run container
docker run -p 8050:8050 adminator-dash

# Or with environment variables
docker run -e PORT=8050 -p 8050:8050 adminator-dash
```

### 4. Docker Compose (Optional)
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8050:8050"
    environment:
      - PORT=8050
      - DEBUG=False
```

Run with: `docker-compose up`

---

## Heroku Deployment

### 1. Install Heroku CLI
```bash
# macOS
brew install heroku/brew/heroku

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

### 2. Create Procfile
```
web: gunicorn --workers 4 --timeout 60 wsgi:app.server
```

### 3. Create runtime.txt
```
python-3.10.13
```

### 4. Deploy
```bash
# Login to Heroku
heroku login

# Create app
heroku create adminator-dash-app

# Set buildpacks
heroku buildpacks:add heroku/python

# Deploy
git push heroku main

# View logs
heroku logs --tail

# Open app
heroku open
```

### 5. Scale Processes (optional)
```bash
# Scale to 2 dynos
heroku ps:scale web=2

# View running processes
heroku ps
```

---

## AWS Deployment

### Option 1: AWS Elastic Beanstalk

#### 1. Install EB CLI
```bash
pip install awseb-cli-bundle
```

#### 2. Create .ebextensions/python.config
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: wsgi:app.server
```

#### 3. Create .ebextensions/django.config
```yaml
commands:
  01_migrate:
    command: "source /var/app/venv/*/bin/activate && gunicorn wsgi:app.server"
    leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: /var/app/current:$PYTHONPATH
```

#### 4. Initialize and Deploy
```bash
# Initialize
eb init -p python-3.10 adminator-dash

# Create environment and deploy
eb create adminator-dash-env
eb deploy

# Open in browser
eb open

# View logs
eb logs
```

### Option 2: AWS EC2

#### 1. Connect to Instance
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

#### 2. Setup Server
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx -y

# Clone repository
git clone your-repo-url
cd dash-admin

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Run with gunicorn
gunicorn --workers 4 --bind 0.0.0.0:8050 wsgi:app.server
```

#### 3. Setup Nginx Reverse Proxy
```nginx
# /etc/nginx/sites-available/default
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8050;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### 4. Setup SSL with Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## DigitalOcean Deployment

### 1. Create Droplet
- OS: Ubuntu 22.04 LTS
- Size: Basic ($5-6/month)

### 2. SSH into Droplet
```bash
ssh root@your-droplet-ip
```

### 3. Install Requirements
```bash
# Update system
apt update && apt upgrade -y

# Install Python and tools
apt install python3 python3-pip python3-venv git nginx certbot python3-certbot-nginx -y

# Clone your repository
git clone your-repo-url /app
cd /app/dash-admin
```

### 4. Setup Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### 5. Create Systemd Service
Create `/etc/systemd/system/adminator.service`:
```ini
[Unit]
Description=Adminator Dash Application
After=network.target

[Service]
User=root
WorkingDirectory=/app/dash-admin
ExecStart=/app/dash-admin/venv/bin/gunicorn --workers 4 --bind 0.0.0.0:8050 wsgi:app.server
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
systemctl daemon-reload
systemctl enable adminator
systemctl start adminator
systemctl status adminator
```

### 6. Setup Nginx
```bash
# Create Nginx config
cat > /etc/nginx/sites-available/adminator << 'EOF'
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8050;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
EOF

# Enable site
ln -s /etc/nginx/sites-available/adminator /etc/nginx/sites-enabled/

# Test config
nginx -t

# Restart Nginx
systemctl restart nginx
```

### 7. Setup SSL
```bash
certbot --nginx -d your-domain.com
```

---

## Render Deployment

### 1. Connect GitHub Repository
- Go to render.com
- Connect your GitHub account
- Select your repository

### 2. Create Web Service
- Service Type: Web Service
- Environment: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn --workers 4 wsgi:app.server`
- Plan: Free or Starter

### 3. Environment Variables
Set in Render dashboard:
```
PORT=10000
PYTHON_VERSION=3.10.0
```

### 4. Deploy
- Push to main branch
- Render automatically deploys
- Access at `https://your-service.onrender.com`

---

## Production Best Practices

1. **Use Environment Variables**
   ```python
   import os
   DEBUG = os.getenv('DEBUG', 'False') == 'True'
   PORT = os.getenv('PORT', 8050)
   ```

2. **Set Up Monitoring**
   - Use CloudWatch (AWS)
   - Use DataDog or New Relic
   - Monitor logs and performance

3. **Use a Content Delivery Network (CDN)**
   - CloudFront (AWS)
   - Cloudflare
   - Bunny CDN

4. **Set up SSL/HTTPS**
   - Let's Encrypt (free)
   - AWS Certificate Manager
   - Cloudflare

5. **Database for Persistence**
   - PostgreSQL
   - MongoDB
   - DynamoDB (AWS)

6. **Caching**
   - Redis (cache data)
   - Browser caching headers
   - CDN caching

7. **Load Balancing**
   - AWS Elastic Load Balancer
   - Nginx load balancing
   - Docker Swarm

---

## Performance Optimization

### 1. Minify Assets
```bash
pip install dash-minify
```

### 2. Enable Compression
In Nginx:
```nginx
gzip on;
gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss;
```

### 3. Use CDN for External Libraries
Update external stylesheets to use CDN URLs.

### 4. Database Query Optimization
- Use indexes
- Cache frequent queries
- Use pagination

### 5. Code Optimization
```bash
# Install profiling tools
pip install flask-debugtoolbar

# Run with profiler
python -m cProfile index.py
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port
lsof -i :8050

# Kill process
kill -9 PID
```

### Module Not Found
```bash
# Verify installation
pip list

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Gunicorn Worker Issues
```bash
# Check system resources
free -h
df -h

# Increase workers (but not too many)
gunicorn --workers 8 wsgi:app.server
```

### SSL Certificate Issues
```bash
# Renew certificate
certbot renew --dry-run

# Force renewal
certbot renew --force-renewal
```

---

## Monitoring & Logging

### View Application Logs
```bash
# Heroku
heroku logs --tail

# DigitalOcean systemd
journalctl -u adminator -f

# Docker
docker logs -f container-id
```

### Set Up Log Aggregation
- CloudWatch (AWS)
- Papertrail
- Sentry (error tracking)

---

## Scaling

### Horizontal Scaling
- Add load balancer
- Run multiple instances
- Use database for shared state

### Vertical Scaling
- Increase server resources
- Add more workers
- Optimize code

---

## References

- [Dash Deployment](https://dash.plotly.com/deployment)
- [Gunicorn Documentation](https://gunicorn.org/)
- [Heroku Python Deploy](https://devcenter.heroku.com/articles/getting-started-with-python)
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/)
- [DigitalOcean App Platform](https://docs.digitalocean.com/products/app-platform/)
- [Render Documentation](https://docs.render.com/)

---

**Last Updated:** March 2026
**Version:** 1.0
