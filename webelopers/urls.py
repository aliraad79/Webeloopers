from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from base.views import home_page, signup, login_view, contact_us_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('sign_up/', signup, name='signup'),
    path('login/', login_view),
    path('contact_us/', contact_us_view),
    path('logOut/', logout_view)
]
