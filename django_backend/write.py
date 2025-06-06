#!/usr/bin/env python

"""
Write to db from jikan api regularly
- using this endpoint: https://docs.api.jikan.moe/#tag/anime/operation/getAnimeSearch
"""

import requests
import time
import os
import django
from django.core.wsgi import get_wsgi_application

# Ensure settings are read and configures Django’s environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_backend.settings")  # so Django knows where to find settings.py
django.setup()
application = get_wsgi_application()

from app.models import *


source = "https://api.jikan.moe/v4/"

def format_to_dict(item, key, subkey, subvalue):
    li = item[key]
    dic = {x[subkey]:x[subvalue] for x in li}
    return dic


def write_anime(genre_id=26, page=1):
    while True:
        # 1. get data at current page
        response = requests.get(f"{source}anime", params={"genres": genre_id, "page": page})
        response.raise_for_status()
        j = response.json()
        data = j["data"]
        
        for anime in data:
            # 2. check if anime exists by id, continue if so
            if Anime.objects.filter(mal_id=anime["mal_id"]).exists():
                continue
            
            # 3. save to db
            # 3.1. anime model
            anime_ = Anime(
                mal_id=anime["mal_id"],
                image=anime["images"]["jpg"]["large_image_url"],
                trailer=anime["trailer"]["url"],
                titles=format_to_dict(anime, "titles", "type", "title"),
                type=anime["type"],
                source=anime["source"],
                episodes=anime["episodes"],
                status=anime["status"],
                aired=anime["aired"],
                duration=anime["duration"],
                rating=anime["rating"],
                score = anime["score"],
                scored_by = anime["scored_by"],
                popularity = anime["popularity"],
                synopsis=anime["synopsis"],
                season=anime["season"],
                year=anime["year"],
                themes=format_to_dict(anime, "themes", "name", "url"),
            )
            anime_.save()

            # 3.2. add enum models
            for genre in anime["genres"]:
                genre_obj, _ = Genre.objects.get_or_create(name=genre["name"], type="genre")
                anime_.genres.add(genre_obj)
            for e_genre in anime["explicit_genres"]:
                e_genre_obj, _ = Genre.objects.get_or_create(name=e_genre["name"], type="explicit")
                anime_.genres.add(e_genre_obj)
            for studio in anime["studios"]:
                studio_obj, _ = Studio.objects.get_or_create(name=studio["name"])
                anime_.studios.add(studio_obj)
            for producer in anime["producers"]:
                producer_obj, _ = Producer.objects.get_or_create(name=producer["name"])
                anime_.producers.add(producer_obj)
            anime_.save()

            print(f"added {anime_.titles["Default"]} to db")

        # 4. go to next page if there's more data, else break
        if not j["pagination"]["has_next_page"]:  # Check if there's no data returned
            print(f"all data scraped")
            break

        page += 1
        time.sleep(1)
    
    return "All data scraped"


Anime.objects.all().delete()
print(f"{len(Anime.objects.all())} animes already in db. Adding more...")
write_anime()
print(f"Write done, now {len(Anime.objects.all())} animes in db")

