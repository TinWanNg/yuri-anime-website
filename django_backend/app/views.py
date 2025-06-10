from rest_framework.generics import ListAPIView
from .models import Anime
from .serializers import AnimeSerializer
from django.db.models import Q

class AnimeListView(ListAPIView):
    serializer_class = AnimeSerializer

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre = self.request.query_params.get('genre')
        order_by = self.request.query_params.get('sort')

        if genre:
            queryset = queryset.filter(genres__name__iexact=genre)

        if order_by in ['title', '-title', 'score', '-score']:
            queryset = queryset.order_by(order_by)

        return queryset
