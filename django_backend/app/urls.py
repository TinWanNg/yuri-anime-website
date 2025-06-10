from django.urls import path
from .views import AnimeListView

urlpatterns = [
    path('api/anime/', AnimeListView.as_view(), name='anime-list'),
]
