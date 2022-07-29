from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

#로그인 함수
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('main')

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['email'] == "swu.ac.kr" or "sungshin.ac.kr" or "ewhain.net" or "sookmyung.ac.kr" or "dongduk.ac.kr" or "duksung.ac.kr" :
            if request.POST['password'] == request.POST['repeat']:
                new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['username'] +'@' +request.POST['email'])
                auth.login(request, new_user)
                return redirect('main')
    return render(request, 'signup.html')