from django.db import models

# individual models for many-to-many relationship
class Genre(models.Model):
    mal_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=[("genre", "Genre"), ("explicit", "Explicit Genre")])
    
    def __str__(self):
        return f"{self.name} ({self.type})" if self.name else "Unnamed Genre"
    
class Theme(models.Model):
    mal_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name or "Unnamed Theme"

class Studio(models.Model):
    mal_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name or "Unnamed Studio"

class Producer(models.Model):
    mal_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name or "Unnamed Producer"

# text choices go here for organization
class Type(models.TextChoices):
    TV = "TV"
    OVA = "OVA"
    MOVIE = "Movie"
    SPECIAL = "Special"
    TVSPECIAL = "TV Special"
    ONA = "ONA"
    MUSIC = "Music"
    PV = "PV"

class Status(models.TextChoices):
    FINISHED = "Finished Airing"
    CURRENTLY = "Currently Airing"
    NOT_YET = "Not yet aired"

class Rating(models.TextChoices):
    G = "G - All Ages"
    PG = "PG - Children"
    PG_13 = "PG-13 - Teens 13 or older"
    R = "R - 17+ (violence & profanity)"
    R_PLUS = "R+ - Mild Nudity"
    RX = "Rx - Hentai"

class Season(models.TextChoices):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"

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
    producers = models.ManyToManyField(Producer,blank=True, related_name="animes")
    studios = models.ManyToManyField(Studio, blank=True, related_name="animes")
    genres = models.ManyToManyField(Genre, blank=True, related_name="animes")  # related_name for reverse lookups
    themes = models.ManyToManyField(Theme, blank=True, related_name="animes")

    def __str__(self):
        return self.titles["Default"]
