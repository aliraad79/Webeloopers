from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from base.models import Course


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(max_length=40, required=True)
    password2 = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LogInForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1')


class ContactUSForm(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea(), min_length=10, max_length=250)

    class Meta:
        model = User
        fields = '__all__'


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class MakeCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_time"].input_formats = ["%H:%M"]
        self.fields["end_time"].input_formats = ["%H:%M"]
        self.fields["exam_date"].input_formats = ["%YYYY-%MM-%DD"]

    class Meta:
        model = Course
        fields = '__all__'
