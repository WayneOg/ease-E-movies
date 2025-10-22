from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Movie, Genre, Series, Season, Episode


# Customize admin site header and title
admin.site.site_header = "ease-E-movies Administration"
admin.site.site_title = "ease-E-movies Admin"
admin.site.index_title = "Welcome to ease-E-movies Admin Panel"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin interface for Genre model."""
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Enhanced admin interface for Movie model."""
    list_display = ('id', 'title', 'poster_thumbnail', 'release_date', 'vote_average', 'runtime', 'get_genres')
    list_filter = ('release_date', 'vote_average', 'genres')
    search_fields = ('title', 'overview', 'imdb_id', 'tmdb_id')
    readonly_fields = ('poster_preview',)
    filter_horizontal = ('genres',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'overview', 'tagline')
        }),
        ('Media', {
            'fields': ('poster_path', 'poster_preview')
        }),
        ('Details', {
            'fields': ('release_date', 'runtime', 'vote_average', 'genres')
        }),
        ('External IDs', {
            'fields': ('id', 'tmdb_id', 'imdb_id'),
            'classes': ('collapse',)
        }),
        ('Streaming URLs', {
            'fields': ('wootly_url', 'dood_url'),
            'classes': ('collapse',)
        }),
    )
    
    def poster_thumbnail(self, obj):
        """Display small poster thumbnail in list view."""
        if obj.poster_path:
            return format_html(
                '<img src="https://image.tmdb.org/t/p/w92{}" style="max-height: 50px; border-radius: 4px;" />',
                obj.poster_path
            )
        return "No poster"
    poster_thumbnail.short_description = 'Poster'
    
    def poster_preview(self, obj):
        """Display larger poster preview in detail view."""
        if obj.poster_path:
            return format_html(
                '<img src="https://image.tmdb.org/t/p/w342{}" style="max-width: 300px; border-radius: 8px;" />',
                obj.poster_path
            )
        return "No poster available"
    poster_preview.short_description = 'Poster Preview'
    
    def get_genres(self, obj):
        """Display genres as comma-separated list."""
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = 'Genres'


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """Enhanced admin interface for Series model."""
    list_display = ('id', 'title', 'poster_thumbnail', 'release_date', 'vote_average', 'status', 'number_of_seasons', 'number_of_episodes')
    list_filter = ('status', 'release_date', 'vote_average', 'genres')
    search_fields = ('title', 'overview', 'imdb_id', 'tmdb_id')
    readonly_fields = ('poster_preview',)
    filter_horizontal = ('genres',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'overview', 'tagline', 'status')
        }),
        ('Media', {
            'fields': ('poster_path', 'poster_preview')
        }),
        ('Details', {
            'fields': ('release_date', 'runtime', 'vote_average', 'genres', 'number_of_seasons', 'number_of_episodes')
        }),
        ('External IDs', {
            'fields': ('id', 'tmdb_id', 'imdb_id'),
            'classes': ('collapse',)
        }),
    )
    
    def poster_thumbnail(self, obj):
        """Display small poster thumbnail in list view."""
        if obj.poster_path:
            return format_html(
                '<img src="https://image.tmdb.org/t/p/w92{}" style="max-height: 50px; border-radius: 4px;" />',
                obj.poster_path
            )
        return "No poster"
    poster_thumbnail.short_description = 'Poster'
    
    def poster_preview(self, obj):
        """Display larger poster preview in detail view."""
        if obj.poster_path:
            return format_html(
                '<img src="https://image.tmdb.org/t/p/w342{}" style="max-width: 300px; border-radius: 8px;" />',
                obj.poster_path
            )
        return "No poster available"
    poster_preview.short_description = 'Poster Preview'


class EpisodeInline(admin.TabularInline):
    """Inline admin for episodes within a season."""
    model = Episode
    extra = 0
    fields = ('episode_number', 'name', 'air_date', 'vote_average')


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Admin interface for Season model."""
    list_display = ('id', 'series', 'season_number', 'name', 'episode_count', 'air_date')
    list_filter = ('series', 'air_date')
    search_fields = ('name', 'series__title')
    inlines = [EpisodeInline]
    
    fieldsets = (
        ('Season Information', {
            'fields': ('series', 'season_number', 'name', 'overview')
        }),
        ('Details', {
            'fields': ('air_date', 'episode_count')
        }),
    )


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    """Admin interface for Episode model."""
    list_display = ('id', 'get_series', 'get_season_number', 'episode_number', 'name', 'air_date', 'vote_average')
    list_filter = ('season__series', 'air_date', 'vote_average')
    search_fields = ('name', 'overview', 'season__series__title')
    
    fieldsets = (
        ('Episode Information', {
            'fields': ('season', 'episode_number', 'name', 'overview')
        }),
        ('Details', {
            'fields': ('air_date', 'vote_average')
        }),
    )
    
    def get_series(self, obj):
        """Get the series title for this episode."""
        return obj.season.series.title
    get_series.short_description = 'Series'
    get_series.admin_order_field = 'season__series__title'
    
    def get_season_number(self, obj):
        """Get the season number for this episode."""
        return obj.season.season_number
    get_season_number.short_description = 'Season'
    get_season_number.admin_order_field = 'season__season_number'