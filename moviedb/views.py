import requests
from bs4 import BeautifulSoup
import os
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key as make_key
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseServerError
from requests.exceptions import RequestException
from .models import Movie, Category, Genre, Series, Season, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from django.http import Http404
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import hashlib
from django.http import JsonResponse
import urllib.parse
from django.db import transaction
#from .service import SearchService



# Store API key as an environment variable
TRAKT_CLIENT_ID = settings.TRAKT_CLIENT_ID

os.environ['TMDb_API_KEY'] = '6bd5cd084c256cd81499c0dfc1e050d2'
API_KEY = os.environ.get('TMDb_API_KEY')

os.environ['OMDB_API_KEY'] = '39087f'
OMDB_API_KEY = os.environ.get('OMDb_API_KEY')

TMDB_BASE_URL = "https://api.themoviedb.org/3"

def make_api_request(url):
    cache_key = make_key('api_request', url)
    cache_timeout = 60 * 60  # 1 hour cache timeout

    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    cache.set(cache_key, response.json(), cache_timeout)
    return response.json()


def fetch_action_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=28&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_horror_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=27&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_animation_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=16&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_scifi_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=878&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_romance_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=10749&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_investigative_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=9648&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_family_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=10751&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_drama_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=18&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_comedy_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=35&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_history_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=36&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_thriller_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=53&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_documentary_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=99&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_fantasy_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=14&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_adventure_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=12&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()

def fetch_crime_movies(page=1):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres=80&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_latest_movies(page=1):
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&sort_by=release_date.desc&release_date.lte={today}&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        # Filter out movies without posters
        movies_with_posters = [movie for movie in movies if movie.get('poster_path')]
        return movies_with_posters
    else:
        response.raise_for_status()


def home(request):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1'
    data = make_api_request(url)
    movies = data['results']
    
    action_movies = fetch_action_movies()
    horror_movies = fetch_horror_movies()
    animation_movies = fetch_animation_movies()
    scifi_movies = fetch_scifi_movies()
    romance_movies = fetch_romance_movies()
    investigative_movies = fetch_investigative_movies()
    drama_movies = fetch_drama_movies()
    comedy_movies = fetch_comedy_movies()
    latest_movies = fetch_latest_movies()
    family_movies = fetch_family_movies()
    history_movies = fetch_history_movies()
    documentary_movies = fetch_documentary_movies()
    thriller_movies = fetch_thriller_movies()
    fantasy_movies = fetch_fantasy_movies()
    adventure_movies = fetch_adventure_movies()
    crime_movies = fetch_crime_movies()
    
    posters = [movie['poster_path'] for movie in movies]
    posters = [movie['poster_path'] for movie in action_movies]
    posters = [movie['poster_path'] for movie in horror_movies]
    posters = [movie['poster_path'] for movie in animation_movies]
    posters = [movie['poster_path'] for movie in scifi_movies]
    posters = [movie['poster_path'] for movie in romance_movies]
    posters = [movie['poster_path'] for movie in investigative_movies]
    posters = [movie['poster_path'] for movie in drama_movies]
    posters = [movie['poster_path'] for movie in comedy_movies]
    posters = [movie['poster_path'] for movie in latest_movies]
    posters = [movie['poster_path'] for movie in family_movies]
    posters = [movie['poster_path'] for movie in history_movies]
    posters = [movie['poster_path'] for movie in documentary_movies]
    posters = [movie['poster_path'] for movie in thriller_movies]
    posters = [movie['poster_path'] for movie in fantasy_movies]
    posters = [movie['poster_path'] for movie in adventure_movies]
    posters = [movie['poster_path'] for movie in crime_movies]
    
    context = {
        'movies': movies,
        'action_movies': action_movies,
        'horror_movies': horror_movies,
        'animation_movies': animation_movies,
        'scifi_movies': scifi_movies,
        'romance_movies': romance_movies,
        'investigative_movies': investigative_movies,
        'drama_movies': drama_movies,
        'comedy_movies': comedy_movies,
        'latest_movies': latest_movies,
        'family_movies': family_movies,
        'fantasy_movies': fantasy_movies,
        'adventure_movies': adventure_movies,
        'thriller_movies': thriller_movies,
        'documentary_movies': documentary_movies,
        'history_movies': history_movies,
        'crime_movies': crime_movies,
        'posters': posters,
    }
    
    return render(request, 'home.html', context)

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

    

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def genre_list(request):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US'
    genres_data = make_api_request(url).get('genres', [])
    for genre_data in genres_data:
        tmdb_id = genre_data.get('id')
        name = genre_data.get('name')
        Genre.objects.get_or_create(tmdb_id=tmdb_id, name=name)
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_movies(request, genre_id):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&with_genres={genre_id}'
    movies_data = make_api_request(url).get('results', [])
    for movie_data in movies_data:
        tmdb_id = movie_data.get('id')
        title = movie_data.get('title')
        overview = movie_data.get('overview', '')
        release_date = movie_data.get('release_date', '')
        poster_path = movie_data.get('poster_path', '')
        movie, _ = Movie.objects.get_or_create(
            tmdb_id=tmdb_id,
            title=title,
            defaults={
                'overview': overview,
                'release_date': release_date,
                'poster_path': poster_path,
            }
        )
        movie.genres.add(Genre.objects.get(tmdb_id=genre_id))
    movies = Movie.objects.filter(genres__tmdb_id=genre_id).distinct()
    return render(request, 'genre_movies.html', {'movies': movies})


