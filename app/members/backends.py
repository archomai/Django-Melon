import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File

from utils.file import download, get_buffer_ext

User = get_user_model()


class FacebookBackend:
    CLIENT_ID = settings.FACEBOOK_APP_ID
    CLIENT_SECRET = settings.FACEBOOK_SECRET_CODE
    URL_ACCESS_TOKEN = 'https://graph.facebook.com/v2.12/oauth/access_token?'
    URL_ME = 'https://graph.facebook.com/v2.12/me'

    def authenticate(self, request, code):
        def get_access_token(auth_code):
            """
            유저가 페이스북에서 우리 애플리케이션 사용에 대해 '승인'한 경유ㅡ
            페이스북에서 우리 애플리케이션의 주소(redirect_uri)에 'code'라는 GET parameter로 전해주는
            인즈 코드 (auth_code)를 사용해서
            페이스북 GraphAPI access_token요청, 결과를 가져와 리턴
            :param auth_code: 유저가 페이스북에 로그인/앱 승인한 결과로 돌아오는
            :return:
            """
            redirect_uri = 'http://localhost:8000/facebook-login/'

            params_access_token = {
                'client_id': self.CLIENT_ID,
                'redirect_uri': redirect_uri,
                'client_secret': self.CLIENT_SECRET,
                'code': auth_code,
            }
            response = requests.get(self.URL_ACCESS_TOKEN, params_access_token)

            response_dict = response.json()
            return response_dict['access_token']

        def get_user_info(user_access_token):
            """
            User access token을 사용해서
            GrapthAPI의 'User' 항목을 리턴
                (엔드포인트 'me'를 사용해서 access_token에 해당하는 사용자의 정보를 가져옴)
            :param user_access_token
            :param access_token:
            :return:
            """
            params = {
                'access_token': user_access_token,
                'fields': ','.join([
                    'id',
                    'name',
                    'picture.width(2000)',
                    'first_name',
                    'last_name',
                ])
            }
            response = requests.get(self.URL_ME, params)
            response_dict = response.json()
            return response_dict

        try:
            access_token = get_access_token(code)
            user_info = get_user_info(access_token)

            facebook_id = user_info['id']
            name = user_info['name']
            first_name = user_info['first_name']
            last_name = user_info['last_name']
            url_picture = user_info['picture']['data']['url']

            try:
                user = User.objects.get(username=facebook_id)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=facebook_id,
                    first_name=first_name,
                    last_name=last_name,
                )
            if not user.img_profile:
                temp_file = download(url_picture)
                ext = get_buffer_ext(temp_file)
                user.img_profile.save(f'{user.pk}.{ext}', File(temp_file))
            return user
        except Exception:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
