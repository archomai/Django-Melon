from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

from members.forms import SignupForm

User = get_user_model()


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


def logout_view(request):
    # /logout/
    # 문서에서 logout <- django logout 검색
    # GET 요청이든 POST 요청이든 상관없음
    logout(request)
    return redirect('index')


def signup_view(request):
    # /signup/
    # username, password, password2가 전달되었다는 가정
    #  password, password2가 같은지도 확인
    # username이 중복되는지 검사, 존재하지 않으면 유정 생성 후 index로 이동
    # 이외의 경우는 다시 회원가입화면으로

    # SignupForm 인스턴스를 생성
    # 생성한 인스턴스를 context에 전달
    # 전달받은 변수를 템플릿에서 변수 렌더링
    # 어떻게 나오나 보기

    # 전달받은 데이터에 문제가 있을 경우, context['errors']를 채우고
    # 헤당 내용을 signup.html템플릿에서 출력
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'signup_form': form,
    }

    return render(request, 'members/signup.html', context)
