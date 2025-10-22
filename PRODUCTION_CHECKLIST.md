# 🚀 Production Deployment Checklist

Before deploying ease-E-movies to production, complete this checklist to ensure security and performance.

## ✅ Security Settings

### 1. Environment Variables
- [ ] Set `DEBUG=False` in `.env`
- [ ] Generate new `SECRET_KEY` (50+ characters, random)
- [ ] Set `DATABASE_URL` for PostgreSQL
- [ ] Verify all API keys are set correctly
- [ ] Remove any test/development credentials

### 2. Django Settings (settings.py)

Add these settings for production:

```python
# Security Settings for Production
if not DEBUG:
    # HTTPS Settings
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # HSTS Settings
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Update ALLOWED_HOSTS
    ALLOWED_HOSTS = [
        'yourdomain.com',
        'www.yourdomain.com',
    ]
```

### 3. Secret Key Generation

Generate a new secret key:

```python
# In Python shell
import secrets
print(secrets.token_urlsafe(50))
```

Or use Django's built-in:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

---

## 🗄️ Database

### PostgreSQL Setup
- [ ] Create production database
- [ ] Set up database user with appropriate permissions
- [ ] Configure `DATABASE_URL` in environment
- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`

### Backup Strategy
- [ ] Set up automated database backups
- [ ] Test backup restoration process
- [ ] Document backup procedures

---

## 📦 Static Files

### Collection
```bash
python manage.py collectstatic --noinput
```

### CDN (Optional but Recommended)
- [ ] Set up CDN for static files
- [ ] Configure `STATIC_URL` to point to CDN
- [ ] Test static file loading

---

## 🔧 Server Configuration

### Web Server (Nginx/Apache)
- [ ] Configure reverse proxy
- [ ] Set up SSL certificate (Let's Encrypt recommended)
- [ ] Configure static file serving
- [ ] Set up gzip compression
- [ ] Configure caching headers

### Application Server (Gunicorn/uWSGI)
- [ ] Install application server
- [ ] Configure workers (2-4 × CPU cores)
- [ ] Set up process management (systemd/supervisor)
- [ ] Configure logging

### Example Gunicorn Configuration:
```bash
gunicorn moviedatabase.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 60 \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log
```

---

## 🚀 Performance

### Caching
- [ ] Consider Redis for production caching
- [ ] Configure cache backend in settings
- [ ] Set appropriate cache timeouts

### Redis Setup (Optional):
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Database Optimization
- [ ] Add database indexes for frequently queried fields
- [ ] Use `select_related()` and `prefetch_related()` in views
- [ ] Monitor slow queries
- [ ] Set up connection pooling

---

## 📊 Monitoring & Logging

### Logging
- [ ] Configure production logging
- [ ] Set up log rotation
- [ ] Monitor error logs
- [ ] Set up error alerting (Sentry, etc.)

### Monitoring
- [ ] Set up uptime monitoring
- [ ] Configure performance monitoring
- [ ] Monitor database performance
- [ ] Track API rate limits

### Recommended Tools:
- **Error Tracking**: Sentry, Rollbar
- **Uptime Monitoring**: UptimeRobot, Pingdom
- **Performance**: New Relic, DataDog
- **Logs**: Papertrail, Loggly

---

## 🔐 API Keys & Rate Limits

### TMDb API
- [ ] Verify API key is valid
- [ ] Monitor rate limits (40 requests per 10 seconds)
- [ ] Implement rate limiting if needed
- [ ] Set up fallback for rate limit errors

### OMDb API
- [ ] Verify API key is valid
- [ ] Check daily request limit
- [ ] Monitor usage

### Trakt API
- [ ] Verify credentials are valid
- [ ] Monitor rate limits
- [ ] Implement OAuth if needed

---

## 🧪 Testing

### Pre-Deployment Tests
- [ ] Run all tests: `python manage.py test`
- [ ] Check for security issues: `python manage.py check --deploy`
- [ ] Test all critical user flows
- [ ] Test on multiple browsers
- [ ] Test mobile responsiveness
- [ ] Load testing (optional)

### Post-Deployment Tests
- [ ] Verify homepage loads
- [ ] Test movie search
- [ ] Test movie details page
- [ ] Test series pages
- [ ] Verify admin panel access
- [ ] Check static files loading
- [ ] Test API integrations

---

## 🌐 Domain & DNS

### Domain Setup
- [ ] Configure domain DNS
- [ ] Set up A/CNAME records
- [ ] Configure SSL certificate
- [ ] Test domain resolution

### SSL Certificate
- [ ] Install SSL certificate
- [ ] Configure auto-renewal
- [ ] Test HTTPS access
- [ ] Verify SSL rating (SSLLabs)

---

## 📱 Additional Considerations

### Email Configuration (if needed)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

### CORS (if needed for API)
```bash
pip install django-cors-headers
```

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
]
```

