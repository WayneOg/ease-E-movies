import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { movieAPI } from '../services/api';
import MovieGrid from '../components/MovieGrid';
import { FiSearch } from 'react-icons/fi';

const Search = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [query, setQuery] = useState(searchParams.get('q') || '');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const searchQuery = searchParams.get('q');
    if (searchQuery) {
      setQuery(searchQuery);
      performSearch(searchQuery);
    }
  }, [searchParams]);

  const performSearch = async (searchQuery) => {
    if (!searchQuery.trim()) return;

    try {
      setLoading(true);
      const data = await movieAPI.searchMovies(searchQuery);
      setResults(data.results || data);
    } catch (error) {
      console.error('Error searching:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      setSearchParams({ q: query });
    }
  };

  return (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container mx-auto px-4">
        {/* Search Header */}
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Search Movies & Series
          </h1>

          {/* Search Form */}
          <form onSubmit={handleSubmit} className="max-w-2xl">
            <div className="relative">
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search for movies, series..."
                className="w-full bg-dark-light text-white px-6 py-4 pr-14 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary text-lg"
                autoFocus
              />
              <button
                type="submit"
                className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white text-xl"
              >
                <FiSearch />
              </button>
            </div>
          </form>
        </div>

        {/* Results */}
        {searchParams.get('q') && (
          <div>
            <h2 className="text-2xl font-semibold text-white mb-6">
              {loading ? (
                'Searching...'
              ) : (
                <>
                  Results for "<span className="text-primary">{searchParams.get('q')}</span>"
                  {results.length > 0 && (
                    <span className="text-gray-400 text-lg ml-2">
                      ({results.length} found)
                    </span>
                  )}
                </>
              )}
            </h2>

            {!loading && results.length === 0 && (
              <div className="text-center py-20">
                <p className="text-gray-400 text-xl mb-4">
                  No results found for "{searchParams.get('q')}"
                </p>
                <p className="text-gray-500">
                  Try different keywords or check your spelling
                </p>
              </div>
            )}

            <MovieGrid movies={results} loading={loading} />
          </div>
        )}
      </div>
    </div>
  );
};

export default Search;