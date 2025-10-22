import { FiGithub, FiTwitter, FiFacebook, FiInstagram } from 'react-icons/fi';

const Footer = () => {
  return (
    <footer className="bg-dark-light border-t border-gray-800 mt-20">
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <span className="text-3xl">🎬</span>
              <span className="text-xl font-bold gradient-text">ease-E-movies</span>
            </div>
            <p className="text-gray-400 text-sm">
              Your ultimate destination for movies and TV series streaming.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <a href="/" className="text-gray-400 hover:text-white transition-colors">
                  Home
                </a>
              </li>
              <li>
                <a href="/movies" className="text-gray-400 hover:text-white transition-colors">
                  Movies
                </a>
              </li>
              <li>
                <a href="/series" className="text-gray-400 hover:text-white transition-colors">
                  TV Series
                </a>
              </li>
              <li>
                <a href="/search" className="text-gray-400 hover:text-white transition-colors">
                  Search
                </a>
              </li>
            </ul>
          </div>

          {/* Genres */}
          <div>
            <h3 className="text-white font-semibold mb-4">Popular Genres</h3>
            <ul className="space-y-2">
              <li>
                <a href="/genre/action" className="text-gray-400 hover:text-white transition-colors">
                  Action
                </a>
              </li>
              <li>
                <a href="/genre/comedy" className="text-gray-400 hover:text-white transition-colors">
                  Comedy
                </a>
              </li>
              <li>
                <a href="/genre/horror" className="text-gray-400 hover:text-white transition-colors">
                  Horror
                </a>
              </li>
              <li>
                <a href="/genre/scifi" className="text-gray-400 hover:text-white transition-colors">
                  Sci-Fi
                </a>
              </li>
            </ul>
          </div>

          {/* Social */}
          <div>
            <h3 className="text-white font-semibold mb-4">Follow Us</h3>
            <div className="flex space-x-4">
              <a
                href="#"
                className="text-gray-400 hover:text-white transition-colors text-xl"
                aria-label="Facebook"
              >
                <FiFacebook />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white transition-colors text-xl"
                aria-label="Twitter"
              >
                <FiTwitter />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white transition-colors text-xl"
                aria-label="Instagram"
              >
                <FiInstagram />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white transition-colors text-xl"
                aria-label="GitHub"
              >
                <FiGithub />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-gray-400 text-sm">
            © {new Date().getFullYear()} ease-E-movies. All rights reserved.
          </p>
          <p className="text-gray-500 text-xs mt-2">
            Built with React, Tailwind CSS, and Django
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;