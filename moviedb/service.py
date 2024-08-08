import requests
from .models import Movie, Series

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
                        id=result['id'],
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
            raise

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
                        id=result['id'],  # assuming TMDB ID is used as the primary key
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
            raise