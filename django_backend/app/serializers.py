from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

"""
serialization = converting complex data e.g. db objs to a format like JSON
deserialization = converting JSON data back into objects
-> ensures different applications interact with the API in a standard way
"""
