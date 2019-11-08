# Generated by Django 2.2.7 on 2019-11-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('course_number', models.DecimalField(decimal_places=0, max_digits=19, max_length=30)),
                ('group_number', models.DecimalField(decimal_places=0, max_digits=19, max_length=30)),
                ('teacher', models.CharField(max_length=30)),
                ('start_time', models.TimeField(max_length=30)),
                ('end_time', models.TimeField(max_length=30)),
                ('first_day', models.CharField(choices=[('0', 'saturday'), ('1', 'sunday'), ('2', 'monday'), ('3', 'tuesday'), ('4', 'wednesday')], max_length=30)),
                ('second_day', models.CharField(blank=True, choices=[('0', 'saturday'), ('1', 'sunday'), ('2', 'monday'), ('3', 'tuesday'), ('4', 'wednesday')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('course_nums_json', models.CharField(max_length=100)),
            ],
        ),
    ]
