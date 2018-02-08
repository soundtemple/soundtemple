from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse_lazy


def login_page(request):
    return render(request, 'auth_user/login.html', {})


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'pages/home_page.html', {})
    else:
        return render(request, 'auth_user/login_fail.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'auth_user/logout.html', {})