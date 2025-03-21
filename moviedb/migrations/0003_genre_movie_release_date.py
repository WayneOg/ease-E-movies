# Generated by Django 5.0.6 on 2024-06-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0002_category_movie_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]
