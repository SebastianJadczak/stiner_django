# Generated by Django 3.1.2 on 2021-02-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('user_trails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoint',
            name='trails',
        ),
        migrations.AddField(
            model_name='usertrail',
            name='points',
            field=models.ManyToManyField(to='map.Point'),
        ),
    ]
