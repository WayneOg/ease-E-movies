# Generated by Django 5.0.6 on 2024-07-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0012_series_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dood_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='wootly_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
