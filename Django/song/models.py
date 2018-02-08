from django.db import models

from album.models import Album
from artist.models import Artist


class Song(models.Model):
    album = models.ForeignKey(Album, verbose_name='앨범', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('곡 제목', max_length=255)
    genre = models.CharField('장르', max_length=100, blank=True)
    lylics = models.TextField('가사', blank=True)

    @property
    def artists(self):
        return self.album.artists.all()

    @property
    def released_date(self):
        return self.album.released_date

    @property
    def formatted_released_date(self):
        # 2017.01.17
        # self.release_date를 위와 같이 출력
        return self.released_date.strftime('%Y.%m.%d')

    def __str__(self):
        # 가수명 - 곡제목 (앨범명)
        return '{artists} - {song} ({album})'.format(
            artists=', '.join(self.album.artists.values_list('name', flat=True)),
            song=self.title,
            album=self.album.title,
        )
