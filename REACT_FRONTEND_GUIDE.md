# 🎬 React Frontend Setup Guide

Complete guide to set up and use the modern React.js frontend for ease-E-movies.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Django Backend Setup](#django-backend-setup)
5. [Running the Application](#running-the-application)
6. [Features](#features)
7. [Project Structure](#project-structure)
8. [Customization](#customization)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The React frontend is a modern, Netflix-inspired UI built with:

- **React 18** - Latest React features
- **Vite** - Lightning-fast build tool
- **Tailwind CSS** - Utility-first styling
- **React Router** - Client-side routing
- **Axios** - API communication
- **Context API** - State management

### Key Features

✅ **Modern UI/UX** - Netflix-inspired design  
✅ **Fully Responsive** - Mobile, tablet, desktop  
✅ **Lazy Loading** - Optimized image loading  
✅ **Search** - Real-time search functionality  
✅ **Favorites** - Save favorite movies/series  
✅ **Genre Filtering** - Browse by genre  
✅ **Infinite Scroll** - Load more content  
✅ **Dark Theme** - Eye-friendly dark mode  

---

## 📦 Prerequisites

Before starting, ensure you have:

- **Node.js** 18+ installed ([Download](https://nodejs.org/))
- **npm** or **yarn** package manager
- **Django backend** running (see below)
- **Git** (optional, for version control)

Check your Node.js version:
```bash
node --version  # Should be 18.0.0 or higher
npm --version   # Should be 9.0.0 or higher
```

---

## 🚀 Installation

### Step 1: Navigate to Frontend Directory

```bash
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

This will install all required packages:
- react, react-dom
- react-router-dom
- axios
- tailwindcss
- react-icons
- vite
- And more...

### Step 3: Configure Environment

Create `.env` file (already created):
```env
VITE_API_URL=http://localhost:8000
```

---

## 🔧 Django Backend Setup

The React frontend needs the Django backend running. Follow these steps:

### Step 1: Enable CORS

Install Django CORS headers:
```bash
pip install django-cors-headers
```

### Step 2: Update Django Settings

Add to `moviedatabase/settings.py`:

```python
INSTALLED_APPS = [
    # ... existing apps
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add at the top
    'django.middleware.common.CommonMiddleware',
    # ... other middleware
]

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

### Step 3: Create API Endpoints

The React app expects these endpoints:

```python
# In moviedb/urls.py or create new api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Movies
    path('movies/', views.movies_list, name='movies_list'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    
    # Series
    path('series/', views.series_list, name='series_list'),
    path('series/<int:id>/', views.series_detail, name='series_detail'),
    
    # Search
    path('search/', views.search, name='search'),
    
    # Genres
    path('action/', views.action_movies, name='action'),
    path('comedy/', views.comedy_movies, name='comedy'),
    path('horror/', views.horror_movies, name='horror'),
    path('scifi/', views.scifi_movies, name='scifi'),
    path('romance/', views.romance_movies, name='romance'),
    path('animation/', views.animation_movies, name='animation'),
    
    # Additional
    path('trending/', views.trending, name='trending'),
    path('popular/', views.popular, name='popular'),
    path('top-rated/', views.top_rated, name='top_rated'),
]
```

### Step 4: Update Views to Return JSON

Example view:
```python
from django.http import JsonResponse
from .models import Movie
from .utils import fetch_movies_by_genre, GENRE_IDS

def movies_list(request):
    page = request.GET.get('page', 1)
    movies = Movie.objects.all()[:20]  # Adjust as needed
    
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

def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = {
            'id': movie.id,
            'title': movie.title,
            'poster_path': movie.poster_path,
            'backdrop_path': movie.backdrop_path,
            'overview': movie.overview,
            'tagline': movie.tagline,
            'vote_average': float(movie.vote_average) if movie.vote_average else 0,
            'release_date': movie.release_date.isoformat() if movie.release_date else None,
            'runtime': movie.runtime,
            'genres': [{'id': g.id, 'name': g.name} for g in movie.genres.all()],
        }
        return JsonResponse(data)
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
```

---

## 🎮 Running the Application

### Start Django Backend (Terminal 1)

```bash
cd c:\Users\a\Documents\GitHub\ease-E-movies
python manage.py runserver
```

Backend will run on: `http://localhost:8000`

### Start React Frontend (Terminal 2)

```bash
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm run dev
```

Frontend will run on: `http://localhost:3000`

### Access the Application

Open your browser and visit:
```
http://localhost:3000
```

---

## ✨ Features

### 1. Home Page
- **Hero Carousel** - Auto-rotating featured movies
- **Trending Section** - Latest trending movies
- **Popular Movies** - Most popular content
- **Top Rated** - Highest-rated movies

### 2. Movies Page
- **Grid Layout** - Responsive movie grid
- **Infinite Scroll** - Load more on scroll
- **Lazy Loading** - Images load as you scroll

### 3. Series Page
- **TV Shows** - Browse all series
- **Season Info** - Number of seasons/episodes
- **Status Badge** - Ongoing/Ended status

### 4. Search
- **Real-time Search** - Instant results
- **Multi-type** - Search movies and series
- **Result Count** - Shows number of results

### 5. Genre Pages
- **Action** - `/genre/action`
- **Comedy** - `/genre/comedy`
- **Horror** - `/genre/horror`
- **Sci-Fi** - `/genre/scifi`
- **Romance** - `/genre/romance`
- **Animation** - `/genre/animation`

### 6. Detail Pages
- **Movie Details** - Full movie information
- **Series Details** - Complete series info
- **Backdrop Images** - Full-width backgrounds
- **Rating Display** - Color-coded ratings
- **Favorites** - Add to favorites

### 7. Navigation
- **Sticky Navbar** - Stays on top while scrolling
- **Mobile Menu** - Hamburger menu for mobile
- **Search Bar** - Quick search access
- **Genre Dropdown** - Easy genre navigation

---

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Navbar.jsx           # Navigation component
│   │   ├── Footer.jsx           # Footer component
│   │   ├── MovieCard.jsx        # Movie card with lazy loading
│   │   ├── MovieGrid.jsx        # Grid layout for movies
│   │   ├── Hero.jsx             # Hero carousel
│   │   └── SkeletonCard.jsx     # Loading skeleton
│   │
│   ├── pages/
│   │   ├── Home.jsx             # Home page
│   │   ├── Movies.jsx           # All movies page
│   │   ├── Series.jsx           # All series page
│   │   ├── MovieDetail.jsx      # Movie detail page
│   │   ├── SeriesDetail.jsx     # Series detail page
│   │   ├── Search.jsx           # Search page
│   │   ├── Genre.jsx            # Genre page
│   │   └── NotFound.jsx         # 404 page
│   │
│   ├── services/
│   │   └── api.js               # API service layer
│   │
│   ├── context/
│   │   └── MovieContext.jsx     # Global state management
│   │
│   ├── App.jsx                  # Main app component
│   ├── main.jsx                 # Entry point
│   └── index.css                # Global styles
│
├── public/                      # Static assets
├── index.html                   # HTML template
├── vite.config.js              # Vite configuration
├── tailwind.config.js          # Tailwind configuration
├── package.json                # Dependencies
└── README.md                   # Documentation
```

---

## 🎨 Customization

### Change Colors

Edit `tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        DEFAULT: '#e50914',  // Change this
        hover: '#f40612',
      },
      dark: {
        DEFAULT: '#141414',
        light: '#1f1f1f',
        lighter: '#2a2a2a',
      }
    },
  },
}
```

### Change Fonts

Edit `src/index.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'Poppins', sans-serif;
}
```

### Add New Pages

1. Create component in `src/pages/`
2. Add route in `src/App.jsx`:

```javascript
<Route path="/new-page" element={<NewPage />} />
```

### Modify API Endpoints

Edit `src/services/api.js`:

```javascript
export const movieAPI = {
  getMovies: (page = 1) => api.get(`/api/movies/?page=${page}`),
  // Add new endpoints here
};
```

---

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

This creates a `dist/` folder with optimized files.

### Deploy to Netlify

1. Install Netlify CLI:
```bash
npm install -g netlify-cli
```

2. Deploy:
```bash
netlify deploy --prod --dir=dist
```

### Deploy to Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel --prod
```

### Serve with Django

1. Build the React app:
```bash
npm run build
```

2. Copy `dist/` contents to Django `static/` folder

3. Update Django settings:
```python
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'dist',
]
```

4. Create a catch-all view in Django:
```python
from django.views.generic import TemplateView

urlpatterns = [
    # ... API routes
    path('', TemplateView.as_view(template_name='index.html')),
]
```

---

## 🐛 Troubleshooting

### Issue: Port 3000 already in use

**Solution**: Change port in `vite.config.js`:
```javascript
server: {
  port: 3001
}
```

### Issue: CORS errors

**Solution**: Ensure Django CORS is configured:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### Issue: API not connecting

**Solution**: 
1. Check Django is running on port 8000
2. Verify `.env` file has correct API URL
3. Check browser console for errors

### Issue: Images not loading

**Solution**:
1. Check TMDb API key in Django
2. Verify poster_path in API response
3. Check browser network tab

### Issue: Build fails

**Solution**:
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Issue: Blank page after build

**Solution**: Check browser console for errors. Usually a routing issue.

---

## 📊 Performance Tips

1. **Enable Gzip** - Compress responses
2. **Use CDN** - Serve static files from CDN
3. **Lazy Load** - Already implemented
4. **Code Splitting** - Already implemented with React Router
5. **Cache API** - Add caching layer
6. **Optimize Images** - Use WebP format

---

## 🔒 Security

1. **Environment Variables** - Never commit `.env`
2. **API Keys** - Keep in backend only
3. **HTTPS** - Use HTTPS in production
4. **CORS** - Restrict to specific origins
5. **Input Validation** - Validate all user input

---

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [React Router](https://reactrouter.com/)
- [Axios](https://axios-http.com/)

---

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Configure Django CORS
3. ✅ Start both servers
4. ✅ Test the application
5. ✅ Customize as needed
6. ✅ Deploy to production

---

## 🤝 Support

If you encounter issues:

1. Check this guide
2. Review browser console
3. Check Django logs
4. Verify API endpoints
5. Test with Postman/curl

---

**Happy Coding! 🚀**

Built with ❤️ using React, Vite, and Tailwind CSS