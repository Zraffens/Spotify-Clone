from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    artistSongs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = '__all__'

    def get_artistSongs(self, instance):
        songs_list = []
        for i in instance.song_set.all():
            songs_list.append(i.id)
        return songs_list
