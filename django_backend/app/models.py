from django.db import models

# individual models for many-to-many relationship
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=[("genre", "Genre"), ("explicit", "Explicit Genre")])

class Studio(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Producer(models.Model):
    name = models.CharField(max_length=200, unique=True)

# text choices go here for organization
class Type(models.TextChoices):
    TV = "tv", "TV"
    OVA = "ova", "OVA"
    MOVIE = "movie", "Movie"
    SPECIAL = "special", "Special"
    ONA = "ona", "ONA"
    MUSIC = "music", "Music"

class Status(models.TextChoices):
    FINISHED = "finished_airing", "Finished Airing"
    CURRENTLY = "currently_airing", "Currently Airing"
    NOT_YET = "not_yet_aired", "Not Yet Aired"

class Rating(models.TextChoices):
    G = "g", "G - All Ages"
    PG = "pg", "PG - Children"
    PG_13 = "pg_13", "PG-13 - Teens 13 or older"
    R = "r", "R - 17+ (violence & profanity)"
    R_PLUS = "r+", "R+ - Mild Nudity"
    RX = "rx", "Rx - Hentai"

class Season(models.TextChoices):
    WINTER = "winter", "Winter"
    SPRING = "spring", "Spring"
    SUMMER = "summer", "Summer"
    FALL = "fall", "Fall"

class Anime(models.Model):
    mal_id = models.IntegerField(null=False)
    image = models.ImageField(null=True, upload_to='images/anime/')
    trailer = models.URLField(null=True)
    titles = models.JSONField(null=False)
    type = models.CharField(null=True, max_length=10, choices=Type.choices)
    source = models.CharField(null=True, max_length=100)
    episodes = models.IntegerField(null=True)
    status = models.CharField(null=True, max_length=50, choices=Status.choices)
    aired = models.JSONField(null=True)
    duration = models.CharField(null=True, max_length=50)
    rating = models.CharField(null=True, max_length=50, choices=Rating.choices)
    score = models.FloatField(null=True)
    scored_by = models.IntegerField(null=True)
    popularity = models.IntegerField(null=True)
    synopsis = models.CharField(null=True, max_length=10000)
    season = models.CharField(null=True, max_length=50, choices=Season.choices)
    year = models.IntegerField(null=True)
    producers = models.ManyToManyField(Producer,null=True)
    studios = models.ManyToManyField(Studio, null=True)
    genres = models.ManyToManyField(Genre, null=True, related_name="animes")  # related_name for reverse lookups
    themes = models.JSONField(null=True)

    def __str__(self):
        pass
