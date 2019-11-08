from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.forms import SignUpForm, LogInForm, ContactUSForm, MakeCourseForm

# Create your views here.
from webelopers import settings


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
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                str(data.get('title')) + str('\n') + str(data.get('email')),
                data.get('text'),
                settings.EMAIL_HOST_USER,
                ['webe19lopers@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'succes.html', {'form': form})
    else:
        form = ContactUSForm()
    return render(request, 'contact_us.html', {'form': form})


def logout_view(request):
    logout(request)
    return home_page(request)


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def panel_view(request):
    return render(request, 'panel.html')


# todo
def make_new_course_view(request):
    if request.method == 'POST':
        form = MakeCourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MakeCourseForm()
    return render(request, 'make_new_course.html', {'form': form})


def edit_profile_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        for i in User.objects.all():
            if i == request.user:
                i.first_name = first_name
                i.last_name = last_name
        if first_name != '':
            request.user.first_name = first_name
        if last_name != '':
            request.user.last_name = last_name
        return profile_view(request)
    return render(request, 'edit_profile.html')
