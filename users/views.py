from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm



def login(request):
    if request.method == 'POST': #если формируется post запрос
        form = UserLoginForm(data=request.POST) #импортируем форму userloginform
        if form.is_valid():
            username = request.POST['username'] #достаем из формы логин и пароль
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) #проверяем логин и пароль
            if user: #если пользователь есть, то авторизуем его и отправим на главную страницу
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html',context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)