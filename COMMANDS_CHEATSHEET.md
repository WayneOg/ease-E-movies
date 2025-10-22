# 🎬 Commands Cheatsheet

Quick reference for all commands you'll need.

---

## 🚀 Initial Setup

### Install Frontend Dependencies
```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm install
```

### Install Django CORS
```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies
pip install django-cors-headers
```

---

## 🎮 Running the Application

### Start Django Backend (Terminal 1)
```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies
python manage.py runserver
```
**Runs on**: http://localhost:8000

### Start React Frontend (Terminal 2)
```powershell
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm run dev
```
**Runs on**: http://localhost:3000

---

## 🔧 Development Commands

### Django Commands
```powershell
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Check for issues
python manage.py check

# Shell
python manage.py shell
```

### React Commands
```powershell
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint

# Install new package
npm install package-name

# Update dependencies
npm update
```

---

## 📦 Package Management

### Install Packages
```powershell
# Frontend
cd frontend
npm install package-name

# Backend
pip install package-name
```

### Update Packages
```powershell
# Frontend
npm update

# Backend
pip install --upgrade package-name
```

### Remove Packages
```powershell
# Frontend
npm uninstall package-name

# Backend
pip uninstall package-name
```

---

## 🐛 Troubleshooting Commands

### Clear Caches
```powershell
# npm cache
npm cache clean --force

# Django cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

### Reinstall Dependencies
```powershell
# Frontend
cd frontend
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install

# Backend
pip install -r requirements.txt --force-reinstall
```

### Kill Process on Port
```powershell
# Kill process on port 3000
Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process

# Kill process on port 8000
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process
```

### Check Port Usage
```powershell
# Check what's running on port 3000
Get-NetTCPConnection -LocalPort 3000

# Check what's running on port 8000
Get-NetTCPConnection -LocalPort 8000
```

---

## 🔍 Debugging Commands

### Django Debug
```powershell
# Run with debug output
python manage.py runserver --verbosity 3

# Check database
python manage.py dbshell

# Show migrations
python manage.py showmigrations

# SQL for migration
python manage.py sqlmigrate app_name migration_name
```

### React Debug
```powershell
# Run with verbose output
npm run dev -- --debug

# Check bundle size
npm run build -- --report

# Analyze dependencies
npm list

# Check for outdated packages
npm outdated
```

---

## 📊 Testing Commands

### Django Tests
```powershell
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test moviedb

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### React Tests (if configured)
```powershell
# Run tests
npm test

# Run with coverage
npm test -- --coverage

# Run in watch mode
npm test -- --watch
```

---

## 🚀 Deployment Commands

### Build Frontend
```powershell
cd frontend
npm run build
```

### Collect Django Static Files
```powershell
python manage.py collectstatic --noinput
```

### Create Requirements File
```powershell
pip freeze > requirements.txt
```

### Deploy to Netlify
```powershell
cd frontend
npm run build
netlify deploy --prod --dir=dist
```

### Deploy to Vercel
```powershell
cd frontend
npm run build
vercel --prod
```

---

## 🔐 Security Commands

### Generate Secret Key
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Check Security
```powershell
python manage.py check --deploy
```

---

## 📝 Git Commands

### Initial Commit
```powershell
git add .
git commit -m "Add React frontend"
git push
```

### Create Branch
```powershell
git checkout -b feature/react-frontend
git push -u origin feature/react-frontend
```

### Merge Branch
```powershell
git checkout main
git merge feature/react-frontend
git push
```

---

## 🔄 Update Commands

### Update Django
```powershell
pip install --upgrade django
```

### Update React
```powershell
cd frontend
npm update react react-dom
```

### Update All Frontend Packages
```powershell
cd frontend
npm update
```

---

## 📦 Backup Commands

### Backup Database
```powershell
# SQLite
Copy-Item db.sqlite3 db.sqlite3.backup

# PostgreSQL
pg_dump dbname > backup.sql
```

### Backup Code
```powershell
# Create zip
Compress-Archive -Path . -DestinationPath backup.zip
```

---

## 🧹 Cleanup Commands

### Remove Build Files
```powershell
# Frontend
cd frontend
Remove-Item -Recurse -Force dist

# Django
python manage.py clean_pyc
```

### Remove Cache
```powershell
# Python cache
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force

# npm cache
npm cache clean --force
```

