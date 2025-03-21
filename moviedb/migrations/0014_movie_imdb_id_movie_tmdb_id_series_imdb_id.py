# Generated by Django 5.0.6 on 2024-07-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0013_movie_dood_url_movie_wootly_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
