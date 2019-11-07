from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    user_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(max_length=40, required=True)
    password2 = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = '__all__'


class LogInForm(forms.Form):
    user_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = '__all__'


class ContactUSForm(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'
