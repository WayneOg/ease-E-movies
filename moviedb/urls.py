from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('series/', views.home_series, name='series'),
    path('categories/', views.movie_list, name='categories'),
    path('genres/', views.genre_list, name='genre_list'),
    path('series_genres/', views.series_genre_list, name='series_genre_list'),
    path('genre/<int:genre_id>/', views.genre_movies, name='genre_movies'),
    path('seriesgenre/<int:genre_id>/', views.genre_series, name='genre_series'),
    path('search/', views.search_results, name='search_results'),
    path('movielist', views.movie_list, name='movie_list'),
    path('movie_details/<int:pk>/', views.movie_details, name='movie_details'),
    path('categories/<slug:category_slug>/', views.category_movies, name='category_movies'),
    path('action/', views.action_movies, name='action_movies'),
    path('animation/', views.animation_movies, name='animation_movies'),
    path('comedy/', views.comedy_movies, name='comedy_movies'),
    path('drama/', views.drama_movies, name='drama_movies'),
    path('horror/', views.horror_movies, name='horror_movies'),
    path('investigative/', views.investigative_movies, name='investigative_movies'),
    path('romance/', views.romance_movies, name='romance_movies'),
    path('sci-fi/', views.scifi_movies, name='scifi_movies'),
    path('serieslist/', views.series_list, name='series_movies'),
    path('series/<int:pk>/', views.serie_details, name='series_details'),
    path('series/<int:pk>/season/<int:season>/', views.serie_details, name='series_details_season'),
    path('action_series/', views.action_series, name='action_series'),
    path('animation_series/', views.animation_series, name='nimation_series'),
    path('comedy_series/', views.comedy_series, name='comedy_series'),
    path('drama_series/', views.drama_series, name='drama_series'),
    path('soap_series/', views.soap_series, name='soap_series'),
    path('kids_series/', views.kids_series, name='kids_series'),
    path('family_series/', views.family_series, name='family_series'),
    path('history_series/', views.politics_series, name='history_series'),
    path('documentary_series/', views.documentary_series, name='documentary_series'),
    path('crime_series/', views.crime_series, name='crime_series'),
    path('reality_series/', views.reality_series, name='reality_series'),
    path('sci-fi_series/', views.scifi_series, name='sci-fi_series'),
    path('serielist', views.serie_list, name='serie_list'),
    path('anime/popular/', views.popular_anime, name='popular_anime'),
    path('anime/genre/<int:genre_id>/', views.anime_by_genre, name='anime_by_genre'),
    path('anime/action/', views.action_anime, name='action_anime'),
    path('anime/scifi/', views.scifi_anime, name='scifi_anime'),
    path('anime/romance/', views.romance_anime, name='romance_anime'),
    path('anime/drama/', views.drama_anime, name='drama_anime'),
    path('anime/comedy/', views.comedy_anime, name='comedy_anime'),
    path('anime/history/', views.history_anime, name='history_anime'),
    path('anime/horror/', views.horror_anime, name='horror_anime'),
    path('anime/investigative/', views.investigative_anime, name='investigative_anime'),
]