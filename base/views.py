from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from base.forms import SignUpForm, LogInForm, ContactUSForm


# Create your views here.

def test(request):
    return render(request, 'Base.html', {'is_login': 1})


def home_page(request, *args):
    if args:
        return render(request, 'homePage.html', {'is_login': args[0]})
    return render(request, 'homePage.html', {'is_login': False})


def signup(request):
    username_error = False
    pass_error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST['”user_name”'])
        data = form.cleaned_data
        username = data.get('user_name')
        print(username)
        if form.is_valid():
            form.save()
            raw_password = data.get('password1')
            repeated_password = data.get('password2')
            for i in User.objects.all():
                if i.username == username:
                    username_error = True
            if raw_password != repeated_password:
                pass_error = True
            if not pass_error and not username_error:
                user = authenticate(username=username, password=raw_password)
                login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form, 'username_error': username_error, 'pass_error': pass_error})


def login_view(request):
    error = bool
    if request.method == 'POST':
        form = LogInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return home_page(request, request.user.is_authenticated)
        else:
            error = True
    else:
        error = False
        form = SignUpForm()
    return render(request, 'LogIn.html', {'form': form, 'error': error})


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        print(form)
        if form.is_valid():
            return render(request, 'succes.html', {'form': form})
    else:
        form = ContactUSForm()
    return render(request, 'contact_us.html', {'form': form})
