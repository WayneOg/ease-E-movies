# Generated by Django 5.0.6 on 2024-07-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0004_movie_tmdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(default='', max_length=255),
        ),
    ]