---

## 🔄 Deployment Process

### Initial Deployment
1. Set up server and install dependencies
2. Clone repository
3. Create virtual environment
4. Install Python packages
5. Configure environment variables
6. Set up database
7. Run migrations
8. Collect static files
9. Configure web server
10. Start application server
11. Test deployment

### Updates/Redeployment
1. Pull latest code
2. Activate virtual environment
3. Install new dependencies (if any)
4. Run migrations
5. Collect static files
6. Restart application server
7. Clear cache
8. Test changes

---

## 📋 Environment Variables Template

Create a `.env.production` file:

```env
# Production Environment Configuration

# Django Settings
DEBUG=False
SECRET_KEY=your-super-secret-key-here-50-plus-characters
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@host:port/database

# API Keys
TMDB_API_KEY=your_production_key
OMDB_API_KEY=your_production_key
TRAKT_CLIENT_ID=your_production_id
TRAKT_CLIENT_SECRET=your_production_secret

# Email (if needed)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Redis (if using)
REDIS_URL=redis://127.0.0.1:6379/1

# Sentry (if using)
SENTRY_DSN=your_sentry_dsn
```

---

## 🎯 Performance Targets

### Page Load Times
- Homepage: < 2 seconds
- Movie Details: < 1.5 seconds
- Search Results: < 2 seconds

### Uptime
- Target: 99.9% uptime
- Monitor and alert on downtime

### API Response Times
- TMDb API: < 500ms
- Database queries: < 100ms

---

## 🆘 Rollback Plan

### If Deployment Fails
1. Keep previous version accessible
2. Document rollback procedure
3. Test rollback in staging
4. Have database backup ready

### Quick Rollback Steps
```bash
# Revert to previous version
git checkout previous-tag
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

---

## ✅ Final Checklist

Before going live:

- [ ] All security settings configured
- [ ] Database backed up
- [ ] Static files collected
- [ ] SSL certificate installed
- [ ] Domain configured
- [ ] Monitoring set up
- [ ] Error tracking configured
- [ ] All tests passing
- [ ] Performance tested
- [ ] Rollback plan documented
- [ ] Team notified
- [ ] Documentation updated

---

## 📞 Support & Maintenance

### Regular Maintenance
- [ ] Weekly: Check error logs
- [ ] Weekly: Monitor performance
- [ ] Monthly: Update dependencies
- [ ] Monthly: Review security
- [ ] Quarterly: Database optimization
- [ ] Yearly: SSL certificate renewal

### Emergency Contacts
- Server provider support
- Database administrator
- Development team lead
- DevOps engineer

---

## 🎉 Post-Deployment

After successful deployment:

1. Monitor for 24-48 hours
2. Check error logs regularly
3. Monitor performance metrics
4. Gather user feedback
5. Document any issues
6. Plan next iteration

---

**Remember**: Always test in a staging environment before deploying to production!

**Good luck with your deployment! 🚀**