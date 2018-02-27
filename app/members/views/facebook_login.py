import requests
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import redirect

__all__ = (
    'facebook_login',
)

User = get_user_model()


def facebook_login(request):
    # Code로부터 AccessToken 가져오기
    client_id = settings.FACEBOOK_APP_ID
    client_secret = settings.FACEBOOK_SECRET_CODE
    # 페이스북로그인 버튼을 누른 후 , 사용자가 승인하면 redirect_uri에 GET parameter로 'code'가 전송됨
    # 이 값과 client_id, secret을 사용해서 Facebook 서버에서 access_token을 받아와야 함
    code = request.GET['code']
    # 이전에 페이스북 로그인 버튼을 눌렀을 때 'code'를 다시 전달 받은 redirect_uri값을 그대로 사용
    redirect_uri = 'http://localhost:8000/facebook-login/'

    # 아래 엔드포인트에 GET 요청을 보냄
    url = 'https://graph.facebook.com/v2.12/oauth/access_token?'
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'client_secret': client_secret,
        'code': code,
    }

    response = requests.get(url, params)
    # 전송받은 결과는 JSON형식의 텍스트, requests가 제공하는 JSON 디코더를 사용해서
    # JSON텍스트를 python dict로 변환해 준다
    response_dict = response.json()
    # 값 출력해 보기
    for key, value in response_dict.items():
        print(f'{key}: {value}')

    # GraphAPI의 me 엔드포인트에 Get 요청 보내기
    url = 'https://graph.facebook.com/v2.12/me'
    params = {
        'access_token': response_dict['access_token'],
        'fields': ','.join([
            'id',
            'name',
            'picture.width(2000)',
            'first_name',
            'last_name',
        ])
    }
    response = requests.get(url, params)
    response_dict = response.json()
    # {
    #  'id': '10102332690796353',
    #  'name': 'Seungri Cho',
    #  'picture':
    #      {'data':
    #           {'height': 267,
    #            'is_silhouette': False,
    #            'url': 'https://scontent.xx.fbcdn.net/v/t1.0-1/1928830_530150637323_3300_n.jpg?oh=281e1e30290b7ef3927a12374fb4c049&oe=5B0F90E7',
    #             'width': 200}
    #       },
    #  'first_name': 'Seungri',
    #  'last_name': 'Cho'
    #  }
    facebook_id = response_dict['id']
    name = response_dict['name']
    first_name = response_dict['first_name']
    last_name = response_dict['last_name']
    url_picture = response_dict['picture']['data']['url']

    # facebook_id가 username인 User가 존재할 경우
    if User.objects.filter(username=facebook_id):
        user = User.objects.get(username=facebook_id)
    # 존재하지 않으면 새 유저를 생성
    else:
        user = User.objects.create_user(
            username=facebook_id,
            first_name=first_name,
            last_name=last_name,
        )
    # 해당 유저를 로그인 시킴
    login(request, user)
    return redirect('index')
