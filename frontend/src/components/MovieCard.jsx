import { Link } from 'react-router-dom';
import { FiStar, FiHeart } from 'react-icons/fi';
import { useMovies } from '../context/MovieContext';
import { useInView } from 'react-intersection-observer';
import { useState } from 'react';

const MovieCard = ({ movie, type = 'movie' }) => {
  const { addToFavorites, isFavorite } = useMovies();
  const [imageLoaded, setImageLoaded] = useState(false);
  const { ref, inView } = useInView({
    triggerOnce: true,
    threshold: 0.1,
  });

  const posterUrl = movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    : '/placeholder-poster.jpg';

  const title = movie.title || movie.name;
  const releaseDate = movie.release_date || movie.first_air_date;
  const year = releaseDate ? new Date(releaseDate).getFullYear() : 'N/A';
  const rating = movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A';

  const getRatingColor = (rating) => {
    if (rating >= 7) return 'text-green-500';
    if (rating >= 5) return 'text-yellow-500';
    return 'text-red-500';
  };

  const handleFavoriteClick = (e) => {
    e.preventDefault();
    addToFavorites(movie);
  };

  return (
    <div ref={ref} className="group relative animate-fadeIn">
      <Link to={`/${type}/${movie.id}`} className="block">
        <div className="relative overflow-hidden rounded-lg shadow-lg hover-scale">
          {/* Skeleton Loader */}
          {!imageLoaded && (
            <div className="skeleton w-full aspect-[2/3] rounded-lg" />
          )}

          {/* Poster Image */}
          {inView && (
            <img
              src={posterUrl}
              alt={title}
              onLoad={() => setImageLoaded(true)}
              className={`w-full aspect-[2/3] object-cover transition-opacity duration-300 ${
                imageLoaded ? 'opacity-100' : 'opacity-0'
              }`}
            />
          )}

          {/* Overlay */}
          <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
            <div className="absolute bottom-0 left-0 right-0 p-4">
              <h3 className="text-white font-semibold text-lg mb-2 line-clamp-2">
                {title}
              </h3>
              <div className="flex items-center justify-between">
                <span className="text-gray-300 text-sm">{year}</span>
                <div className="flex items-center space-x-1">
                  <FiStar className={getRatingColor(rating)} />
                  <span className={`text-sm font-semibold ${getRatingColor(rating)}`}>
                    {rating}
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Favorite Button */}
          <button
            onClick={handleFavoriteClick}
            className={`absolute top-2 right-2 p-2 rounded-full backdrop-blur-md transition-all duration-300 ${
              isFavorite(movie.id)
                ? 'bg-primary text-white'
                : 'bg-black/50 text-white hover:bg-primary'
            }`}
            aria-label="Add to favorites"
          >
            <FiHeart className={isFavorite(movie.id) ? 'fill-current' : ''} />
          </button>
        </div>
      </Link>

      {/* Title Below Card */}
      <div className="mt-2">
        <h3 className="text-white font-medium text-sm line-clamp-1">{title}</h3>
        <div className="flex items-center justify-between mt-1">
          <span className="text-gray-400 text-xs">{year}</span>
          <div className="flex items-center space-x-1">
            <FiStar className={`text-xs ${getRatingColor(rating)}`} />
            <span className={`text-xs ${getRatingColor(rating)}`}>{rating}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MovieCard;