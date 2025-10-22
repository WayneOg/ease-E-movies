# 🚀 Frontend Quick Start

Get the React frontend running in 5 minutes!

---

## ⚡ Quick Setup

### 1. Install Dependencies

```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm install
```

### 2. Start Django Backend (Terminal 1)

```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies
python manage.py runserver
```

### 3. Start React Frontend (Terminal 2)

```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm run dev
```

### 4. Open Browser

Visit: **http://localhost:3000**

---

## 🔧 Django CORS Setup (Required!)

The React app needs Django to allow cross-origin requests.

### Install CORS Package

```powershell
pip install django-cors-headers
```

### Update `moviedatabase/settings.py`

Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ... existing apps
    'corsheaders',
]
```

Add to `MIDDLEWARE` (at the top):
```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this
    'django.middleware.common.CommonMiddleware',
    # ... other middleware
]
```

Add CORS configuration:
```python
# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

---

## 📡 API Endpoints Needed

The React app expects these endpoints to return JSON:

### Required Endpoints

```
GET /movies/              - List all movies
GET /movie/<id>/          - Movie details
GET /series/              - List all series
GET /series/<id>/         - Series details
GET /search/?q=query      - Search movies/series
GET /trending/            - Trending movies
GET /popular/             - Popular movies
GET /top-rated/           - Top rated movies

# Genre endpoints
GET /action/              - Action movies
GET /comedy/              - Comedy movies
GET /horror/              - Horror movies
GET /scifi/               - Sci-Fi movies
GET /romance/             - Romance movies
GET /animation/           - Animation movies
```

### Example View (JSON Response)

```python
from django.http import JsonResponse
from .models import Movie

def movies_list(request):
    movies = Movie.objects.all()[:20]
    
    data = {
        'results': [
            {
                'id': movie.id,
                'title': movie.title,
                'poster_path': movie.poster_path,
                'backdrop_path': movie.backdrop_path,
                'overview': movie.overview,
                'vote_average': float(movie.vote_average) if movie.vote_average else 0,
                'release_date': movie.release_date.isoformat() if movie.release_date else None,
                'runtime': movie.runtime,
            }
            for movie in movies
        ]
    }
    
    return JsonResponse(data)
```

---

## ✅ Verification Checklist

- [ ] Node.js 18+ installed
- [ ] Dependencies installed (`npm install`)
- [ ] Django backend running on port 8000
- [ ] CORS configured in Django
- [ ] React frontend running on port 3000
- [ ] Browser shows the app

---

## 🎯 What You Get

✅ **Modern UI** - Netflix-inspired design  
✅ **Responsive** - Works on all devices  
✅ **Fast** - Vite + React 18  
✅ **Search** - Real-time search  
✅ **Lazy Loading** - Optimized images  
✅ **Favorites** - Save favorites locally  
✅ **Dark Theme** - Eye-friendly  

---

## 🐛 Common Issues

### Port 3000 in use?
```powershell
# Kill process on port 3000
Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process
```

### CORS errors?
- Make sure `django-cors-headers` is installed
- Check Django settings for CORS configuration
- Restart Django server

### API not found?
- Ensure Django is running on port 8000
- Check `.env` file has `VITE_API_URL=http://localhost:8000`
- Verify API endpoints exist

---

## 📚 Full Documentation

For detailed documentation, see:
- **REACT_FRONTEND_GUIDE.md** - Complete setup guide
- **frontend/README.md** - Frontend documentation

---

**That's it! You're ready to go! 🎉**