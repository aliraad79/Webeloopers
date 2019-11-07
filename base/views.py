from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.forms import SignUpForm, LogInForm, ContactUSForm


# Create your views here.


def home_page(request):
    return render(request, 'homePage.html')


def signup(request):
    username_error = False
    pass_error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            for i in User.objects.all():
                if i.username == request.POST['username']:
                    username_error = True
            if request.POST['password1'] != request.POST['password2']:
                pass_error = True
        except:
            pass
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            if not pass_error and not username_error:
                user = authenticate(username=data.get('username'), password=data.get('password1'))
                login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form, 'username_error': username_error, 'pass_error': pass_error})


def login_view(request):
    error = bool
    wrong_info = bool
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return home_page(request)
            else:
                wrong_info = True
    else:
        error = False
        form = SignUpForm()
    return render(request, 'LogIn.html', {'form': form, 'error': error, 'wrong_info': wrong_info})


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        print(form)
        if form.is_valid():
            return render(request, 'succes.html', {'form': form})
    else:
        form = ContactUSForm()
    return render(request, 'contact_us.html', {'form': form})


def logout_view(request):
    logout(request)
    return home_page(request)