class SearchService:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_movies_and_series(self, query):
        movies = self.search_movies(query)
        series = self.search_series(query)
        return movies, series

    def search_movies(self, query):
        movie_url = 'https://api.themoviedb.org/3/search/movie'
        movie_params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'query': query
        }
        try:
            movie_response = requests.get(movie_url, params=movie_params)
            movie_response.raise_for_status()
            movie_results = movie_response.json().get('results', [])
            movies = []
            for result in movie_results:
                if result.get('poster_path'):
                    movie, created = Movie.objects.update_or_create(
                        tmdb_id=result['id'],  # Using `tmdb_id` instead of `id`
                        defaults={
                            'title': result['title'],
                            'overview': result.get('overview', ''),
                            'release_date': result.get('release_date', None),
                            'poster_path': result.get('poster_path', ''),
                            'vote_average': result.get('vote_average', 0)
                        }
                    )
                    movies.append(movie)
            return movies
        except requests.RequestException as e:
            logger.error(f"Error fetching movie data: {str(e)}")
            return []

    def search_series(self, query):
        series_url = 'https://api.themoviedb.org/3/search/tv'
        series_params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'query': query
        }
        try:
            series_response = requests.get(series_url, params=series_params)
            series_response.raise_for_status()
            series_results = series_response.json().get('results', [])
            series = []
            for result in series_results:
                if result.get('poster_path'):
                    serie, created = Series.objects.update_or_create(
                        tmdb_id=result['id'],
                        defaults={
                            'title': result['name'],
                            'summary': result.get('overview', ''),
                            'release_date': result.get('first_air_date', None),
                            'poster': result.get('poster_path', ''),
                            'vote_average': result.get('vote_average', 0)
                        }
                    )
                    series.append(serie)
            return series
        except requests.RequestException as e:
            logger.error(f"Error fetching series data: {str(e)}")
            return []

def search_results(request):
    query = request.GET.get('query', '').strip()
    if not query:
        return render(request, 'search_results.html', {
            'movies': [],
            'series': [],
            'error': 'Please enter a search term.'
        })

    search_service = SearchService(api_key=API_KEY)
    try:
        movies, series = search_service.search_movies_and_series(query)
    except requests.RequestException as e:
        logger.error(f"Error fetching data: {str(e)}")
        return render(request, 'search_results.html', {
            'error': 'An error occurred while fetching the search results. Please try again later.'
        })

    if not movies and not series:
        return render(request, 'search_results.html', {
            'error': 'No results found for your search.',
            'query': query
        })

    return render(request, 'search_results.html', {
        'movies': movies,
        'series': series,
        'query': query
    })
    
    
# Utility function to generate a unique token
def generate_movie_token(movie_id):
    return hashlib.sha256(f"{movie_id}".encode()).hexdigest()

