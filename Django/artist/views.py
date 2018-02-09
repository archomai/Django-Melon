from django.http import HttpResponse
from django.shortcuts import render

from artist.models import Artist


def artist_list(request):
    # 전체 Artist목록을 ul > li 로 출력
    # 템플릿은 'artist/artist_list.html'을 사용
    # 전달할 context키는 'artists'를 사용
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(request, 'artist/artist_list.html', context)


def artist_add(request):
    # HTML에 Artist클래스가 받을 수 있는 모든 input 을 구현
    #   img_profile은 제외
    # method가 POST면 request.POST에서 해당 데이터 처리
    #   새 Artist객체를 만들고 artist_list로 이동
    # method가 GET이면 artist_add.html을 표

    # ** 생년월일은 YYYY-MM-DD 형식으로 받음
    #   이후 datetiem,.strptime을 사용해서 date 객체로 변환

    # 1. artist_add.html 작성
    # 2. url과 연결, ./artist/add/ 에 매핑
    # 3. Get 요청시 잘 되는지 확인
    # 4. form method설정 후 POST요청시 artist_add() view에서 분기
    # 5. POST요청의 값이 request.POST 에 잘 오는지 확인
    # 6. request.POST에 담긴 값을 사용해 Artist인스턴스 생성
    # 7. 생성 완료 후 'artist:artist-list' URL name에 해당하는 view로 이동

    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        real_name = request.POST['real_name']
        nationality = request.POST['nationality']
        birth_date = request.POST['birth_date']
        constellation = request.POST['constellation']
        blood_type = request.POST['blood_type']
        intro = request.POST['intro']

        artist = Artist.objects.create(
            name=name,
            real_name=real_name,
            nationality=nationality,
            birth_date=birth_date,
            constellation=constellation,
            blood_type=blood_type,
            intro=intro
        )

        return HttpResponse('artist')
    else:
        return render(request, 'artist/artist_add.html', context)
