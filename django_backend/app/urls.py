from django.urls import path
from .views import *

urlpatterns = [
    path('api/anime/', AnimeListView.as_view(), name='anime-list'),
    path('api/anime/search/', AnimeSearchView.as_view(), name='anime-search'),
]
