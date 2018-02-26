from django.shortcuts import render, get_object_or_404

from ...models import Artist

__all_ = (
    'artist_detail',
)


def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    context = {
        'artist': artist
    }
    return render(request, 'artist/artist_detail.html', context)