def movie_details(request, pk):
    try:
        # Fetch movie details from the TMDB API
        tmdb_api_key = API_KEY  # Replace with your actual API key
        url = f'https://api.themoviedb.org/3/movie/{pk}?api_key={tmdb_api_key}&language=en-US'
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        movie_data = response.json()

        # Extract movie details from API response
        movie_title = movie_data.get('title')
        movie_overview = movie_data.get('overview', '')
        movie_poster_path = movie_data.get('poster_path', '')
        movie_release_date = movie_data.get('release_date', '')
        movie_vote_average = movie_data.get('vote_average', 0)
        movie_genres = [genre['name'] for genre in movie_data.get('genres', [])]
        movie_runtime = movie_data.get('runtime', 0)
        movie_tagline = movie_data.get('tagline', '')
        movie_imdb_id = movie_data.get('imdb_id')

        # Create the full URL for the poster image
        full_poster_url = f'https://image.tmdb.org/t/p/w500{movie_poster_path}'

        # Create or update the Movie instance
        movie, created = Movie.objects.update_or_create(
            id=pk,
            defaults={
                'title': movie_title,
                'overview': movie_overview,
                'poster_path': full_poster_url,
                'release_date': movie_release_date,
                'vote_average': movie_vote_average,
                'runtime': movie_runtime,
                'tagline': movie_tagline,
                'imdb_id': movie_imdb_id,
                # Add other fields as needed
            }
        )

        # Generate a token for the movie
        movie_token = generate_movie_token(pk)

        context = {
            'movie': movie,
            'genres': movie_genres,
            'movie_token': movie_token,
        }
        return render(request, 'movie_details.html', context)

    except requests.RequestException as e:
        return render(request, 'error.html', {'error_message': f'Error fetching data from TMDB: {str(e)}'})
    
    
    
def category_movies(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    movies = Movie.objects.filter(categories=category)
    context = {
        'category': category,
        'movies': movies
    }
    return render(request, 'category_movies.html', context)


def latest_movies(request):
    try:
        headers = {
            'Content-Type': 'application/json',
            'trakt-api-version': '2',
            'trakt-api-key': settings.TRAKT_CLIENT_ID,
        }
        url = 'https://api.trakt.tv/movies/trending'
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        print("API Response Data:", data)  # Debugging: Print the API response
        
        latest_movies = [
            {
                'id': movie['movie']['ids']['trakt'],  # Use Trakt ID for URL
                'title': movie['movie']['title'],
                'year': movie['movie']['year'],
                'overview': movie['movie']['overview'],
                'poster': movie['movie'].get('images', {}).get('poster', {}).get('full', 'default_poster_url')  # Handle missing poster
            }
            for movie in data
        ]
        print("Parsed Latest Movies:", latest_movies)  # Debugging: Print the parsed movie data
        
        context = {'latest_movies': latest_movies}
        return render(request, 'home.html', context)

    except requests.RequestException as e:
        return render(request, 'error.html', {'error_message': f'Error fetching data from Trakt.tv: {str(e)}'})
    
    
def get_movies_by_category(category_id, page_number):
    url = f'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': API_KEY,
        'with_genres': category_id,
        'page': page_number
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    movies = data.get('results', [])
    
    return movies

def paginate_movies(request, movies):
    paginator = Paginator(movies, 20)  # Show 20 movies per page
    page_number = request.GET.get('page')
    
    try:
        movies = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    
    return movies

def action_movies(request):
    category_id = 28  # Action movies
    page_number = request.GET.get('page', 1)
    
    try:
        # Assuming get_movies_by_category retrieves movies based on category_id and page_number
        action_movies = get_movies_by_category(category_id, page_number)
        
        # Assuming paginate_movies paginates the movies list
        action_movies = paginate_movies(request, action_movies)
    
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    context = {
        'action_movies': action_movies,
        'category': 'Action',
    }
    
    return render(request, 'movies.html', context)

def animation_movies(request):
    category_id = 16  # Animation movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Animation'})

def crime_movies(request):
    category_id = 80  # Crime movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Crime'})

def comedy_movies(request):
    category_id = 35  # Comedy movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Comedy'})

def drama_movies(request):
    category_id = 18  # Drama movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Drama'})

def horror_movies(request):
    category_id = 27  # Horror movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Horror'})

def family_movies(request):
    category_id = 10751  # Family movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Family'})

def romance_movies(request):
    category_id = 10749  # Romance movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Romance'})

def scifi_movies(request):
    category_id = 878  # Science Fiction movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Science Fiction'})

def history_movies(request):
    category_id = 36  # History Fiction movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'History'})

def documentary_movies(request):
    category_id = 99  # Documentary Fiction movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Documentary'})

def thriller_movies(request):
    category_id = 53  #  Thriller movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Thriller'})

def fantasy_movies(request):
    category_id = 14  # Fantasy movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Fantasy'})

def adventure_movies(request):
    category_id = 12  # Adventure movies
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Adventure'})

def investigative_movies(request):
    category_id = 9648  # Mystery movies (closest match for investigative)
    page_number = request.GET.get('page', 1)
    
    try:
        movies = get_movies_by_category(category_id, page_number)
        movies = paginate_movies(request, movies)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'movies.html', {'movies': movies, 'category': 'Investigative'})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'serie_list.html', {'series': series})


