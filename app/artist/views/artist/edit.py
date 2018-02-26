from django.shortcuts import render, get_object_or_404, redirect

from artist.forms import ArtistForm
from artist.models import Artist

__all__ = (
    'artist_edit',
)


def artist_edit(request, artist_pk):
    """
    artist_pk에 해당하는 Artist를 수정

    Form: ArtistForm
    Template : artist/artist-edit.html

    bound form: ArtistForm(instance=<artist instance>)
    ModelForm를 사용해 instance 업데이트
        form = ArtistForm(request.POST, request.FILES, instance=<artist instance>)
        form.save()

    :param request:
    :param artist_pk:
    :return:
    """
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist:artist-list')
    else:
        form = ArtistForm(instance=artist)
    context = {
        'artist_form': form
    }
    return render(request, 'artist/artist_edit.html', context)
