"""
Utility functions for the moviedb app.
This module contains helper functions for API calls, caching, and data processing.
"""

import requests
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key as make_key
from django.conf import settings
from requests.exceptions import RequestException
from typing import Optional, Dict, List, Any
import logging

logger = logging.getLogger(__name__)

# API Configuration
TMDB_API_KEY = settings.TMDB_API_KEY
TRAKT_CLIENT_ID = settings.TRAKT_CLIENT_ID
OMDB_API_KEY = settings.OMDB_API_KEY
TMDB_BASE_URL = "https://api.themoviedb.org/3"


def make_api_request(url: str, cache_timeout: int = 3600) -> Optional[Dict[str, Any]]:
    """
    Make an API request with caching support.
    
    Args:
        url: The API endpoint URL
        cache_timeout: Cache timeout in seconds (default: 1 hour)
        
    Returns:
        JSON response as dictionary or None if request fails
    """
    cache_key = make_key('api_request', url)
    
    # Try to get cached response
    cached_response = cache.get(cache_key)
    if cached_response:
        logger.debug(f"Cache hit for URL: {url}")
        return cached_response
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Cache the response
        cache.set(cache_key, data, cache_timeout)
        logger.debug(f"Cached response for URL: {url}")
        
        return data
    except RequestException as e:
        logger.error(f"API request failed for URL {url}: {str(e)}")
        return None
    except ValueError as e:
        logger.error(f"Invalid JSON response from URL {url}: {str(e)}")
        return None


def fetch_movies_by_genre(genre_id: int, page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Fetch movies by genre ID from TMDb API.
    
    Args:
        genre_id: TMDb genre ID
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of movie dictionaries
    """
    url = (
        f'{TMDB_BASE_URL}/discover/movie'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&with_genres={genre_id}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    return data.get('results', []) if data else []


def fetch_latest_movies(page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Fetch latest movies sorted by release date.
    
    Args:
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of movie dictionaries with posters
    """
    from datetime import datetime
    
    today = datetime.today().strftime('%Y-%m-%d')
    url = (
        f'{TMDB_BASE_URL}/discover/movie'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&sort_by=release_date.desc'
        f'&release_date.lte={today}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    if not data:
        return []
    
    movies = data.get('results', [])
    # Filter out movies without posters
    return [movie for movie in movies if movie.get('poster_path')]


def fetch_popular_movies(page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Fetch popular movies from TMDb API.
    
    Args:
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of movie dictionaries
    """
    url = (
        f'{TMDB_BASE_URL}/movie/popular'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    return data.get('results', []) if data else []


def fetch_series_by_genre(genre_id: int, page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Fetch TV series by genre ID from TMDb API.
    
    Args:
        genre_id: TMDb genre ID
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of series dictionaries
    """
    url = (
        f'{TMDB_BASE_URL}/discover/tv'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&with_genres={genre_id}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    return data.get('results', []) if data else []


# Genre ID mapping for easy reference
GENRE_IDS = {
    'action': 28,
    'adventure': 12,
    'animation': 16,
    'comedy': 35,
    'crime': 80,
    'documentary': 99,
    'drama': 18,
    'family': 10751,
    'fantasy': 14,
    'history': 36,
    'horror': 27,
    'music': 10402,
    'mystery': 9648,
    'romance': 10749,
    'science_fiction': 878,
    'thriller': 53,
    'war': 10752,
    'western': 37,
}


def get_genre_id(genre_name: str) -> Optional[int]:
    """
    Get TMDb genre ID by genre name.
    
    Args:
        genre_name: Genre name (e.g., 'action', 'horror')
        
    Returns:
        Genre ID or None if not found
    """
    return GENRE_IDS.get(genre_name.lower())


def fetch_movie_details(movie_id: int, language: str = 'en-US') -> Optional[Dict[str, Any]]:
    """
    Fetch detailed information about a specific movie.
    
    Args:
        movie_id: TMDb movie ID
        language: Language code (default: en-US)
        
    Returns:
        Movie details dictionary or None if not found
    """
    url = (
        f'{TMDB_BASE_URL}/movie/{movie_id}'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
    )
    
    return make_api_request(url)


def fetch_series_details(series_id: int, language: str = 'en-US') -> Optional[Dict[str, Any]]:
    """
    Fetch detailed information about a specific TV series.
    
    Args:
        series_id: TMDb series ID
        language: Language code (default: en-US)
        
    Returns:
        Series details dictionary or None if not found
    """
    url = (
        f'{TMDB_BASE_URL}/tv/{series_id}'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
    )
    
    return make_api_request(url)


def search_movies(query: str, page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Search for movies by query string.
    
    Args:
        query: Search query
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of movie dictionaries
    """
    import urllib.parse
    
    encoded_query = urllib.parse.quote(query)
    url = (
        f'{TMDB_BASE_URL}/search/movie'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&query={encoded_query}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    return data.get('results', []) if data else []


def search_series(query: str, page: int = 1, language: str = 'en-US') -> List[Dict[str, Any]]:
    """
    Search for TV series by query string.
    
    Args:
        query: Search query
        page: Page number for pagination
        language: Language code (default: en-US)
        
    Returns:
        List of series dictionaries
    """
    import urllib.parse
    
    encoded_query = urllib.parse.quote(query)
    url = (
        f'{TMDB_BASE_URL}/search/tv'
        f'?api_key={TMDB_API_KEY}'
        f'&language={language}'
        f'&query={encoded_query}'
        f'&page={page}'
    )
    
    data = make_api_request(url)
    return data.get('results', []) if data else []