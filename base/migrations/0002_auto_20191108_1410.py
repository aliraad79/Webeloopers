# Generated by Django 2.2.7 on 2019-11-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouruser',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
