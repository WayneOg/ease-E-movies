import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FiSearch, FiMenu, FiX, FiFilm, FiTv, FiHome, FiHeart } from 'react-icons/fi';

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery)}`);
      setSearchQuery('');
      setIsMobileMenuOpen(false);
    }
  };

  const genres = [
    { name: 'Action', path: '/genre/action' },
    { name: 'Comedy', path: '/genre/comedy' },
    { name: 'Horror', path: '/genre/horror' },
    { name: 'Sci-Fi', path: '/genre/scifi' },
    { name: 'Romance', path: '/genre/romance' },
    { name: 'Animation', path: '/genre/animation' },
  ];

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? 'bg-dark/95 backdrop-blur-md shadow-lg' : 'bg-transparent'
      }`}
    >
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2 group">
            <span className="text-3xl">🎬</span>
            <span className="text-xl font-bold gradient-text">ease-E-movies</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <Link
              to="/"
              className="flex items-center space-x-1 text-gray-300 hover:text-white transition-colors"
            >
              <FiHome />
              <span>Home</span>
            </Link>
            <Link
              to="/movies"
              className="flex items-center space-x-1 text-gray-300 hover:text-white transition-colors"
            >
              <FiFilm />
              <span>Movies</span>
            </Link>
            <Link
              to="/series"
              className="flex items-center space-x-1 text-gray-300 hover:text-white transition-colors"
            >
              <FiTv />
              <span>Series</span>
            </Link>

            {/* Genres Dropdown */}
            <div className="relative group">
              <button className="text-gray-300 hover:text-white transition-colors">
                Genres ▾
              </button>
              <div className="absolute top-full left-0 mt-2 w-48 bg-dark-light rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                {genres.map((genre) => (
                  <Link
                    key={genre.name}
                    to={genre.path}
                    className="block px-4 py-2 text-gray-300 hover:bg-dark-lighter hover:text-white transition-colors first:rounded-t-lg last:rounded-b-lg"
                  >
                    {genre.name}
                  </Link>
                ))}
              </div>
            </div>
          </div>

          {/* Search Bar */}
          <form onSubmit={handleSearch} className="hidden md:flex items-center">
            <div className="relative">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search movies..."
                className="bg-dark-light text-white px-4 py-2 pr-10 rounded-full focus:outline-none focus:ring-2 focus:ring-primary w-64 transition-all"
              />
              <button
                type="submit"
                className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
              >
                <FiSearch />
              </button>
            </div>
          </form>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="md:hidden text-white text-2xl"
          >
            {isMobileMenuOpen ? <FiX /> : <FiMenu />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className="md:hidden bg-dark-light rounded-lg mt-2 p-4 animate-slideIn">
            <form onSubmit={handleSearch} className="mb-4">
              <div className="relative">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search movies..."
                  className="w-full bg-dark text-white px-4 py-2 pr-10 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                />
                <button
                  type="submit"
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400"
                >
                  <FiSearch />
                </button>
              </div>
            </form>

            <div className="space-y-2">
              <Link
                to="/"
                onClick={() => setIsMobileMenuOpen(false)}
                className="flex items-center space-x-2 text-gray-300 hover:text-white py-2"
              >
                <FiHome />
                <span>Home</span>
              </Link>
              <Link
                to="/movies"
                onClick={() => setIsMobileMenuOpen(false)}
                className="flex items-center space-x-2 text-gray-300 hover:text-white py-2"
              >
                <FiFilm />
                <span>Movies</span>
              </Link>
              <Link
                to="/series"
                onClick={() => setIsMobileMenuOpen(false)}
                className="flex items-center space-x-2 text-gray-300 hover:text-white py-2"
              >
                <FiTv />
                <span>Series</span>
              </Link>

              <div className="border-t border-gray-700 my-2 pt-2">
                <p className="text-gray-400 text-sm mb-2">Genres</p>
                {genres.map((genre) => (
                  <Link
                    key={genre.name}
                    to={genre.path}
                    onClick={() => setIsMobileMenuOpen(false)}
                    className="block text-gray-300 hover:text-white py-2 pl-4"
                  >
                    {genre.name}
                  </Link>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;