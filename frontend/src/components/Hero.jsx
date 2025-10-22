import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FiPlay, FiInfo, FiStar } from 'react-icons/fi';

const Hero = ({ movies }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    if (!movies || movies.length === 0) return;

    const interval = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % movies.length);
      setIsLoaded(false);
    }, 8000);

    return () => clearInterval(interval);
  }, [movies]);

  if (!movies || movies.length === 0) {
    return (
      <div className="relative h-[70vh] bg-dark-light animate-pulse">
        <div className="skeleton w-full h-full" />
      </div>
    );
  }

  const movie = movies[currentIndex];
  const backdropUrl = movie.backdrop_path
    ? `https://image.tmdb.org/t/p/original${movie.backdrop_path}`
    : '';

  return (
    <div className="relative h-[70vh] overflow-hidden">
      {/* Background Image */}
      <div className="absolute inset-0">
        {backdropUrl && (
          <img
            src={backdropUrl}
            alt={movie.title || movie.name}
            onLoad={() => setIsLoaded(true)}
            className={`w-full h-full object-cover transition-opacity duration-1000 ${
              isLoaded ? 'opacity-100' : 'opacity-0'
            }`}
          />
        )}
        <div className="absolute inset-0 bg-gradient-to-r from-black via-black/70 to-transparent" />
        <div className="absolute inset-0 bg-gradient-to-t from-dark via-transparent to-transparent" />
      </div>

      {/* Content */}
      <div className="relative h-full container mx-auto px-4 flex items-center">
        <div className="max-w-2xl space-y-4 animate-fadeIn">
          <h1 className="text-4xl md:text-6xl font-bold text-white leading-tight">
            {movie.title || movie.name}
          </h1>

          {movie.vote_average && (
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-1">
                <FiStar className="text-yellow-500" />
                <span className="text-white font-semibold">
                  {movie.vote_average.toFixed(1)}
                </span>
              </div>
              {movie.release_date && (
                <span className="text-gray-300">
                  {new Date(movie.release_date).getFullYear()}
                </span>
              )}
            </div>
          )}

          <p className="text-gray-300 text-lg line-clamp-3 max-w-xl">
            {movie.overview}
          </p>

          <div className="flex space-x-4 pt-4">
            <Link
              to={`/movie/${movie.id}`}
              className="flex items-center space-x-2 bg-primary hover:bg-primary-hover text-white px-8 py-3 rounded-lg font-semibold transition-colors"
            >
              <FiPlay />
              <span>Watch Now</span>
            </Link>
            <Link
              to={`/movie/${movie.id}`}
              className="flex items-center space-x-2 bg-white/20 hover:bg-white/30 backdrop-blur-md text-white px-8 py-3 rounded-lg font-semibold transition-colors"
            >
              <FiInfo />
              <span>More Info</span>
            </Link>
          </div>
        </div>
      </div>

      {/* Indicators */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 flex space-x-2">
        {movies.slice(0, 5).map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentIndex(index)}
            className={`w-2 h-2 rounded-full transition-all ${
              index === currentIndex ? 'bg-white w-8' : 'bg-white/50'
            }`}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

export default Hero;