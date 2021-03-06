from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

__all__ = (
    'login_view',
)


def login_view(request):
    # Post 요청일때는
    # authenticate -> login후 'index'로 redirect
    #
    # Get 요청일때는
    # members/login.html 파일을 보여줌
    #  해당 파일의 form에는 username, password input과 '로그인'버튼이 있음
    #  form은 method POST로 다시 이 view로의 action(빈 값)을 가짐
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'members/login.html')