---

## 📊 Monitoring Commands

### Check Django Logs
```powershell
# View debug.log
Get-Content debug.log -Tail 50 -Wait
```

### Check npm Logs
```powershell
# View npm debug log
Get-Content npm-debug.log
```

### Monitor Performance
```powershell
# Django
python manage.py runserver --noreload

# React (production mode)
npm run preview
```

---

## 🎯 Quick Actions

### Full Restart
```powershell
# Stop all servers (Ctrl+C in each terminal)

# Restart Django
cd c:\Users\a\Documents\GitHub\ease-E-movies
python manage.py runserver

# Restart React
cd c:\Users\a\Documents\GitHub\ease-E-movies\frontend
npm run dev
```

### Fresh Install
```powershell
# Backend
pip install -r requirements.txt

# Frontend
cd frontend
Remove-Item -Recurse -Force node_modules
npm install
```

### Production Build
```powershell
# Build frontend
cd frontend
npm run build

# Collect static
cd ..
python manage.py collectstatic --noinput

# Run production server
python manage.py runserver --insecure
```

---

## 🆘 Emergency Commands

### Reset Everything
```powershell
# Stop all servers
# Delete node_modules
Remove-Item -Recurse -Force frontend\node_modules

# Delete Python cache
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force

# Reinstall
cd frontend
npm install
cd ..
pip install -r requirements.txt
```

### Fix Permissions
```powershell
# Windows - Run as Administrator
icacls . /grant Everyone:F /t
```

---

## 📚 Documentation Commands

### Generate Docs
```powershell
# Django
pip install sphinx
sphinx-quickstart
sphinx-build -b html docs/source docs/build

# React (if using JSDoc)
npm install -g jsdoc
jsdoc src -r -d docs
```

---

## 🎨 Code Quality Commands

### Format Code
```powershell
# Python (Black)
pip install black
black .

# JavaScript (Prettier)
cd frontend
npm install --save-dev prettier
npx prettier --write "src/**/*.{js,jsx}"
```

### Lint Code
```powershell
# Python (Flake8)
pip install flake8
flake8 .

# JavaScript (ESLint)
cd frontend
npm run lint
```

---

## 🔍 Search Commands

### Find Files
```powershell
# Find by name
Get-ChildItem -Recurse -Filter "*.jsx"

# Find by content
Select-String -Path "src\**\*.jsx" -Pattern "useState"
```

### Find in Code
```powershell
# Search in all files
Select-String -Path . -Pattern "TODO" -Recurse
```

---

## 📈 Performance Commands

### Measure Build Time
```powershell
# Frontend
Measure-Command { npm run build }

# Django
Measure-Command { python manage.py collectstatic --noinput }
```

### Check Bundle Size
```powershell
cd frontend
npm run build
Get-ChildItem dist -Recurse | Measure-Object -Property Length -Sum
```

---

## 🎯 Most Used Commands

```powershell
# Start development (run in 2 terminals)
python manage.py runserver          # Terminal 1
npm run dev                          # Terminal 2 (in frontend/)

# Install packages
pip install package-name             # Backend
npm install package-name             # Frontend

# Build for production
npm run build                        # Frontend
python manage.py collectstatic       # Django

# Check for issues
python manage.py check               # Django
npm run lint                         # Frontend

# Clear cache
npm cache clean --force              # Frontend
python manage.py shell               # Django (then cache.clear())
```

---

## 💡 Pro Tips

1. **Use aliases** - Create PowerShell aliases for common commands
2. **Use tmux/screen** - Run multiple terminals in one window
3. **Use watchdog** - Auto-restart Django on file changes
4. **Use nodemon** - Auto-restart Node on file changes
5. **Use Docker** - Containerize for consistent environments

---

## 🎊 Quick Reference

| Task | Command |
|------|---------|
| Start Django | `python manage.py runserver` |
| Start React | `npm run dev` |
| Install npm | `npm install` |
| Install pip | `pip install -r requirements.txt` |
| Build React | `npm run build` |
| Django shell | `python manage.py shell` |
| Clear npm cache | `npm cache clean --force` |
| Check Django | `python manage.py check` |
| Run tests | `python manage.py test` |
| Create superuser | `python manage.py createsuperuser` |

---

**Bookmark this page for quick reference! 📌**