from django.contrib.auth.models import User
from django.db import models
from django import forms


# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.DecimalField(max_length=30, decimal_places=0, max_digits=19)
    group_number = models.DecimalField(max_length=30, decimal_places=0, max_digits=19)
    teacher = models.CharField(max_length=30)
    start_time = models.TimeField(max_length=30)
    end_time = models.TimeField(max_length=30)
    CHOICES = (('0', 'saturday'), ('1', 'sunday'), ('2', 'monday'), ('3', 'tuesday'), ('4', 'wednesday'))
    first_day = models.CharField(choices=CHOICES, max_length=30)
    second_day = models.CharField(choices=CHOICES, max_length=30, blank=True)


class OurUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')

    def __init__(self, user, image=None):
        super(OurUser, self).__init__()
        self.user = user
        self.image = image


class UserCourse(models.Model):
    user_name = models.CharField(max_length=30)
    course_nums_json = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
