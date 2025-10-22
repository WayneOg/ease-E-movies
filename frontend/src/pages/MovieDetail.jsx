import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { movieAPI } from '../services/api';
import { FiStar, FiClock, FiCalendar, FiHeart, FiPlay, FiArrowLeft } from 'react-icons/fi';
import { useMovies } from '../context/MovieContext';
import VideoPlayer from '../components/VideoPlayer';

const MovieDetail = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showPlayer, setShowPlayer] = useState(false);
  const { addToFavorites, isFavorite } = useMovies();

  useEffect(() => {
    fetchMovieDetails();
  }, [id]);

  const fetchMovieDetails = async () => {
    try {
      setLoading(true);
      const data = await movieAPI.getMovieById(id);
      setMovie(data);
    } catch (error) {
      console.error('Error fetching movie details:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen pt-24 pb-12">
        <div className="container mx-auto px-4">
          <div className="skeleton w-full h-96 rounded-lg" />
        </div>
      </div>
    );
  }

  if (!movie) {
    return (
      <div className="min-h-screen pt-24 pb-12 flex items-center justify-center">
        <p className="text-gray-400 text-xl">Movie not found</p>
      </div>
    );
  }

  const backdropUrl = movie.backdrop_path
    ? `https://image.tmdb.org/t/p/original${movie.backdrop_path}`
    : '';
  const posterUrl = movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    : '';

  return (
    <div className="min-h-screen">
      {/* Backdrop */}
      <div className="relative h-[60vh]">
        {backdropUrl && (
          <img
            src={backdropUrl}
            alt={movie.title}
            className="w-full h-full object-cover"
          />
        )}
        <div className="absolute inset-0 bg-gradient-to-t from-dark via-dark/70 to-transparent" />
        
        {/* Back Button */}
        <Link
          to="/"
          className="absolute top-24 left-4 flex items-center space-x-2 text-white bg-black/50 backdrop-blur-md px-4 py-2 rounded-lg hover:bg-black/70 transition-colors"
        >
          <FiArrowLeft />
          <span>Back</span>
        </Link>
      </div>

      {/* Content */}
      <div className="container mx-auto px-4 -mt-40 relative z-10">
        <div className="flex flex-col md:flex-row gap-8">
          {/* Poster */}
          <div className="flex-shrink-0">
            <img
              src={posterUrl}
              alt={movie.title}
              className="w-64 rounded-lg shadow-2xl"
            />
          </div>

          {/* Details */}
          <div className="flex-grow space-y-6">
            <div>
              <h1 className="text-4xl md:text-5xl font-bold text-white mb-2">
                {movie.title}
              </h1>
              {movie.tagline && (
                <p className="text-gray-400 italic text-lg">{movie.tagline}</p>
              )}
            </div>

            {/* Meta Info */}
            <div className="flex flex-wrap gap-4 text-gray-300">
              {movie.vote_average && (
                <div className="flex items-center space-x-2">
                  <FiStar className="text-yellow-500" />
                  <span className="font-semibold">{movie.vote_average.toFixed(1)}</span>
                </div>
              )}
              {movie.runtime && (
                <div className="flex items-center space-x-2">
                  <FiClock />
                  <span>{movie.runtime} min</span>
                </div>
              )}
              {movie.release_date && (
                <div className="flex items-center space-x-2">
                  <FiCalendar />
                  <span>{new Date(movie.release_date).getFullYear()}</span>
                </div>
              )}
            </div>

            {/* Genres */}
            {movie.genres && movie.genres.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {movie.genres.map((genre) => (
                  <span
                    key={genre.id}
                    className="px-4 py-2 bg-dark-light rounded-full text-sm text-gray-300"
                  >
                    {genre.name}
                  </span>
                ))}
              </div>
            )}

            {/* Overview */}
            <div>
              <h2 className="text-2xl font-bold text-white mb-3">Overview</h2>
              <p className="text-gray-300 leading-relaxed">{movie.overview}</p>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap gap-4">
              <button 
                onClick={() => setShowPlayer(true)}
                className="flex items-center space-x-2 bg-primary hover:bg-primary-hover text-white px-8 py-3 rounded-lg font-semibold transition-colors"
              >
                <FiPlay />
                <span>Watch Now</span>
              </button>
              <button
                onClick={() => addToFavorites(movie)}
                className={`flex items-center space-x-2 px-8 py-3 rounded-lg font-semibold transition-colors ${
                  isFavorite(movie.id)
                    ? 'bg-primary text-white'
                    : 'bg-dark-light text-white hover:bg-dark-lighter'
                }`}
              >
                <FiHeart className={isFavorite(movie.id) ? 'fill-current' : ''} />
                <span>{isFavorite(movie.id) ? 'Remove from Favorites' : 'Add to Favorites'}</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Video Player Modal */}
      {showPlayer && (
        <VideoPlayer
          wootlyUrl={movie.wootly_url}
          doodUrl={movie.dood_url}
          title={movie.title}
          movieId={movie.id}
          type="movie"
          onClose={() => setShowPlayer(false)}
        />
      )}
    </div>
  );
};

export default MovieDetail;