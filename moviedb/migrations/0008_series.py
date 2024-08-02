# Generated by Django 5.0.6 on 2024-07-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0007_remove_genre_tmdb_id_remove_movie_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.URLField(blank=True, null=True)),
                ('imdb_id', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
