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


class UserCourse(models.Model):
    user_name = models.CharField(max_length=30)
    course_nums_json = models.CharField(max_length=100)
