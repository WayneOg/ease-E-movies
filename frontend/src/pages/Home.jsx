import { useEffect, useState } from 'react';
import { useMovies } from '../context/MovieContext';
import { movieAPI } from '../services/api';
import Hero from '../components/Hero';
import MovieGrid from '../components/MovieGrid';

const Home = () => {
  const { trending, loading: trendingLoading } = useMovies();
  const [popular, setPopular] = useState([]);
  const [topRated, setTopRated] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [popularData, topRatedData] = await Promise.all([
          movieAPI.getPopular(),
          movieAPI.getTopRated(),
        ]);
        setPopular(popularData.results || popularData);
        setTopRated(topRatedData.results || topRatedData);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <Hero movies={trending} />

      {/* Content Sections */}
      <div className="container mx-auto px-4 py-12 space-y-12">
        {/* Trending */}
        <section>
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-6">
            Trending Now
          </h2>
          <MovieGrid movies={trending} loading={trendingLoading} />
        </section>

        {/* Popular */}
        <section>
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-6">
            Popular Movies
          </h2>
          <MovieGrid movies={popular} loading={loading} />
        </section>

        {/* Top Rated */}
        <section>
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-6">
            Top Rated
          </h2>
          <MovieGrid movies={topRated} loading={loading} />
        </section>
      </div>
    </div>
  );
};

export default Home;