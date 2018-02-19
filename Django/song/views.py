from django.shortcuts import render

from song.models import Song


def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'song/song_list.html', context)


def song_search(request):
    """
    사용할 URL : song/search/
    사용할 Template: templates/song/song_search.html
        form안에
            input한개, button한개 배치
    :param request:
    :return:
    """
    return render(request, 'song/song_search.html')
