from django.db import models

from album.models import Album
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, related_name='song')  # through='ArtistSong')

    def __str__(self):
        return f'{self.title}'

# class ArtistSong(models.Model):
#     artist = models.ForeignK.ey(Artist, on_delete=models.CASCADE)
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)
#     demo_date = models.DateTimeField()
