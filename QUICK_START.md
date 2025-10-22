# 🎬 ease-E-movies - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd ease-E-movies
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
- Copy `.env.example` to `.env` (if exists) or use the existing `.env`
- Update API keys if needed

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser (for admin access)**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

---

## 🗄️ Database Configuration

### Local Development (SQLite)
The app uses SQLite by default. No additional configuration needed!

### Production (PostgreSQL)
1. Uncomment `DATABASE_URL` in `.env`
2. Set your PostgreSQL connection string:
```env
DATABASE_URL=postgresql://user:password@host:port/database
```

---

## 🔑 API Keys

The application uses the following APIs:

### TMDb (The Movie Database)
- **Purpose**: Movie and TV show data
- **Get your key**: https://www.themoviedb.org/settings/api
- **Set in .env**: `TMDB_API_KEY=your_key_here`

### OMDb (Open Movie Database)
- **Purpose**: Additional movie information
- **Get your key**: http://www.omdbapi.com/apikey.aspx
- **Set in .env**: `OMDB_API_KEY=your_key_here`

### Trakt
- **Purpose**: TV series tracking
- **Get your credentials**: https://trakt.tv/oauth/applications
- **Set in .env**: 
  - `TRAKT_CLIENT_ID=your_id_here`
  - `TRAKT_CLIENT_SECRET=your_secret_here`

---

## 📁 Project Structure

```
ease-E-movies/
├── moviedb/                    # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin configuration
│   ├── utils.py               # Utility functions (NEW!)
│   ├── templates/             # HTML templates
│   └── static/                # Static files
│       ├── css/               # Stylesheets (NEW!)
│       │   ├── base.css
│       │   └── navigation.css
│       └── js/                # JavaScript (NEW!)
│           └── main.js
├── moviedatabase/             # Project settings
│   ├── settings.py            # Configuration
│   ├── urls.py                # Root URL config
│   └── wsgi.py                # WSGI config
├── .env                       # Environment variables
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
└── db.sqlite3                 # SQLite database (local)
```

---

## 🎨 Features

### For Users
- ✅ Browse movies by genre
- ✅ Search movies and TV series
- ✅ View detailed information
- ✅ Responsive design (mobile-friendly)
- ✅ Fast loading with caching
- ✅ Smooth animations and transitions

### For Admins
- ✅ Enhanced admin panel
- ✅ Visual poster previews
- ✅ Advanced filtering and search
- ✅ Bulk operations
- ✅ Organized fieldsets

---

## 🛠️ Common Commands

### Development
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (SQLite only)
# Delete db.sqlite3 and run migrate again
```

### Admin
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

### Static Files
```bash
# Collect static files (for production)
python manage.py collectstatic
```

### Cache
```bash
# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
>>> exit()
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'dotenv'"
**Solution:**
```bash
pip install python-dotenv
```

### Issue: "No module named 'requests'"
**Solution:**
```bash
pip install requests
```

### Issue: Database errors
**Solution:**
```bash
# Delete database and start fresh
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Static files not loading
**Solution:**
```bash
# Make sure DEBUG=True in .env for development
# Run collectstatic for production
python manage.py collectstatic --noinput
```

### Issue: API requests failing
**Solution:**
- Check your internet connection
- Verify API keys in `.env`
- Check API rate limits
- Review `debug.log` for errors

---

## 📊 Performance Tips

### Development
1. Keep `DEBUG=True` in `.env`
2. Use SQLite for faster setup
3. Cache is enabled by default

### Production
1. Set `DEBUG=False`
2. Use PostgreSQL for better performance
3. Run `collectstatic` before deployment
4. Consider using Redis for caching
5. Enable HTTPS
6. Set proper `ALLOWED_HOSTS`

---

## 🔒 Security Checklist

Before deploying to production:

- [ ] Set `DEBUG=False`
- [ ] Change `SECRET_KEY` in settings.py
- [ ] Update `ALLOWED_HOSTS`
- [ ] Use environment variables for all secrets
- [ ] Enable HTTPS
- [ ] Set up proper database backups
- [ ] Review and update CORS settings if needed
- [ ] Enable Django security middleware
- [ ] Set secure cookie settings

---

## 📚 Additional Resources

### Documentation
- Django: https://docs.djangoproject.com/
- TMDb API: https://developers.themoviedb.org/
- Python: https://docs.python.org/

### Improvements Documentation
- See `IMPROVEMENTS.md` for detailed list of all improvements
- Check inline code comments for specific functionality

---

## 🤝 Getting Help

### Check Logs
1. Console output (when running server)
2. `debug.log` file in project root
3. Browser console (F12) for JavaScript errors

### Common Log Locations
- Django errors: Console output
- API errors: `debug.log`
- JavaScript errors: Browser console

---

## 🎯 Quick Tips

1. **Admin Panel**: Access at `/admin/` with superuser credentials
2. **API Caching**: Responses cached for 1 hour by default
3. **Mobile Menu**: Click hamburger icon on mobile devices
4. **Search**: Use the search bar in navigation
5. **Lazy Loading**: Images load as you scroll for better performance

---

## 📝 Environment Variables Reference

```env
# Required
DEBUG=True                          # True for dev, False for production
TMDB_API_KEY=your_key              # TMDb API key

# Optional (have defaults)
OMDB_API_KEY=your_key              # OMDb API key
TRAKT_CLIENT_ID=your_id            # Trakt client ID
TRAKT_CLIENT_SECRET=your_secret    # Trakt client secret

# Production Only
DATABASE_URL=postgresql://...       # PostgreSQL connection string
```

---

## 🚀 Deployment

### Vercel / Heroku / Railway
1. Set environment variables in platform dashboard
2. Uncomment `DATABASE_URL` for PostgreSQL
3. Run migrations: `python manage.py migrate`
4. Collect static files: `python manage.py collectstatic`

### Traditional Server
1. Set up virtual environment
2. Install dependencies
3. Configure environment variables
4. Set up Gunicorn/uWSGI
5. Configure Nginx/Apache
6. Set up SSL certificate

---

**Happy Coding! 🎬✨**

For detailed improvements and technical documentation, see `IMPROVEMENTS.md`