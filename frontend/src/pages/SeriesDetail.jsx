import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { seriesAPI } from '../services/api';
import { FiStar, FiClock, FiCalendar, FiHeart, FiPlay, FiArrowLeft, FiChevronDown, FiChevronUp } from 'react-icons/fi';
import { useMovies } from '../context/MovieContext';
import VideoPlayer from '../components/VideoPlayer';

const SeriesDetail = () => {
  const { id } = useParams();
  const [series, setSeries] = useState(null);
  const [loading, setLoading] = useState(true);
  const [expandedSeasons, setExpandedSeasons] = useState({});
  const [showPlayer, setShowPlayer] = useState(false);
  const [selectedEpisode, setSelectedEpisode] = useState(null);
  const { addToFavorites, isFavorite } = useMovies();

  const handleWatchEpisode = (episode, seasonNumber) => {
    setSelectedEpisode({ ...episode, seasonNumber });
    setShowPlayer(true);
  };

  const toggleSeason = (seasonNumber) => {
    setExpandedSeasons(prev => ({
      ...prev,
      [seasonNumber]: !prev[seasonNumber]
    }));
  };

  useEffect(() => {
    fetchSeriesDetails();
  }, [id]);

  const fetchSeriesDetails = async () => {
    try {
      setLoading(true);
      const data = await seriesAPI.getSeriesById(id);
      setSeries(data);
    } catch (error) {
      console.error('Error fetching series details:', error);
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

  if (!series) {
    return (
      <div className="min-h-screen pt-24 pb-12 flex items-center justify-center">
        <p className="text-gray-400 text-xl">Series not found</p>
      </div>
    );
  }

  const backdropUrl = series.backdrop_path
    ? `https://image.tmdb.org/t/p/original${series.backdrop_path}`
    : '';
  const posterUrl = series.poster_path
    ? `https://image.tmdb.org/t/p/w500${series.poster_path}`
    : '';

  return (
    <div className="min-h-screen">
      {/* Backdrop */}
      <div className="relative h-[60vh]">
        {backdropUrl && (
          <img
            src={backdropUrl}
            alt={series.title || series.name}
            className="w-full h-full object-cover"
          />
        )}
        <div className="absolute inset-0 bg-gradient-to-t from-dark via-dark/70 to-transparent" />
        
        {/* Back Button */}
        <Link
          to="/series"
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
              alt={series.title || series.name}
              className="w-64 rounded-lg shadow-2xl"
            />
          </div>

          {/* Details */}
          <div className="flex-grow space-y-6">
            <div>
              <h1 className="text-4xl md:text-5xl font-bold text-white mb-2">
                {series.title || series.name}
              </h1>
              {series.tagline && (
                <p className="text-gray-400 italic text-lg">{series.tagline}</p>
              )}
            </div>

            {/* Meta Info */}
            <div className="flex flex-wrap gap-4 text-gray-300">
              {series.vote_average && (
                <div className="flex items-center space-x-2">
                  <FiStar className="text-yellow-500" />
                  <span className="font-semibold">{series.vote_average.toFixed(1)}</span>
                </div>
              )}
              {series.number_of_seasons && (
                <div className="flex items-center space-x-2">
                  <span>{series.number_of_seasons} Seasons</span>
                </div>
              )}
              {series.number_of_episodes && (
                <div className="flex items-center space-x-2">
                  <span>{series.number_of_episodes} Episodes</span>
                </div>
              )}
              {series.release_date && (
                <div className="flex items-center space-x-2">
                  <FiCalendar />
                  <span>{new Date(series.release_date).getFullYear()}</span>
                </div>
              )}
              {series.status && (
                <div className="px-3 py-1 bg-primary rounded-full text-sm">
                  {series.status}
                </div>
              )}
            </div>

            {/* Genres */}
            {series.genres && series.genres.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {series.genres.map((genre) => (
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
              <p className="text-gray-300 leading-relaxed">{series.overview}</p>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap gap-4">
              <button
                onClick={() => addToFavorites(series)}
                className={`flex items-center space-x-2 px-8 py-3 rounded-lg font-semibold transition-colors ${
                  isFavorite(series.id)
                    ? 'bg-primary text-white'
                    : 'bg-dark-light text-white hover:bg-dark-lighter'
                }`}
              >
                <FiHeart className={isFavorite(series.id) ? 'fill-current' : ''} />
                <span>{isFavorite(series.id) ? 'Remove from Favorites' : 'Add to Favorites'}</span>
              </button>
            </div>
          </div>
        </div>

        {/* Seasons and Episodes */}
        {series.seasons && series.seasons.length > 0 && (
          <div className="mt-12">
            <h2 className="text-3xl font-bold text-white mb-6">Seasons & Episodes</h2>
            <div className="space-y-4">
              {series.seasons.map((season) => (
                <div key={season.id} className="bg-dark-light rounded-lg overflow-hidden">
                  {/* Season Header */}
                  <button
                    onClick={() => toggleSeason(season.season_number)}
                    className="w-full flex items-center justify-between p-6 hover:bg-dark-lighter transition-colors"
                  >
                    <div className="flex items-center space-x-4">
                      <div className="text-left">
                        <h3 className="text-xl font-bold text-white">
                          {season.name || `Season ${season.season_number}`}
                        </h3>
                        <p className="text-gray-400 text-sm mt-1">
                          {season.episode_count} Episodes
                          {season.air_date && ` • ${new Date(season.air_date).getFullYear()}`}
                        </p>
                      </div>
                    </div>
                    {expandedSeasons[season.season_number] ? (
                      <FiChevronUp className="text-white text-2xl" />
                    ) : (
                      <FiChevronDown className="text-white text-2xl" />
                    )}
                  </button>

                  {/* Episodes List */}
                  {expandedSeasons[season.season_number] && season.episodes && (
                    <div className="border-t border-gray-800">
                      {season.episodes.length > 0 ? (
                        <div className="divide-y divide-gray-800">
                          {season.episodes.map((episode) => (
                            <div
                              key={episode.id}
                              className="p-6 hover:bg-dark transition-colors"
                            >
                              <div className="flex items-start justify-between">
                                <div className="flex-1">
                                  <div className="flex items-center space-x-3 mb-2">
                                    <span className="text-primary font-bold text-lg">
                                      {episode.episode_number}
                                    </span>
                                    <h4 className="text-white font-semibold text-lg">
                                      {episode.name || `Episode ${episode.episode_number}`}
                                    </h4>
                                  </div>
                                  {episode.overview && (
                                    <p className="text-gray-400 text-sm leading-relaxed mb-2">
                                      {episode.overview}
                                    </p>
                                  )}
                                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                                    {episode.air_date && (
                                      <span className="flex items-center space-x-1">
                                        <FiCalendar size={14} />
                                        <span>{new Date(episode.air_date).toLocaleDateString()}</span>
                                      </span>
                                    )}
                                    {episode.vote_average > 0 && (
                                      <span className="flex items-center space-x-1">
                                        <FiStar size={14} className="text-yellow-500" />
                                        <span>{episode.vote_average.toFixed(1)}</span>
                                      </span>
                                    )}
                                  </div>
                                </div>
                                <button 
                                  onClick={() => handleWatchEpisode(episode, season.season_number)}
                                  className="ml-4 flex items-center space-x-2 bg-primary hover:bg-primary-hover text-white px-4 py-2 rounded-lg font-semibold transition-colors"
                                >
                                  <FiPlay size={16} />
                                  <span>Watch</span>
                                </button>
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="p-6 text-center text-gray-400">
                          No episodes available for this season
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Video Player Modal for Episodes */}
      {showPlayer && selectedEpisode && (
        <VideoPlayer
          wootlyUrl={selectedEpisode.wootly_url}
          doodUrl={selectedEpisode.dood_url}
          title={`${series.title} - S${selectedEpisode.seasonNumber}E${selectedEpisode.episode_number} - ${selectedEpisode.name}`}
          movieId={series.id}
          type="tv"
          seasonNumber={selectedEpisode.seasonNumber}
          episodeNumber={selectedEpisode.episode_number}
          onClose={() => {
            setShowPlayer(false);
            setSelectedEpisode(null);
          }}
        />
      )}
    </div>
  );
};

export default SeriesDetail;