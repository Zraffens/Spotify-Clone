from rest_framework import serializers
from .models import Album
from .models2 import Playlist


class AlbumSerializer(serializers.ModelSerializer):
    artistn = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    def get_artistn(self, instance):
        list1 = []

        for i in instance.artists.all():
            list1.append(str(i.title))
        
        return list1


class PlaylistSerializer(serializers.ModelSerializer):
    artistn = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def get_artistn(self, instance):
        list1 = []

        for i in instance.artists.all():
            list1.append(str(i.title))
        return list1