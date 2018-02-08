from django.db import models

from artist.models import Artist


class Album(models.Model):
    title = models.CharField('앨범명', max_length=50)
    released_date = models.DateField('발매일', blank=True, null=True)
    genre = models.CharField('장르', max_length=30, blank=True)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.title
