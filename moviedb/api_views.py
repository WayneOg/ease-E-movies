"""
API Views for React Frontend
Returns JSON responses for all endpoints
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from .models import Movie, Series, Genre, Season, Episode
from .utils import (
    fetch_movies_by_genre,
    fetch_latest_movies,
    fetch_popular_movies,
    fetch_movie_details,
    fetch_series_details,
    search_movies,
    search_series,
    GENRE_IDS,
    make_api_request,
    TMDB_API_KEY
)
import logging

logger = logging.getLogger(__name__)


def serialize_movie(movie_data, include_streaming=False):
    """Convert movie data to JSON-serializable format"""
    result = {
        'id': movie_data.get('id'),
        'title': movie_data.get('title'),
        'poster_path': movie_data.get('poster_path'),
        'backdrop_path': movie_data.get('backdrop_path'),
        'overview': movie_data.get('overview', ''),
        'vote_average': movie_data.get('vote_average', 0),
        'release_date': movie_data.get('release_date'),
        'runtime': movie_data.get('runtime'),
        'genres': movie_data.get('genres', []),
        'tagline': movie_data.get('tagline', ''),
    }
    
    # Include streaming URLs if requested (for detail view)
    if include_streaming:
        result['wootly_url'] = movie_data.get('wootly_url')
        result['dood_url'] = movie_data.get('dood_url')
    
    return result


def serialize_series(series_data, include_seasons=False):
    """Convert series data to JSON-serializable format"""
    result = {
        'id': series_data.get('id'),
        'title': series_data.get('name') or series_data.get('title'),
        'name': series_data.get('name') or series_data.get('title'),
        'poster_path': series_data.get('poster_path'),
        'backdrop_path': series_data.get('backdrop_path'),
        'overview': series_data.get('overview', ''),
        'vote_average': series_data.get('vote_average', 0),
        'first_air_date': series_data.get('first_air_date'),
        'release_date': series_data.get('first_air_date'),
        'number_of_seasons': series_data.get('number_of_seasons'),
        'number_of_episodes': series_data.get('number_of_episodes'),
        'genres': series_data.get('genres', []),
        'tagline': series_data.get('tagline', ''),
        'status': series_data.get('status', ''),
    }
    
    # Include seasons and episodes if requested (for detail view)
    if include_seasons:
        result['seasons'] = series_data.get('seasons', [])
    
    return result


@require_http_methods(["GET"])
def api_movies_list(request):
    """Get list of all movies"""
    try:
        page = int(request.GET.get('page', 1))
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page={page}'
        data = make_api_request(url)
        
        movies = [serialize_movie(movie) for movie in data.get('results', [])]
        
        return JsonResponse({
            'results': movies,
            'page': page,
            'total_pages': data.get('total_pages', 1),
            'total_results': data.get('total_results', 0),
        })
    except Exception as e:
        logger.error(f"Error fetching movies: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_movie_detail(request, pk):
    """Get movie details by ID"""
    try:
        movie_data = fetch_movie_details(pk)
        if not movie_data:
            return JsonResponse({'error': 'Movie not found'}, status=404)
        
        # Check if movie exists in database with streaming URLs
        try:
            db_movie = Movie.objects.get(id=pk)
            movie_data['wootly_url'] = db_movie.wootly_url
            movie_data['dood_url'] = db_movie.dood_url
        except Movie.DoesNotExist:
            movie_data['wootly_url'] = None
            movie_data['dood_url'] = None
        
        return JsonResponse(serialize_movie(movie_data, include_streaming=True))
    except Exception as e:
        logger.error(f"Error fetching movie {pk}: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_series_list(request):
    """Get list of all TV series"""
    try:
        page = int(request.GET.get('page', 1))
        url = f'https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US&page={page}'
        data = make_api_request(url)
        
        series = [serialize_series(show) for show in data.get('results', [])]
        
        return JsonResponse({
            'results': series,
            'page': page,
            'total_pages': data.get('total_pages', 1),
            'total_results': data.get('total_results', 0),
        })
    except Exception as e:
        logger.error(f"Error fetching series: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_series_detail(request, pk):
    """Get series details by ID with seasons and episodes"""
    try:
        series_data = fetch_series_details(pk)
        if not series_data:
            return JsonResponse({'error': 'Series not found'}, status=404)
        
        # Fetch seasons and episodes from database if available
        try:
            db_series = Series.objects.get(id=pk)
            seasons_data = []
            
            # Get all seasons ordered by season number
            seasons = Season.objects.filter(series=db_series).order_by('season_number')
            
            for season in seasons:
                # Get all episodes for this season ordered by episode number
                episodes = Episode.objects.filter(season=season).order_by('episode_number')
                
                episodes_data = [{
                    'id': episode.id,
                    'episode_number': episode.episode_number,
                    'name': episode.name,
                    'overview': episode.overview,
                    'air_date': episode.air_date.isoformat() if episode.air_date else None,
                    'vote_average': episode.vote_average,
                } for episode in episodes]
                
                seasons_data.append({
                    'id': season.id,
                    'season_number': season.season_number,
                    'name': season.name,
                    'overview': season.overview,
                    'air_date': season.air_date.isoformat() if season.air_date else None,
                    'episode_count': season.episode_count,
                    'episodes': episodes_data,
                })
            
            series_data['seasons'] = seasons_data
        except Series.DoesNotExist:
            series_data['seasons'] = []
        
        return JsonResponse(serialize_series(series_data, include_seasons=True))
    except Exception as e:
        logger.error(f"Error fetching series {pk}: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_search(request):
    """Search for movies and series"""
    try:
        query = request.GET.get('q', '').strip()
        if not query:
            return JsonResponse({'error': 'Query parameter required'}, status=400)
        
        # Search movies
        movies_data = search_movies(query)
        movies = [serialize_movie(movie) for movie in movies_data]
        
        # Search series
        series_data = search_series(query)
        series = [serialize_series(show) for show in series_data]
        
        return JsonResponse({
            'movies': movies,
            'series': series,
            'query': query,
        })
    except Exception as e:
        logger.error(f"Error searching for '{query}': {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_trending(request):
    """Get trending movies"""
    try:
        url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}'
        data = make_api_request(url)
        
        movies = [serialize_movie(movie) for movie in data.get('results', [])]
        
        return JsonResponse({'results': movies})
    except Exception as e:
        logger.error(f"Error fetching trending: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_popular(request):
    """Get popular movies"""
    try:
        movies_data = fetch_popular_movies()
        movies = [serialize_movie(movie) for movie in movies_data]
        
        return JsonResponse({'results': movies})
    except Exception as e:
        logger.error(f"Error fetching popular: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_top_rated(request):
    """Get top rated movies"""
    try:
        url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=en-US&page=1'
        data = make_api_request(url)
        
        movies = [serialize_movie(movie) for movie in data.get('results', [])]
        
        return JsonResponse({'results': movies})
    except Exception as e:
        logger.error(f"Error fetching top rated: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_genre_movies(request, genre_name):
    """Get movies by genre"""
    try:
        # Map genre name to ID
        genre_map = {
            'action': GENRE_IDS.get('action', 28),
            'comedy': GENRE_IDS.get('comedy', 35),
            'horror': GENRE_IDS.get('horror', 27),
            'scifi': GENRE_IDS.get('science_fiction', 878),
            'romance': GENRE_IDS.get('romance', 10749),
            'animation': GENRE_IDS.get('animation', 16),
            'drama': GENRE_IDS.get('drama', 18),
            'thriller': GENRE_IDS.get('thriller', 53),
            'fantasy': GENRE_IDS.get('fantasy', 14),
            'adventure': GENRE_IDS.get('adventure', 12),
            'crime': GENRE_IDS.get('crime', 80),
            'mystery': GENRE_IDS.get('mystery', 9648),
            'family': GENRE_IDS.get('family', 10751),
            'documentary': GENRE_IDS.get('documentary', 99),
            'history': GENRE_IDS.get('history', 36),
        }
        
        genre_id = genre_map.get(genre_name.lower())
        if not genre_id:
            return JsonResponse({'error': 'Invalid genre'}, status=400)
        
        page = int(request.GET.get('page', 1))
        movies_data = fetch_movies_by_genre(genre_id, page)
        movies = [serialize_movie(movie) for movie in movies_data]
        
        return JsonResponse({
            'results': movies,
            'genre': genre_name,
        })
    except Exception as e:
        logger.error(f"Error fetching {genre_name} movies: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_latest(request):
    """Get latest movies"""
    try:
        movies_data = fetch_latest_movies()
        movies = [serialize_movie(movie) for movie in movies_data]
        
        return JsonResponse({'results': movies})
    except Exception as e:
        logger.error(f"Error fetching latest: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)