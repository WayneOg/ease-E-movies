# 🎨 Integration Guide - Using New CSS & JavaScript

This guide shows you how to integrate the new CSS and JavaScript improvements into your Django templates.

---

## 📋 Table of Contents

1. [Quick Integration](#quick-integration)
2. [Base Template Setup](#base-template-setup)
3. [Using CSS Classes](#using-css-classes)
4. [Using JavaScript Functions](#using-javascript-functions)
5. [Component Examples](#component-examples)
6. [Mobile Responsive Navigation](#mobile-responsive-navigation)

---

## 🚀 Quick Integration

### Step 1: Update Your Base Template

Add these lines to your base template (e.g., `base.html`):

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}ease-E-movies{% endblock %}</title>
    
    <!-- New CSS Files -->
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    <link rel="stylesheet" href="{% static 'css/navigation.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
    
    <!-- New JavaScript File -->
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 🎯 Base Template Setup

### Complete Base Template Example

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}ease-E-movies{% endblock %}</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
    
    <!-- CSS Files -->
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    <link rel="stylesheet" href="{% static 'css/navigation.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="navbar-container">
            <a href="{% url 'home' %}" class="navbar-brand">
                <span class="brand-logo">🎬</span>
                ease-E-movies
            </a>
            
            <!-- Mobile Menu Toggle -->
            <button class="mobile-menu-toggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <!-- Navigation Menu -->
            <ul class="navbar-menu">
                <li><a href="{% url 'home' %}" class="nav-link">Home</a></li>
                
                <!-- Dropdown Example -->
                <li class="dropdown">
                    <a href="#" class="nav-link dropdown-toggle">
                        Movies <span class="dropdown-arrow">▼</span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="{% url 'action' %}">Action</a></li>
                        <li><a href="{% url 'comedy' %}">Comedy</a></li>
                        <li><a href="{% url 'horror' %}">Horror</a></li>
                        <li><a href="{% url 'scifi' %}">Sci-Fi</a></li>
                    </ul>
                </li>
                
                <li><a href="{% url 'series' %}" class="nav-link">Series</a></li>
                <li><a href="{% url 'search' %}" class="nav-link">Search</a></li>
            </ul>
            
            <!-- Search Bar -->
            <div class="navbar-search">
                <form action="{% url 'search' %}" method="get">
                    <input type="text" name="q" placeholder="Search movies..." class="search-input">
                    <button type="submit" class="search-button">🔍</button>
                </form>
            </div>
        </div>
    </nav>
    
    <!-- Mobile Menu Overlay -->
    <div class="menu-overlay"></div>
    
    <!-- Main Content -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 ease-E-movies. All rights reserved.</p>
        </div>
    </footer>
    
    <!-- Back to Top Button -->
    <button id="backToTop" class="back-to-top" aria-label="Back to top">↑</button>
    
    <!-- Toast Container -->
    <div id="toastContainer" class="toast-container"></div>
    
    <!-- JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 🎨 Using CSS Classes

### 1. Movie Grid Layout

```html
<div class="movie-grid">
    {% for movie in movies %}
    <div class="movie-card">
        <img src="https://image.tmdb.org/t/p/w500{{ movie.poster_path }}" 
             alt="{{ movie.title }}"
             class="lazy-load"
             data-src="https://image.tmdb.org/t/p/w500{{ movie.poster_path }}">
        <div class="movie-card-content">
            <h3 class="movie-title">{{ movie.title }}</h3>
            <div class="movie-meta">
                <span class="rating-badge" data-rating="{{ movie.vote_average }}">
                    ⭐ {{ movie.vote_average }}
                </span>
                <span class="year">{{ movie.release_date|date:"Y" }}</span>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```

### 2. Loading Skeleton

```html
<!-- Show while loading -->
<div class="skeleton-card">
    <div class="skeleton-image"></div>
    <div class="skeleton-text"></div>
    <div class="skeleton-text short"></div>
</div>
```

### 3. Buttons

```html
<!-- Primary Button -->
<button class="btn btn-primary">Watch Now</button>

<!-- Secondary Button -->
<button class="btn btn-secondary">Add to Watchlist</button>

<!-- Outline Button -->
<button class="btn btn-outline">Learn More</button>
```

### 4. Cards

```html
<div class="card">
    <div class="card-header">
        <h2>Featured Movie</h2>
    </div>
    <div class="card-body">
        <p>Movie description goes here...</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary">Watch Now</button>
    </div>
</div>
```

### 5. Container & Spacing

```html
<!-- Container -->
<div class="container">
    <h1>Page Title</h1>
</div>

<!-- Spacing Utilities -->
<div class="mt-2">Margin top 2</div>
<div class="mb-3">Margin bottom 3</div>
<div class="p-2">Padding 2</div>
```

---

## 🔧 Using JavaScript Functions

### 1. Toast Notifications

```html
<script>
// Show success message
window.MovieDBUtils.showToast('Movie added to watchlist!', 'success');

// Show error message
window.MovieDBUtils.showToast('Failed to load movie', 'error');

// Show info message
window.MovieDBUtils.showToast('Loading...', 'info');
</script>
```

### 2. Lazy Loading Images

```html
<!-- Add lazy-load class and data-src attribute -->
<img class="lazy-load" 
     data-src="https://image.tmdb.org/t/p/w500/poster.jpg"
     alt="Movie Poster">
```

The JavaScript will automatically:
- Load images as they come into view
- Show loading animation
- Handle errors gracefully

### 3. Rating Colors

```html
<!-- Add data-rating attribute -->
<span class="rating-badge" data-rating="8.5">⭐ 8.5</span>
<span class="rating-badge" data-rating="6.2">⭐ 6.2</span>
<span class="rating-badge" data-rating="4.1">⭐ 4.1</span>
```

Colors automatically applied:
- **Green**: Rating ≥ 7.0
- **Orange**: Rating 5.0 - 6.9
- **Red**: Rating < 5.0

### 4. Horizontal Scroll

```html
<div class="horizontal-scroll">
    <div class="movie-card">Movie 1</div>
    <div class="movie-card">Movie 2</div>
    <div class="movie-card">Movie 3</div>
    <!-- More cards... -->
</div>
```

Features:
- Drag to scroll on desktop
- Touch scroll on mobile
- Smooth scrolling

### 5. Local Storage

```javascript
// Save user preference
window.MovieDBUtils.saveToLocalStorage('theme', 'dark');

// Get user preference
const theme = window.MovieDBUtils.getFromLocalStorage('theme');

// Remove preference
window.MovieDBUtils.removeFromLocalStorage('theme');
```

---

## 📱 Component Examples

### Movie List Page

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Action Movies - ease-E-movies{% endblock %}

{% block content %}
<div class="container">
    <h1 class="page-title">Action Movies</h1>
    
    <!-- Loading State -->
    {% if loading %}
    <div class="movie-grid">
        {% for i in "123456" %}
        <div class="skeleton-card">
            <div class="skeleton-image"></div>
            <div class="skeleton-text"></div>
            <div class="skeleton-text short"></div>
        </div>
        {% endfor %}
    </div>
    {% endif %}
    
    <!-- Movies Grid -->
    <div class="movie-grid">
        {% for movie in movies %}
        <div class="movie-card">
            <a href="{% url 'movie_detail' movie.id %}">
                <img class="lazy-load" 
                     data-src="https://image.tmdb.org/t/p/w500{{ movie.poster_path }}"
                     alt="{{ movie.title }}">
                <div class="movie-card-content">
                    <h3 class="movie-title">{{ movie.title }}</h3>
                    <div class="movie-meta">
                        <span class="rating-badge" data-rating="{{ movie.vote_average }}">
                            ⭐ {{ movie.vote_average }}
                        </span>
                        <span class="year">{{ movie.release_date|date:"Y" }}</span>
                    </div>
                </div>
            </a>
        </div>
        {% empty %}
        <p class="text-center">No movies found.</p>
        {% endfor %}
    </div>
    
    <!-- Pagination -->
    {% if has_next %}
    <div class="text-center mt-3">
        <button class="btn btn-primary" onclick="loadMore()">Load More</button>
    </div>
    {% endif %}
</div>
{% endblock %}

{% block extra_js %}
<script>
function loadMore() {
    window.MovieDBUtils.showToast('Loading more movies...', 'info');
    // Your load more logic here
}
</script>
{% endblock %}
```

### Movie Detail Page

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}{{ movie.title }} - ease-E-movies{% endblock %}

{% block content %}
<div class="movie-detail">
    <div class="movie-backdrop" 
         style="background-image: url('https://image.tmdb.org/t/p/original{{ movie.backdrop_path }}');">
        <div class="backdrop-overlay"></div>
    </div>
    
    <div class="container">
        <div class="movie-detail-content">
            <div class="movie-poster">
                <img src="https://image.tmdb.org/t/p/w500{{ movie.poster_path }}" 
                     alt="{{ movie.title }}">
            </div>
            
            <div class="movie-info">
                <h1 class="movie-title">{{ movie.title }}</h1>
                
                <div class="movie-meta">
                    <span class="rating-badge" data-rating="{{ movie.vote_average }}">
                        ⭐ {{ movie.vote_average }}
                    </span>
                    <span class="year">{{ movie.release_date|date:"Y" }}</span>
                    <span class="runtime">{{ movie.runtime }} min</span>
                </div>
                
                <p class="tagline">{{ movie.tagline }}</p>
                <p class="overview">{{ movie.overview }}</p>
                
                <div class="genres">
                    {% for genre in movie.genres.all %}
                    <span class="genre-badge">{{ genre.name }}</span>
                    {% endfor %}
                </div>
                
                <div class="action-buttons">
                    <button class="btn btn-primary" onclick="playMovie()">
                        ▶ Play Now
                    </button>
                    <button class="btn btn-secondary" onclick="addToWatchlist()">
                        + Add to Watchlist
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
function playMovie() {
    window.MovieDBUtils.showToast('Starting movie...', 'success');
    // Your play logic here
}

function addToWatchlist() {
    window.MovieDBUtils.showToast('Added to watchlist!', 'success');
    window.MovieDBUtils.saveToLocalStorage('watchlist_{{ movie.id }}', true);
}
</script>
{% endblock %}
```

### Search Page

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Search - ease-E-movies{% endblock %}

{% block content %}
<div class="container">
    <div class="search-page">
        <h1 class="page-title">Search Movies & Series</h1>
        
        <form method="get" class="search-form">
            <div class="search-input-group">
                <input type="text" 
                       name="q" 
                       value="{{ query }}" 
                       placeholder="Search for movies, series..."
                       class="search-input-large"
                       autofocus>
                <button type="submit" class="btn btn-primary">Search</button>
            </div>
        </form>
        
        {% if query %}
        <div class="search-results">
            <h2>Results for "{{ query }}"</h2>
            
            {% if results %}
            <div class="movie-grid">
                {% for item in results %}
                <div class="movie-card">
                    <a href="{% url 'movie_detail' item.id %}">
                        <img class="lazy-load" 
                             data-src="https://image.tmdb.org/t/p/w500{{ item.poster_path }}"
                             alt="{{ item.title }}">
                        <div class="movie-card-content">
                            <h3 class="movie-title">{{ item.title }}</h3>
                            <span class="rating-badge" data-rating="{{ item.vote_average }}">
                                ⭐ {{ item.vote_average }}
                            </span>
                        </div>
                    </a>
                </div>
                {% endfor %}
            </div>
            {% else %}
            <div class="no-results">
                <p>No results found for "{{ query }}"</p>
                <p class="text-muted">Try different keywords</p>
            </div>
            {% endif %}
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

---

## 📱 Mobile Responsive Navigation

The navigation automatically adapts to mobile devices:

### Features:
- ✅ Hamburger menu on mobile
- ✅ Slide-in menu animation
- ✅ Overlay background
- ✅ Touch-friendly dropdowns
- ✅ Sticky navbar on scroll

### HTML Structure:

```html
<nav class="navbar">
    <div class="navbar-container">
        <!-- Brand -->
        <a href="/" class="navbar-brand">ease-E-movies</a>
        
        <!-- Mobile Toggle -->
        <button class="mobile-menu-toggle">
            <span></span>
            <span></span>
            <span></span>
        </button>
        
        <!-- Menu -->
        <ul class="navbar-menu">
            <li><a href="/" class="nav-link">Home</a></li>
            <li class="dropdown">
                <a href="#" class="nav-link dropdown-toggle">
                    Movies <span class="dropdown-arrow">▼</span>
                </a>
                <ul class="dropdown-menu">
                    <li><a href="/action">Action</a></li>
                    <li><a href="/comedy">Comedy</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>

<!-- Overlay for mobile -->
<div class="menu-overlay"></div>
```

---

## 🎯 Best Practices

### 1. Always Use Lazy Loading for Images
```html
<!-- ✅ Good -->
<img class="lazy-load" data-src="image.jpg" alt="Description">

<!-- ❌ Bad -->
<img src="image.jpg" alt="Description">
```

### 2. Use Toast for User Feedback
```javascript
// ✅ Good - Inform users
window.MovieDBUtils.showToast('Action completed!', 'success');

// ❌ Bad - Silent actions
// No feedback
```

### 3. Add Loading States
```html
<!-- ✅ Good - Show skeleton while loading -->
{% if loading %}
    <div class="skeleton-card"></div>
{% else %}
    <div class="movie-card">...</div>
{% endif %}
```

### 4. Use Semantic HTML
```html
<!-- ✅ Good -->
<main class="main-content">
    <article class="movie-detail">...</article>
</main>

<!-- ❌ Bad -->
<div class="main-content">
    <div class="movie-detail">...</div>
</div>
```

---

## 🔍 Testing Your Integration

### 1. Check CSS Loading
Open browser DevTools → Network tab → Look for:
- `base.css` (Status: 200)
- `navigation.css` (Status: 200)

### 2. Check JavaScript Loading
Open browser Console → Type:
```javascript
window.MovieDBUtils
```
Should show object with functions.

### 3. Test Mobile View
- Open DevTools → Toggle device toolbar
- Test hamburger menu
- Test touch scrolling

### 4. Test Lazy Loading
- Open DevTools → Network tab
- Scroll page
- Images should load as you scroll

---

## 📚 Additional Resources

- **IMPROVEMENTS.md** - Technical details of all improvements
- **QUICK_START.md** - Quick start guide
- **CHANGELOG.md** - Version history
- **PRODUCTION_CHECKLIST.md** - Deployment guide

---

## 🆘 Troubleshooting

### CSS Not Loading?
```python
# In settings.py, ensure:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'moviedb' / 'static']

# Run:
python manage.py collectstatic
```

### JavaScript Not Working?
```html
<!-- Ensure script is at bottom of body -->
<script src="{% static 'js/main.js' %}"></script>
```

### Images Not Lazy Loading?
```html
<!-- Ensure both class and data-src are present -->
<img class="lazy-load" data-src="image.jpg" alt="Description">
```

---

## ✅ Next Steps

1. ✅ Update your base template with new CSS/JS
2. ✅ Add lazy-load class to images
3. ✅ Use toast notifications for user feedback
4. ✅ Test on mobile devices
5. ✅ Customize colors in CSS variables

---

**Happy Coding! 🚀**