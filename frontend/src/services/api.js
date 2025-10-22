import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Add any auth tokens here if needed
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API endpoints
export const movieAPI = {
  // Get all movies
  getMovies: (page = 1) => api.get(`/api/movies/?page=${page}`),
  
  // Get movie by ID
  getMovieById: (id) => api.get(`/api/movie/${id}/`),
  
  // Get movies by genre
  getMoviesByGenre: (genre, page = 1) => api.get(`/api/genre/${genre}/?page=${page}`),
  
  // Search movies
  searchMovies: (query, page = 1) => api.get(`/api/search/?q=${query}&page=${page}`),
  
  // Get trending movies
  getTrending: () => api.get('/api/trending/'),
  
  // Get popular movies
  getPopular: (page = 1) => api.get(`/api/popular/?page=${page}`),
  
  // Get top rated movies
  getTopRated: (page = 1) => api.get(`/api/top-rated/?page=${page}`),
  
  // Get latest movies
  getLatest: () => api.get('/api/latest/'),
};

export const seriesAPI = {
  // Get all series
  getSeries: (page = 1) => api.get(`/api/series/?page=${page}`),
  
  // Get series by ID
  getSeriesById: (id) => api.get(`/api/series/${id}/`),
  
  // Get series by genre
  getSeriesByGenre: (genre, page = 1) => api.get(`/api/genre/${genre}/?page=${page}`),
  
  // Get season details
  getSeasonDetails: (seriesId, seasonNumber) => 
    api.get(`/api/series/${seriesId}/season/${seasonNumber}/`),
  
  // Get episode details
  getEpisodeDetails: (seriesId, seasonNumber, episodeNumber) => 
    api.get(`/api/series/${seriesId}/season/${seasonNumber}/episode/${episodeNumber}/`),
};

export const genreAPI = {
  // Get all genres
  getGenres: () => api.get('/api/genres/'),
  
  // Get movies by genre name
  getMoviesByGenre: (genreName, page = 1) => 
    api.get(`/api/genre/${genreName}/?page=${page}`),
};

export default api;