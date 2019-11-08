# Generated by Django 2.2.7 on 2019-11-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_ouruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('course_nums_json', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
