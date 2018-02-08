from django.db import models

from artist.models import Artist


class Album(models.Model):
    title = models.CharField('앨범명', max_length=50)
    img_cover = models.ImageField('커버이미지', upload_to='album', blank=True)
    artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록')
    released_date = models.DateField('발매일', blank=True, null=True)

    @property
    def genre(self):
        # 장르는 가지고 있는 노래들에서 가져오기
        return ''

    def __str__(self):
        # 호호호빵 [휘성 (Realslow), 김태우]
        # 이렇게 나오도록
        return '{title} [{artist}]'.format(
            title= self.title,
            artist=', '.join(self.artists.values_list('name', flat=True)),
        )
