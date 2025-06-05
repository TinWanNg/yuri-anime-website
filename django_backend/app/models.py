from django.db import models

# individual models for many-to-many relationship

class YuriAnime(models.Model):
    mal_id = models.IntegerField(null=False)
    image = models.ImageField(null=True, upload_to='images/anime/')
    trailer = models.URLField(null=True)
    titles = models.JSONField(null=False)
    type = models.CharField(max_length=10,
                            choices=[("tv", "TV"), 
                                     ("ova", "OVA"), 
                                     ("movie", "Movie"), 
                                     ("special", "Special"), 
                                     ("ova", "ONA"), 
                                     ("music", "Music")])
    source = models.CharField(null=True, max_length=100)
    episodes = models.IntegerField(null=True)
    status = models.CharField(max_length=50,
                              choices=[("finished_airing", "Finished Airing"), 
                                     ("currently_airing", "Currently Airing"), 
                                     ("not_yet_aired", "Not yet aired")])
    aired = models.JSONField(null=True)
    duration = models.CharField(null=True, max_length=50)
    rating = models.CharField(max_length=50,
                              choices=[("g", "G - All Ages"),
                                       ("pg", "PG - Children"),
                                       ("pg_13",  "PG-13 - Teens 13 or older"), 
                                       ("r", "R - 17+ (violence & profanity)"),
                                       ("r+", "R+ - Mild Nudity"),
                                       ("rx", "Rx - Hentai")])
    score = models.FloatField(null=True)
    scored_by = models.IntegerField(null=True)
    popularity = models.IntegerField(null=True)
    synopsis = models.CharField(null=True, max_length=10000)
    season = models.CharField(null=True, max_length=50,
                              choices=[("winter", "Winter"),
                                       ("spring", "Spring"),
                                       ("summer", "Summer"),
                                       ("fall", "Fall")])
    year = models.IntegerField(null=True)
    producers = models.JSONField(null=True)
    studios = models.JSONField(null=True)
    genres = models.JSONField(null=True)
    explicit_genres = models.JSONField(null=True)
    themes = models.JSONField(null=True)

    def __str__(self):
        pass
