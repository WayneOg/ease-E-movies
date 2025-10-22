# ease-E-movies Frontend

Modern React.js frontend for the ease-E-movies application.

## 🚀 Features

- ⚡ **Vite** - Lightning fast build tool
- ⚛️ **React 18** - Latest React features
- 🎨 **Tailwind CSS** - Utility-first CSS framework
- 🔄 **React Router** - Client-side routing
- 📡 **Axios** - HTTP client for API calls
- 🎭 **Context API** - State management
- 🖼️ **Lazy Loading** - Optimized image loading
- 📱 **Responsive Design** - Mobile-first approach
- 🌙 **Dark Theme** - Netflix-inspired design

## 📦 Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🛠️ Tech Stack

- **React 18.3** - UI library
- **Vite 5.3** - Build tool
- **Tailwind CSS 3.4** - Styling
- **React Router 6.26** - Routing
- **Axios 1.7** - HTTP client
- **React Icons 5.2** - Icon library
- **React Intersection Observer** - Lazy loading

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/       # Reusable components
│   │   ├── Navbar.jsx
│   │   ├── Footer.jsx
│   │   ├── MovieCard.jsx
│   │   ├── MovieGrid.jsx
│   │   ├── Hero.jsx
│   │   └── SkeletonCard.jsx
│   ├── pages/           # Page components
│   │   ├── Home.jsx
│   │   ├── Movies.jsx
│   │   ├── Series.jsx
│   │   ├── MovieDetail.jsx
│   │   ├── SeriesDetail.jsx
│   │   ├── Search.jsx
│   │   ├── Genre.jsx
│   │   └── NotFound.jsx
│   ├── services/        # API services
│   │   └── api.js
│   ├── context/         # React Context
│   │   └── MovieContext.jsx
│   ├── hooks/           # Custom hooks
│   ├── App.jsx          # Main app component
│   ├── main.jsx         # Entry point
│   └── index.css        # Global styles
├── public/              # Static assets
├── index.html           # HTML template
├── vite.config.js       # Vite configuration
├── tailwind.config.js   # Tailwind configuration
└── package.json         # Dependencies

```

## 🎨 Components

### Navbar
- Responsive navigation with mobile menu
- Search functionality
- Genre dropdown
- Sticky on scroll

### MovieCard
- Lazy loading images
- Hover effects
- Rating display
- Favorite button

### Hero
- Auto-rotating carousel
- Backdrop images
- Call-to-action buttons

### MovieGrid
- Responsive grid layout
- Loading skeletons
- Empty state handling

## 🔌 API Integration

The frontend connects to the Django backend via Axios:

```javascript
// Example API call
import { movieAPI } from './services/api';

const movies = await movieAPI.getMovies(page);
const movie = await movieAPI.getMovieById(id);
const results = await movieAPI.searchMovies(query);
```

## 🎯 Available Routes

- `/` - Home page with trending movies
- `/movies` - All movies
- `/series` - All TV series
- `/movie/:id` - Movie details
- `/series/:id` - Series details
- `/search?q=query` - Search results
- `/genre/:genreName` - Movies by genre

## 🌐 Environment Variables

Create a `.env` file in the frontend directory:

```env
VITE_API_URL=http://localhost:8000
```

## 🎨 Customization

### Colors

Edit `tailwind.config.js` to customize colors:

```javascript
colors: {
  primary: {
    DEFAULT: '#e50914',  // Netflix red
    hover: '#f40612',
  },
  dark: {
    DEFAULT: '#141414',
    light: '#1f1f1f',
    lighter: '#2a2a2a',
  }
}
```

### Fonts

Edit `src/index.css` to change fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
```

## 📱 Responsive Breakpoints

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

## 🚀 Performance Optimizations

- ✅ Lazy loading images with Intersection Observer
- ✅ Code splitting with React Router
- ✅ Optimized bundle size with Vite
- ✅ Skeleton loaders for better UX
- ✅ Debounced search
- ✅ Cached API responses

## 🐛 Troubleshooting

### Port already in use
```bash
# Change port in vite.config.js
server: {
  port: 3001
}
```

### API connection issues
- Ensure Django backend is running on port 8000
- Check CORS settings in Django
- Verify VITE_API_URL in .env file

### Build errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## 📝 Scripts

```bash
# Development
npm run dev          # Start dev server (http://localhost:3000)

# Production
npm run build        # Build for production
npm run preview      # Preview production build

# Linting
npm run lint         # Run ESLint
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the ease-E-movies application.

---

**Built with ❤️ using React and Tailwind CSS**