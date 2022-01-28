from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    artistn = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'

    def get_logo(self, instance):
        return 'http://localhost:8000/media/' + str(instance.album.logo)
    
    def get_artistn(self, instance):
        return str(instance.artist.title)
