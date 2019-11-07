from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from base.views import home_page, signup, login_view, test, signup_dup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('sign_up/', signup),
    path('sign_up/sign_up/', signup_dup),
    path('login/', login_view),
]
