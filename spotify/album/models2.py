from django.db import models
from artist.models import Artist


class Playlist(models.Model):
    from song.models import Song

    title = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, upload_to='images/')
    artists = models.ManyToManyField(Artist)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
