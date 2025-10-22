import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { movieAPI } from '../services/api';
import MovieGrid from '../components/MovieGrid';
import { FiChevronDown } from 'react-icons/fi';

const Genre = () => {
  const { genreName } = useParams();
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);

  useEffect(() => {
    setMovies([]);
    setPage(1);
    fetchMoviesByGenre(1);
  }, [genreName]);

  const fetchMoviesByGenre = async (pageNum = 1) => {
    try {
      if (pageNum === 1) {
        setLoading(true);
      } else {
        setLoadingMore(true);
      }

      const data = await movieAPI.getMoviesByGenre(genreName, pageNum);
      const newMovies = data.results || data;

      if (pageNum === 1) {
        setMovies(newMovies);
      } else {
        setMovies((prev) => [...prev, ...newMovies]);
      }

      setHasMore(newMovies.length > 0);
      setPage(pageNum);
    } catch (error) {
      console.error('Error fetching movies by genre:', error);
    } finally {
      setLoading(false);
      setLoadingMore(false);
    }
  };

  const loadMore = () => {
    if (!loadingMore && hasMore) {
      fetchMoviesByGenre(page + 1);
    }
  };

  const formatGenreName = (name) => {
    return name.charAt(0).toUpperCase() + name.slice(1);
  };

  return (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-2">
            {formatGenreName(genreName)} Movies
          </h1>
          <p className="text-gray-400">
            Explore the best {genreName} movies
          </p>
        </div>

        {/* Movies Grid */}
        <MovieGrid movies={movies} loading={loading} />

        {/* Load More Button */}
        {!loading && hasMore && (
          <div className="flex justify-center mt-12">
            <button
              onClick={loadMore}
              disabled={loadingMore}
              className="flex items-center space-x-2 bg-primary hover:bg-primary-hover text-white px-8 py-3 rounded-lg font-semibold transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loadingMore ? (
                <>
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white" />
                  <span>Loading...</span>
                </>
              ) : (
                <>
                  <span>Load More</span>
                  <FiChevronDown />
                </>
              )}
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Genre;