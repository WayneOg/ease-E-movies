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

def search_results(request):
    query = request.GET.get('query', '').strip()
    if not query:
        return render(request, 'search_results.html', {'movies': [], 'series': []})  # Render empty page if no query

    # Check if movie and series already exist in the database
    movies = list(Movie.objects.filter(title__icontains=query))
    series = list(Series.objects.filter(title__icontains=query))

    # Fetch data from TMDb API for movies if not found in the database
    if not movies:
        tmdb_api_key = API_KEY
        movie_url = 'https://api.themoviedb.org/3/search/movie'
        movie_params = {
            'api_key': tmdb_api_key,
            'language': 'en-US',
            'query': query
        }

        try:
            movie_response = requests.get(movie_url, params=movie_params)
            movie_response.raise_for_status()  # Raise an exception for bad status codes
            movie_results = movie_response.json().get('results', [])

            for result in movie_results:
                if result.get('poster_path'):  # Only process movies with posters
                    movie, created = Movie.objects.update_or_create(
                        id=result['id'],
                        defaults={
                            'title': result['title'],
                            'overview': result.get('overview', ''),
                            'release_date': result.get('release_date', None),
                            'poster_path': result.get('poster_path', ''),
                        }
                    )
                    movies.append(movie)

        except requests.RequestException:
            return HttpResponseServerError("Error fetching movie data from API")

    # Fetch data from TVmaze API for series if not found in the database
    if not series:
        series_url = 'http://api.tvmaze.com/search/shows'
        series_params = {'q': query}

        try:
            series_response = requests.get(series_url, params=series_params)
            series_response.raise_for_status()  # Raise an exception for bad status codes
            series_results = series_response.json()

            for result in series_results:
                show = result['show']
                if show.get('image') and show['image'].get('medium'):  # Only process series with posters
                    serie, created = Series.objects.update_or_create(
                        tmdb_id=show['id'],
                        defaults={
                            'title': show['name'],
                            'summary': show.get('summary', ''),
                            'release_date': show.get('premiered', None),
                            'poster': show.get('image', {}).get('medium', ''),
                        }
                    )
                    series.append(serie)

        except requests.RequestException:
            return HttpResponseServerError("Error fetching series data from API")

    # Filter out movies and series without posters
    movies = [movie for movie in movies if movie.poster_path]
    series = [serie for serie in series if serie.poster]

    return render(request, 'search_results.html', {'movies': movies, 'series': series})



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
    
        url = 'https://api.tvmaze.com/shows'  # Endpoint for TVmaze API shows
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        series = response.json()
        context = {'series': series}
        return render(request, 'series_list.html', context)

    
def series_details(request, pk, season=1):
    # Fetch series details from the TVmaze API
    series_url = f'http://api.tvmaze.com/shows/{pk}'
    series_response = requests.get(series_url)
    series_response.raise_for_status()
    series_data = series_response.json()
    
    # Fetch seasons details
    seasons_url = f'http://api.tvmaze.com/shows/{pk}/seasons'
    seasons_response = requests.get(seasons_url)
    seasons_response.raise_for_status()
    seasons_data = seasons_response.json()
    
    # Fetch episodes details for the selected season
    episodes_url = f'http://api.tvmaze.com/seasons/{season}/episodes'
    episodes_response = requests.get(episodes_url)
    episodes_response.raise_for_status()
    episodes_data = episodes_response.json()

    # Example fields to retrieve from the API response
    series_name = series_data.get('name')
    series_summary = series_data.get('summary', '')
    series_image = series_data.get('image', {}).get('medium', '')

    # Assuming you have a Series model to save or retrieve details
    series, created = Series.objects.get_or_create(
        tmdb_id=pk,
        defaults={
            'title': series_name,
            'summary': series_summary,
            'poster': series_image,
            # Add other fields as needed
        }
    )

    context = {
        'series': series,
        'seasons': seasons_data,
        'season': season,
        'episodes': episodes_data
    }
    return render(request, 'series_details.html', context)

def fetch_episodes(request, pk, season, series_id, season_number):
    episodes_url = f'http://api.tvmaze.com/seasons/{season}/episodes'
    episodes_response = requests.get(episodes_url)
    episodes_response.raise_for_status()
    episodes_data = episodes_response.json()
    
    series = get_object_or_404(Series, id=series_id)
    season = get_object_or_404(Season, series=series, number=season_number)
    episodes = Episode.objects.filter(season=season).order_by('number')
    
    episodes_data = [
        {
            'id': episode.id,
            'number': episode.number,
            'name': episode.name,
        }
        for episode in episodes
    ]
    
    return JsonResponse({'episodes': episodes_data})

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

