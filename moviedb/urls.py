from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('series/', views.home_series, name='series'),
    path('categories/', views.movie_list, name='categories'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genre/<int:genre_id>/', views.genre_movies, name='genre_movies'),
    path('seriesgenre/<int:genre_id>/', views.genre_series, name='genre_movies'),
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
]