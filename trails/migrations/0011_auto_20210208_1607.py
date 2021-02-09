# Generated by Django 3.1.2 on 2021-02-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('trails', '0010_trail_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='points',
        ),
        migrations.AddField(
            model_name='trail',
            name='points',
            field=models.ManyToManyField(to='map.Point'),
        ),
    ]
