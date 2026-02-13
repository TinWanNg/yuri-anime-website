from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import *
from .serializers import *
from django.db.models import F

"""
state the allowed parameters for the endpoints here in views
"""
class AnimeListView(ListAPIView):
    serializer_class = AnimeSerializer

    @swagger_auto_schema(
        operation_description="Get a list of all yuri anime with optional filtering and sorting",
        manual_parameters=[
            openapi.Parameter('genre', openapi.IN_QUERY, description="Filter by genre ID", type=openapi.TYPE_INTEGER),
            openapi.Parameter('type', openapi.IN_QUERY, description="Filter by type (TV, OVA, Movie, Special, TV Special, ONA, Music, PV)", type=openapi.TYPE_STRING),
            openapi.Parameter('status', openapi.IN_QUERY, description="Filter by status (Finished Airing, Currently Airing, Not yet aired)", type=openapi.TYPE_STRING),
            openapi.Parameter('rating', openapi.IN_QUERY, description="Filter by rating (G - All Ages, PG - Children, PG-13 - Teens 13 or older, R - 17+, R+ - Mild Nudity, Rx - Hentai)", type=openapi.TYPE_STRING),
            openapi.Parameter('sort', openapi.IN_QUERY, description="Sort by field (title, score, popularity, year). Prefix with '-' for descending order", type=openapi.TYPE_STRING),
        ],
        responses={200: AnimeSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # only allow specific whitelisted values for filter and sort
    def get_queryset(self):
        queryset = Anime.objects.all()

        # Filter
        genre = self.request.query_params.get('genre')
        type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')
        rating = self.request.query_params.get('rating')

        if genre:
            queryset = queryset.filter(genres__id=genre)

        # handle text chocies fields
        if type and Type(type):
            queryset = queryset.filter(type__iexact=type)
        if status and Status(status):
            queryset = queryset.filter(status__iexact=status)
        if rating and Rating(rating):
            queryset = queryset.filter(rating__iexact=rating)

        # Sort
        order_by = self.request.query_params.get('sort')

        sort_vals = ['title','score', 'popularity', 'year']  
        if order_by in sort_vals + ['-' + val for val in sort_vals]:  # allows both asc and desc
            if "title" in order_by:
                queryset = queryset.extra(select={'title_default': "json_extract(titles, '$.Default')"}).order_by('title_default')
                if order_by.startswith("-"):
                    queryset = queryset.reverse()
            else:
                queryset = queryset.order_by(order_by)

        return queryset


class AnimeSearchView(ListAPIView):
    serializer_class = AnimeSerializer

    @swagger_auto_schema(
        operation_description="Search anime by title or synopsis",
        manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, description="Search query string", type=openapi.TYPE_STRING, required=True),
        ],
        responses={200: AnimeSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        # Get search query
        query = self.request.query_params.get('q', '')

        if not query:
            return Anime.objects.none()        

        # Search in titles JSON field (Default key) and synopsis
        queryset = Anime.objects.all()
        queryset = queryset.extra(
            where=["json_extract(titles, '$.Default') LIKE %s OR synopsis LIKE %s"],
            params=[f'%{query}%', f'%{query}%']
        )
        
        return queryset
