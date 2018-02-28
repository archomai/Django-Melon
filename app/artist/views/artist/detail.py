import requests
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from ...models import Artist

__all_ = (
    'artist_detail',
)


def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)

    # youtube에서 아티스트명으로 검색한 결과 가져오기
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': settings.YOUTUBE_API_KEY,
        'part': 'snippet',
        'type': 'video',
        'maxResults': '10',
        'q': artist.name,
    }
    response = requests.get(url, params)
    response_dict = response.json()


    context = {
        'artist': artist,
        # youtube 검색 후 전달받은 데이터의 'item' 값
        'youtube_items': response_dict['items'],
    }
    return render(request, 'artist/artist_detail.html', context)


