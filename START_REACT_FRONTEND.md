# 🚀 Start Your React Frontend

## ✅ Setup Complete!

Your React frontend is now fully configured and ready to use! Here's what was done:

### Backend Configuration ✅
- ✅ CORS headers installed and configured
- ✅ API views created (`moviedb/api_views.py`)
- ✅ API endpoints added to URLs
- ✅ Django settings updated

### Frontend Configuration ✅
- ✅ React app created with Vite
- ✅ 318 npm packages installed
- ✅ API service configured
- ✅ All components and pages ready

---

## 🎯 Quick Start (2 Steps)

### Step 1: Start Django Backend

Open **Terminal 1** in VS Code:

```powershell
python manage.py runserver
```

✅ You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 2: Start React Frontend

Open **Terminal 2** in VS Code:

```powershell
Set-Location "c:\Users\a\Documents\GitHub\ease-E-movies\frontend"; npm run dev
```

✅ You should see:
```
  VITE v5.3.4  ready in XXX ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### Step 3: Open Browser

Visit: **http://localhost:5173/**

---

## 📡 Available API Endpoints

Your Django backend now has these JSON API endpoints:

```
GET /api/movies/              - List all movies (paginated)
GET /api/movie/<id>/          - Movie details
GET /api/series/              - List all series (paginated)
GET /api/series/<id>/         - Series details
GET /api/search/?q=query      - Search movies and series
GET /api/trending/            - Trending movies
GET /api/popular/             - Popular movies
GET /api/top-rated/           - Top rated movies
GET /api/latest/              - Latest movies

# Genre endpoints
GET /api/genre/action/        - Action movies
GET /api/genre/comedy/        - Comedy movies
GET /api/genre/horror/        - Horror movies
GET /api/genre/scifi/         - Sci-Fi movies
GET /api/genre/romance/       - Romance movies
GET /api/genre/animation/     - Animation movies
GET /api/genre/drama/         - Drama movies
GET /api/genre/thriller/      - Thriller movies
GET /api/genre/fantasy/       - Fantasy movies
GET /api/genre/adventure/     - Adventure movies
GET /api/genre/crime/         - Crime movies
GET /api/genre/mystery/       - Mystery movies
GET /api/genre/family/        - Family movies
GET /api/genre/documentary/   - Documentary movies
GET /api/genre/history/       - History movies
```

---

## 🎨 What You Get

### Modern Features
- ✅ **Netflix-inspired UI** - Dark theme with red accents
- ✅ **Fully Responsive** - Works perfectly on mobile, tablet, desktop
- ✅ **Fast Performance** - Vite + React 18 for instant updates
- ✅ **Lazy Loading** - Images load as you scroll
- ✅ **Search** - Real-time search with instant results
- ✅ **Favorites** - Save favorites (stored in browser)
- ✅ **Smooth Animations** - Professional transitions and effects

### Pages Available
1. **Home** (`/`) - Hero carousel + trending + popular sections
2. **Movies** (`/movies`) - All movies with infinite scroll
3. **Series** (`/series`) - All TV series
4. **Movie Details** (`/movie/:id`) - Full movie information
5. **Series Details** (`/series/:id`) - Full series information
6. **Search** (`/search?q=query`) - Search results
7. **Genre** (`/genre/:name`) - Movies by genre
8. **404 Page** - Custom not found page

---

## 🧪 Test the API

You can test the API endpoints directly in your browser:

1. **Test Movies List:**
   http://localhost:8000/api/movies/

2. **Test Movie Details:**
   http://localhost:8000/api/movie/550/

3. **Test Search:**
   http://localhost:8000/api/search/?q=matrix

4. **Test Trending:**
   http://localhost:8000/api/trending/

5. **Test Genre:**
   http://localhost:8000/api/genre/action/

---

## 🔧 Troubleshooting

### Port Already in Use?

**For Django (port 8000):**
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process
```

**For React (port 5173):**
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 5173).OwningProcess | Stop-Process
```

### CORS Errors?

Make sure Django is running and CORS is configured. Check:
- `corsheaders` is in `INSTALLED_APPS`
- `CorsMiddleware` is in `MIDDLEWARE`
- `CORS_ALLOWED_ORIGINS` includes `http://localhost:5173`

### API Returns 404?

Make sure you're using the `/api/` prefix:
- ✅ Correct: `http://localhost:8000/api/movies/`
- ❌ Wrong: `http://localhost:8000/movies/`

### React Shows Blank Page?

1. Check browser console for errors (F12)
2. Make sure Django backend is running
3. Check `.env` file has correct API URL
4. Try clearing browser cache

---

## 🎯 Development Workflow

### Making Changes

**Backend Changes (Django):**
1. Edit files in `moviedb/`
2. Django auto-reloads (no restart needed)
3. Refresh browser to see changes

**Frontend Changes (React):**
1. Edit files in `frontend/src/`
2. Vite hot-reloads automatically
3. Changes appear instantly in browser

### Adding New Features

**Add New API Endpoint:**
1. Add function to `moviedb/api_views.py`
2. Add URL to `moviedb/urls.py`
3. Add method to `frontend/src/services/api.js`
4. Use in your React components

**Add New Page:**
1. Create component in `frontend/src/pages/`
2. Add route to `frontend/src/App.jsx`
3. Add navigation link to `frontend/src/components/Navbar.jsx`

---

## 📦 Production Build

When ready to deploy:

### Build React App
```powershell
cd frontend
npm run build
```

This creates optimized files in `frontend/dist/`

### Deploy Options

1. **Serve from Django:**
   - Copy `frontend/dist/` to Django static files
   - Configure Django to serve the React app

2. **Deploy Separately:**
   - **Backend:** Deploy Django to Heroku, Railway, or DigitalOcean
   - **Frontend:** Deploy to Vercel, Netlify, or Cloudflare Pages

---

## 🎓 Learning Resources

### React Documentation
- [React Official Docs](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)

### Django REST APIs
- [Django REST Framework](https://www.django-rest-framework.org/)
- [CORS Headers](https://github.com/adamchainz/django-cors-headers)

---

## 🎉 You're All Set!

Your modern React frontend is ready to use. Just run both servers and start building!

**Need help?** Check the comprehensive guides:
- `REACT_FRONTEND_GUIDE.md` - Full documentation
- `FRONTEND_QUICKSTART.md` - Quick reference
- `COMMANDS_CHEATSHEET.md` - All commands

---

**Happy Coding! 🚀**