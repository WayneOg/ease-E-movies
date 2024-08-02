from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    vote_average = models.FloatField(default=0)
    genres = models.ManyToManyField(Genre, blank=True)
    runtime = models.IntegerField(default=0)  # Set default runtime to 0
    tagline = models.CharField(max_length=255, blank=True, null=True)
    wootly_url = models.URLField(blank=True, null=True)
    dood_url = models.URLField(blank=True, null=True)
    imdb_id = models.CharField(max_length=10, blank=True, null=True)
    tmdb_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Series(models.Model):
    title = models.CharField(max_length=200)
    poster = models.URLField(blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    tmdb_id = models.IntegerField(unique=True, null=True)
    summary = models.TextField(max_length=255, null=True)
    imdb_id = models.CharField(max_length=10, blank=True, null=True)
    # Add more fields as needed
    
    def __str__(self):
        return self.title
    
class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='seasons')
    number = models.IntegerField()

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    number = models.IntegerField()
    name = models.CharField(max_length=255)
