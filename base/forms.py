from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    user_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(max_length=40, required=True)
    password2 = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = '__all__'


class LogInForm(UserCreationForm):
    user_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = '__all__'
