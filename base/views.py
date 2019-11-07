from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse

from base.forms import SignUpForm, LogInForm


# Create your views here.

def test(request):
    return render(request, 'Base.html', {'is_login': 1})


def signup_dup(request):
    return redirect('/sign_up')


def home_page(request, *args):
    if args:
        return render(request, 'homePage.html', {'is_login': args[0]})
    return render(request, 'homePage.html', {'is_login': False})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            username = data.get('username')
            raw_password = data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
        else:
            return render(request, 'sign_up.html', {'form': form, 'error': True})
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return home_page(request, request.user.is_authenticated)
            else:
                return render(request, '')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
