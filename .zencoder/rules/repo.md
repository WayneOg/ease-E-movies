---
description: Repository Information Overview
alwaysApply: true
---

# ease-E-movies Information

## Summary
A Django-based movie database application that allows users to browse movies, TV series, and anime. The application integrates with external APIs like TMDb (The Movie Database) and provides features for searching, categorizing, and viewing details of various media content.

## Structure
- **moviedatabase/**: Django project configuration files
- **moviedb/**: Main Django application with models, views, and templates
- **static/**: Static files for the application (CSS, JS, images)
- **.vscode/**: VS Code configuration
- **migrations/**: Database migration files

## Language & Runtime
**Language**: Python
**Version**: Python 3.9 (specified in vercel.json)
**Framework**: Django 5.0.6
**Build System**: Django's built-in management commands
**Package Manager**: pip

## Dependencies
**Main Dependencies**:
- Django: Web framework
- dj-database-url: Database URL configuration
- psycopg2-binary: PostgreSQL adapter
- requests: HTTP library for API calls
- supabase: Supabase client library
- beautifulsoup4: HTML parsing

**Development Dependencies**:
- python-dotenv: Environment variable management

## Database
**Type**: PostgreSQL (Supabase)
**Configuration**: Connection via dj_database_url in settings.py
**Models**:
- Movie: Stores movie information
- Series: Stores TV series information
- Season/Episode: Hierarchical TV show structure
- Category/Genre: Classification system

## External APIs
**TMDb API**: Used for fetching movie and TV series data
- API Key configured in settings.py
- Base URL: https://api.themoviedb.org/3

**Trakt API**: Integration for additional media data
- Client ID and Secret configured in settings.py

## Build & Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
```

## Deployment
**Platform**: Vercel
**Configuration**: vercel.json defines build and deployment settings
**Runtime**: Python 3.9
**Build Command**: python manage.py migrate
**Static Files**: Collected via build_files.sh script

## Main Entry Points
**Application**: moviedatabase/wsgi.py
**URLs**: 
- Main routes defined in moviedb/urls.py
- Admin interface at /admin/
- Homepage at root URL (/)

## Templates
**Location**: moviedb/templates/
**Key Templates**:
- home.html: Main landing page
- movie_details.html: Individual movie view
- series_details.html: Individual series view
- anime_details.html: Individual anime view

## Testing
**Framework**: Django's built-in TestCase
**Test Location**: moviedb/tests.py (currently empty)