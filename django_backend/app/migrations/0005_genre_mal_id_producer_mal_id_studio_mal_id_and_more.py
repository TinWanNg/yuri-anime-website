# Generated by Django 5.1.2 on 2025-06-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_anime_genres_alter_anime_producers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='mal_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='mal_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studio',
            name='mal_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='mal_id',
            field=models.IntegerField(null=True),
        ),
    ]
