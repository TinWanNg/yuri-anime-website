from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from django.db.models import F

"""
state the allowed parameters for the endpoints here in views
"""
class AnimeListView(ListAPIView):
    serializer_class = AnimeSerializer

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre = self.request.query_params.get('genre')
        order_by = self.request.query_params.get('sort')

        if genre:
            queryset = queryset.filter(genres__name__iexact=genre)

        sort_vals = ['title','score', 'popularity', 'year']  # only allow specific whitelisted values
        if order_by in sort_vals + ['-' + val for val in sort_vals]:
            if "title" in order_by:
                queryset = queryset.extra(select={'title_default': "json_extract(titles, '$.Default')"}).order_by('title_default')
                if order_by.startswith("-"):
                    queryset = queryset.reverse()
            else:
                queryset = queryset.order_by(order_by)

        return queryset
