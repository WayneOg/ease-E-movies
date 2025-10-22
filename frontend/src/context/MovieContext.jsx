import { createContext, useContext, useState, useEffect } from 'react';
import { movieAPI, seriesAPI } from '../services/api';

const MovieContext = createContext();

export const useMovies = () => {
  const context = useContext(MovieContext);
  if (!context) {
    throw new Error('useMovies must be used within MovieProvider');
  }
  return context;
};

export const MovieProvider = ({ children }) => {
  const [movies, setMovies] = useState([]);
  const [series, setSeries] = useState([]);
  const [trending, setTrending] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [favorites, setFavorites] = useState(() => {
    const saved = localStorage.getItem('favorites');
    return saved ? JSON.parse(saved) : [];
  });

  // Fetch trending movies on mount
  useEffect(() => {
    fetchTrending();
  }, []);

  // Save favorites to localStorage
  useEffect(() => {
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }, [favorites]);

  const fetchTrending = async () => {
    try {
      setLoading(true);
      const data = await movieAPI.getTrending();
      setTrending(data.results || data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch trending movies');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchMovies = async (page = 1) => {
    try {
      setLoading(true);
      const data = await movieAPI.getMovies(page);
      setMovies(data.results || data);
      setError(null);
      return data;
    } catch (err) {
      setError('Failed to fetch movies');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchSeries = async (page = 1) => {
    try {
      setLoading(true);
      const data = await seriesAPI.getSeries(page);
      setSeries(data.results || data);
      setError(null);
      return data;
    } catch (err) {
      setError('Failed to fetch series');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const searchContent = async (query, page = 1) => {
    try {
      setLoading(true);
      setSearchQuery(query);
      const data = await movieAPI.searchMovies(query, page);
      setError(null);
      return data;
    } catch (err) {
      setError('Search failed');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const addToFavorites = (item) => {
    setFavorites((prev) => {
      if (prev.find((fav) => fav.id === item.id)) {
        return prev.filter((fav) => fav.id !== item.id);
      }
      return [...prev, item];
    });
  };

  const isFavorite = (id) => {
    return favorites.some((fav) => fav.id === id);
  };

  const value = {
    movies,
    series,
    trending,
    loading,
    error,
    searchQuery,
    favorites,
    fetchMovies,
    fetchSeries,
    fetchTrending,
    searchContent,
    addToFavorites,
    isFavorite,
  };

  return <MovieContext.Provider value={value}>{children}</MovieContext.Provider>;
};