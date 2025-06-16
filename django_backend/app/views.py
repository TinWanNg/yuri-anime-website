from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from django.db.models import F

"""
state the allowed parameters for the endpoints here in views
"""
class AnimeListView(ListAPIView):
    serializer_class = AnimeSerializer

    # only allow specific whitelisted values for filter and sort
    def get_queryset(self):
        queryset = Anime.objects.all()

        # Filter
        genre = self.request.query_params.get('genre')
        type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')

        if genre:
            queryset = queryset.filter(genres__id=genre)

        # handle text chocies fields
        if type and Type(type):
            queryset = queryset.filter(type__iexact=type)
        if status and Status(status):
            queryset = queryset.filter(status__iexact=status)

        # Sort
        order_by = self.request.query_params.get('sort')

        sort_vals = ['title','score', 'popularity', 'year']  
        if order_by in sort_vals + ['-' + val for val in sort_vals]:
            if "title" in order_by:
                queryset = queryset.extra(select={'title_default': "json_extract(titles, '$.Default')"}).order_by('title_default')
                if order_by.startswith("-"):
                    queryset = queryset.reverse()
            else:
                queryset = queryset.order_by(order_by)

        return queryset
