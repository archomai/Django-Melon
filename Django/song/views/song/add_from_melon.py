from datetime import datetime
from io import BytesIO

import requests
from django.core.files import File
from django.shortcuts import redirect

from artist.models import Artist
from crawler.artist import ArtistData
from crawler.song import SongData
from song.models import Song

__all__ = (
    'song_add_from_melon',
)


def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song_data = SongData(song_id)
        song_data.get_detail()

        artist, _ = Artist.objects.update_or_create_from_melon(song_data.artist_id)
        # Song.objects.upadate_or_create_from_melon() 매서드를 SongManager에 만들고
        #   해당 메서드가 Song detail정보들을 저장하면서 Artist.objects.update_or_create_melon_()도 호출해서
        #   자신의 artists 필드를 자동으로 채우게 구현
        song, _ = Song.objects.update_or_create(
            melon_id=song_id,
            defaults={
                'title': song_data.title,
                'genre': song_data.genre,
                'lyrics': song_data.lyrics,
            }
        )
        song.artists.add(artist)
        return redirect('song:song-list')
