from django.db.models import Q
from django.http import HttpResponse
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

    - GET POST 분기
    1. input의 name을 keyword로 지정
    2. 이 함수를 request.method가 'GET'일 때와 'POST'일 때로 분기
    3. request.method가 'POST'일 때
        request.POST dict의 'name'키에 해당하는 값을
        HttpRespose로 출력
    4. request.method가 'GET'일 때
        이전에 하던 템플릿 출력을 유지

    - Query filter로 검색하기
    1. keyword가 자신의 'title'에 포함되는 Song 쿼리셋 생성
    2. 위 쿼리셋을 'songs'변수에 할당
    3. context dict를 만들고 'songs'키에 songs변수를 할당
    4. render의 3번째 인수로 context를 전달
    5. template에 전달된 'songs'를 출력
    :param request:
    :return:
    """
    context = {}
    # Song과 연결된 Artist의 name에 keyword가 포함되는 경우
    # Song과 연결된 Album의 title에 keyword가 포함되는 경우
    # Song의 title에 keyword가 포함되는 경
    #   를 모두 포함(or -> Q object)하는 쿼리셋을 'songs'에 할당

    if request.method == 'POST':
        # POST 요청에 전달된 데이터(input요소의 값들)중, name이 'keyword'인 input의 값
        keyword = request.POST['keyword'].strip()
        # keyword에 빈 값이 올 경우 결과 QuerySet을 할당하지 않도록 수정
        if keyword:
            # Song목록 중 title이 keyword를 포함하는 퀘리셋
            songs = Song.objects.filter(
                Q(album__title__contains=keyword) |
                Q(album__artists__name__contains=keyword) |
                Q(title__contains=keyword)
            ).distinct()
            context['songs'] = songs

            # songs_from_artists
            # songs_from_albums
            # songs_from_title
            # 위 세변수에 더 위의 조건 3개에 부합하는 쿼리셋을 각각전달
            # 세 변수를 이용해 검색 결과를 3단으로 분리해서 출력
            # -> 아티스트로 검색한 노래 결과, 앨범으로 검색한 노래 결과, 제목으로 검색한 노래 결과

            songs_from_artists = Song.objects.filter(
                album__artists__name__contains=keyword
            )
            context['songs_from_artists'] = songs_from_artists

            songs_from_album = Song.objects.filter(
                album__title__contains=keyword
            )
            context['songs_from_albums'] = songs_from_album

            songs_from_title = Song.objects.filter(
                title__contains=keyword
            )
            context['songs_from_title'] = songs_from_title

    # 만약 method가 POST였다면 context에 'songs'가 채워진 상태,
    # GET이면 빙 상태로 render실행
    return render(request, 'song/song_search.html', context)
