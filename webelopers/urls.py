from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from base.views import home_page, signup, login_view, contact_us_view, logout_view, profile_view, edit_profile_view, \
    panel_view, make_new_course_view, all_courses_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('sign_up/', signup, name='signup'),
    path('login/', login_view),
    path('contact_us/', contact_us_view),
    path('logOut/', logout_view),
    path('Profile/', profile_view),
    path('editProfile/', edit_profile_view),
    path('panel/', panel_view),
    path('make_new_course/', make_new_course_view),
    path('all_courses/', all_courses_view)
]
