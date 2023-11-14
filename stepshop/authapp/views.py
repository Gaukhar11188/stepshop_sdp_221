from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from mainapp.views import get_data


def login(request):
    title = 'Вход'
    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = get_data(title=title, login_form=login_form)

    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'Регистрация'

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()

    context = get_data(title=title, register_form=register_form)

    return render(request, 'register.html', context)