def fetch_streaming_link(movie_title):
    search_url = f'https://en.nexus-stream.com/movies'
    response = requests.get(search_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find_all('a', class_='movie-title')  # Adjust class or selector as needed

    for result in search_results:
        title = result.get_text().strip()
        if title.lower() == movie_title.lower():
            movie_page_url = result['href']
            movie_response = requests.get(movie_page_url)
            movie_response.raise_for_status()
            movie_soup = BeautifulSoup(movie_response.content, 'html.parser')

            streaming_link = movie_soup.find('a', class_='stream-link')['href']  # Adjust class or selector as needed
            return streaming_link

    return None


def serie_list(request):
    series = Series.objects.all()
    return render(request, 'series_list.html', {'series': series})

def series_genre_list(request):
    url = f'https://api.themoviedb.org/3/genre/tv/list?api_key={API_KEY}&language=en-US'
    genres_data = make_api_request(url).get('genres', [])
    for genre_data in genres_data:
        tmdb_id = genre_data.get('id')
        name = genre_data.get('name')
        Genre.objects.get_or_create(tmdb_id=tmdb_id, name=name)
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_series(request, genre_id):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&with_genres={genre_id}'
    series_data = make_api_request(url).get('results', [])
    for serie_data in series_data:
        tmdb_id = serie_data.get('id')
        title = serie_data.get('title')
        overview = serie_data.get('overview', '')
        release_date = serie_data.get('release_date', '')
        poster_path = serie_data.get('poster_path', '')
        serie, _ = Series.objects.get_or_create(
            tmdb_id=tmdb_id,
            title=title,
            defaults={
                'overview': overview,
                'release_date': release_date,
                'poster_path': poster_path,
            }
        )
        serie.genres.add(Genre.objects.get(tmdb_id=genre_id))
    series = Series.objects.filter(genres__tmdb_id=genre_id).distinct()
    return render(request, 'genre_movies.html', {'series': series})


def get_series_by_category(category_id, page_number):
    url = f'https://api.themoviedb.org/3/discover/tv'
    params = {
        'api_key': API_KEY,
        'with_genres': category_id,
        'page': page_number
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    series = data.get('results', [])
    
    return series

def paginate_series(request, series):
    paginator = Paginator(series, 20)  # Show 20 movies per page
    page_number = request.GET.get('page')
    
    try:
        series = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        series = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        series = paginator.page(paginator.num_pages)
    
    return series

def fetch_latest_series(page=1):
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&sort_by=release_date.desc&release_date.lte={today}&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        series = response.json().get('results', [])
        # Filter out movies without posters
        series_with_posters = [series for series in series if series.get('poster_path')]
        return series_with_posters
    else:
        response.raise_for_status()

def fetch_action_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10759&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_soap_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10766&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_animation_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=16&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_scifi_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10765&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_kids_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10762&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_family_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10751&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_drama_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=18&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_comedy_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=35&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_politics_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10768&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()
        
def fetch_mystery_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=9648&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()

        
def fetch_reality_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=10764&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()

def fetch_crime_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=80&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()

def fetch_documentary_series(page=1):
    url = f'https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&language=en-US&with_genres=99&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        response.raise_for_status()




def action_series(request):
    category_id = 10759  # Action movies
    page_number = request.GET.get('page', 1)
    
    try:
        # Assuming get_movies_by_category retrieves movies based on category_id and page_number
        action_series = get_movies_by_category(category_id, page_number)
        
        # Assuming paginate_movies paginates the movies list
        action_series = paginate_movies(request, action_movies)
    
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    context = {
        'action_series': action_series,
        'category': 'Action',
    }
    
    return render(request, 'series21.html', context)

def animation_series(request):
    category_id = 16  # Animation movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Animation'})

def crime_series(request):
    category_id = 80  # Crime movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Crime'})

def comedy_series(request):
    category_id = 35  # Comedy movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_movies_by_category(category_id, page_number)
        series = paginate_movies(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Comedy'})

def drama_series(request):
    category_id = 18  # Drama movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Drama'})

def reality_series(request):
    category_id = 10764  # Reality movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Horror'})

def family_series(request):
    category_id = 10751  # Family movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Family'})

def kids_series(request):
    category_id = 10762 # kids movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Kids'})

def scifi_series(request):
    category_id = 10765  # Science Fiction movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Science Fiction'})

def mystery_series(request):
    category_id = 9648  # Mystery movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Mystery'})

def documentary_series(request):
    category_id = 99  # Documentary Fiction movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Documentary'})

def politics_series(request):
    category_id = 10768  #  series movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'War&Politics'})

def soap_series(request):
    category_id = 10766  # Soap movies
    page_number = request.GET.get('page', 1)
    
    try:
        series = get_series_by_category(category_id, page_number)
        series = paginate_series(request, series)
    except requests.exceptions.RequestException:
        return HttpResponseServerError('Error fetching data from TMDb.')
    
    return render(request, 'series21.html', {'series': series, 'category': 'Soaps'})

def home_series(request):
    url = f'https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=en-US&page=1'
    data = make_api_request(url)
    series = data['results']
    
    action_series = fetch_action_series()
    reality_series = fetch_reality_series()
    animation_series = fetch_animation_series()
    scifi_series = fetch_scifi_series()
    mystery_series = fetch_mystery_series()
    drama_series = fetch_drama_series()
    comedy_series = fetch_comedy_series()
    latest_series = fetch_latest_series()
    family_series = fetch_family_series()
    politics_series = fetch_politics_series()
    kids_series = fetch_kids_series()
    soap_series = fetch_soap_series()
    crime_series = fetch_crime_series()
    documentary_series = fetch_documentary_series()
    
    posters = [serie['poster_path'] for serie in series]
    posters = [serie['poster_path'] for serie in action_series]
    posters = [serie['poster_path'] for serie in kids_series]
    posters = [serie['poster_path'] for serie in animation_series]
    posters = [serie['poster_path'] for serie in scifi_series]
    posters = [serie['poster_path'] for serie in soap_series]
    posters = [serie['poster_path'] for serie in mystery_series]
    posters = [serie['poster_path'] for serie in drama_series]
    posters = [serie['poster_path'] for serie in comedy_series]
    posters = [serie['poster_path'] for serie in latest_series]
    posters = [serie['poster_path'] for serie in family_series]
    posters = [serie['poster_path'] for serie in reality_series]
    posters = [serie['poster_path'] for serie in politics_series]
    posters = [serie['poster_path'] for serie in crime_series]
    posters = [serie['poster_path'] for serie in documentary_series]
    
    context = {
        'series': series,
        'action_series': action_series,
        'politics_series': politics_series,
        'animation_series': animation_series,
        'scifi_series': scifi_series,
        'drama_series': drama_series,
        'comedy_series': comedy_series,
        'latest_series': latest_series,
        'family_series': family_series,
        'reality_series': reality_series,
        'soap_series': soap_series,
        'kids_series': kids_series,
        'mystery_series': mystery_series,
        'crime_series': crime_series,
        'documentary_series': documentary_series,
        'posters': posters,
    }
    
    return render(request, 'series.html', context)

def generate_serie_token(movie_id):
    return hashlib.sha256(f"{movie_id}".encode()).hexdigest()

import logging
logger = logging.getLogger(__name__)

def serie_details(request, pk):
    try:
        tmdb_api_key = API_KEY  # Ensure API_KEY is defined in settings.py
        tmdb_base_url = 'https://api.themoviedb.org/3'
        tvmaze_base_url = 'https://api.tvmaze.com'

        # Fetch series details from TMDB
        series_url = f'{tmdb_base_url}/tv/{pk}?api_key={tmdb_api_key}&language=en-US'
        series_response = requests.get(series_url)
        series_response.raise_for_status()
        serie_data = series_response.json()

        # Extract series details
        serie_name = serie_data.get('name')
        serie_overview = serie_data.get('overview', '')
        serie_poster_path = serie_data.get('poster_path', '')
        serie_first_air_date = serie_data.get('first_air_date', '')
        serie_vote_average = serie_data.get('vote_average', 0)
        serie_genres = [genre['name'] for genre in serie_data.get('genres', [])]
        serie_episode_run_time = serie_data.get('episode_run_time', [])
        serie_tagline = serie_data.get('tagline', '')
        serie_status = serie_data.get('status', '')
        full_poster_url = f'https://image.tmdb.org/t/p/w500{serie_poster_path}'
        
        # The `pk` is the TMDB ID in this case
        tmdb_id = pk

        # Fetch TVDB ID from TMDB
        external_ids_url = f'{tmdb_base_url}/tv/{pk}/external_ids?api_key={tmdb_api_key}'
        external_ids_response = requests.get(external_ids_url)
        external_ids_response.raise_for_status()
        external_ids_data = external_ids_response.json()
        tvdb_id = external_ids_data.get('tvdb_id')

        if not tvdb_id:
            raise ValueError('TVDB ID not found for the series in TMDB')

        # Fetch series details from TVMaze
        tvmaze_url = f'{tvmaze_base_url}/lookup/shows?thetvdb={tvdb_id}'
        tvmaze_response = requests.get(tvmaze_url)
        tvmaze_response.raise_for_status()
        tvmaze_data = tvmaze_response.json()
        serie_tvmaze_id = tvmaze_data['id']

        # Fetch seasons data from TVMaze
        seasons_url = f'{tvmaze_base_url}/shows/{serie_tvmaze_id}/seasons'
        seasons_response = requests.get(seasons_url)
        seasons_response.raise_for_status()
        seasons_data = seasons_response.json()

        # Fetch episodes for each season
        seasons_with_episodes = []
        for season in seasons_data:
            season_id = season['id']
            episodes_url = f'{tvmaze_base_url}/seasons/{season_id}/episodes'
            episodes_response = requests.get(episodes_url)
            episodes_response.raise_for_status()
            episodes_data = episodes_response.json()

            seasons_with_episodes.append({
                'season': season,
                'episodes': episodes_data
            })
            
              

        serie_token = generate_serie_token(pk)
        latest_series = fetch_latest_series()

        context = {
            'serie': {
                'tmdb_id': tmdb_id,
                'name': serie_name,
                'overview': serie_overview,
                'poster_path': full_poster_url,
                'first_air_date': serie_first_air_date,
                'vote_average': serie_vote_average,
                'tagline': serie_tagline,
                'status': serie_status,
                'genres': serie_genres,
                'episode_run_time': serie_episode_run_time,
            },
            'seasons': seasons_with_episodes,
            'serie_token': serie_token,
            'latest_series': latest_series,
        }
        return render(request, 'series_details.html', context)

    except requests.RequestException as e:
        logger.error(f"Error fetching series details: {str(e)}")
        return render(request, 'series_details.html', {'error_message': 'Your series wasn\'t found. Try again later.'})
    except ValueError as e:
        logger.error(f"Error processing series data: {str(e)}")
        return render(request, 'series_details.html', {'error_message': 'There was an issue processing the series data.'})
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return render(request, 'series_details.html', {'error_message': 'An unexpected error occurred. Try again later.'})
    