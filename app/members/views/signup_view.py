from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from members.forms import SignupForm

User = get_user_model()

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