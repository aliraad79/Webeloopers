from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
import json

from base.forms import SignUpForm, LogInForm, ContactUSForm, MakeCourseForm
from base.models import Course, UserCourse

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
            form.save()
            data = form.cleaned_data
            form.save()
            usercourse = UserCourse(user_name=request.POST['username'], course_nums_json=json.dumps([]))
            usercourse.save()
            if not pass_error and not username_error:
                user = authenticate(request, username=data.get('username'), password=data.get('password1'))
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
        form = LogInForm()
    return render(request, 'LogIn.html', {'form': form, 'error': error, 'wrong_info': wrong_info})


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                str(data.get('title')),
                data.get('text') + str('\n') + str(data.get('email')),
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
    return redirect('/')


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
                if first_name != '':
                    i.first_name = first_name
                if last_name != '':
                    i.last_name = last_name
                i.save()
                break

        return render(request, 'profile.html')
    return render(request, 'edit_profile.html')


def all_courses_view(request):
    data = None
    if request.method == "POST":
        query = request.POST["search_query"]
        data = Course.objects.filter(department=query)
        # depart = request.POST.get('department') == 'department'
        # teacher = request.POST.get('teacher') == 'teacher'
        # course = request.POST.get('course') == 'course'
        # query = request.POST["search_query"]
        # if not depart and not course and not teacher:
        #     data = Course.objects.filter(department=query)
        # else:
        #     data1 = Course.objects.none()
        #     data2 = Course.objects.none()
        #     data3 = Course.objects.none()
        #     if depart:
        #         data1 = Course.objects.filter(department=query)
        #     if teacher:
        #         data2 = Course.objects.filter(teacher=query)
        #     if course:
        #         data3 = Course.objects.filter(name=query)
        #     data = (data1 | data2 | data3).distinct()
    alldata = Course.objects.all()
    # usecourses = getusercourses(request.user.username)
    return render(request, 'all_courses.html', {'courses': data, 'alldata': alldata})


def getusercourses(username):
    user = None
    for usercourse in UserCourse.objects.all():
        if usercourse.user_name == username:
            user = usercourse
    courses = json.loads(user.course_nums_json)
    mycourses = Course.objects.none()
    for coursenum in courses:
        mycourses |= Course.objects.filter(course_number=coursenum)
    return mycourses


def getAllCourse():
    return Course.objects.all()


def choose_course_view(request):
    course_num = request.GET.get('num', '')
    user_course = None
    for usercourse in UserCourse.objects.all():
        if usercourse.user_name == request.user.username:
            user_course = usercourse
            break
    courses = json.loads(user_course.course_nums_json)
    if course_num not in courses:
        courses.append(course_num)
    courses = json.dumps(courses)
    user_course.course_nums_json = courses
    user_course.save()

    mycourses = Course.objects.none()
    courses = json.loads(courses)
    for coursenum in courses:
        mycourses |= Course.objects.filter(course_number=coursenum)
    alldata = Course.objects.all()
    return redirect('/all_courses/', {'mycourses': mycourses, 'alldata': alldata})


def remove_course(request):
    course_num = request.GET.get('num', '')
    user_course = None
    for usercourse in UserCourse.objects.all():
        if usercourse.user_name == request.user.username:
            user_course = usercourse
            break
    courses = json.loads(user_course.course_nums_json)
    if course_num in courses:
        courses.remove(course_num)
    courses = json.dumps(courses)

    user_course.course_nums_json = courses
    user_course.save()

    mycourses = Course.objects.none()
    courses = json.loads(courses)
    for coursenum in courses:
        mycourses |= Course.objects.filter(course_number=coursenum)
    alldata = Course.objects.all()
    return redirect('/all_courses/', {'mycourses': mycourses, 'alldata': alldata})
