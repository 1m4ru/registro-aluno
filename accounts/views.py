from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = auth.authenticate(username=username, password=password)
        
        if check_user == None:
            messages.error(request, message='Usuário ou senha inválidos.')
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')



    else:
        return render(request, 'pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        User.objects.create_user(username=user, password=password, email=email)
        return redirect('login')

    else:
        return render(request, 'pages/register.html')
