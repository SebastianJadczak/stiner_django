# Generated by Django 3.0.5 on 2020-05-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_remove_point_trails'),
        ('trails', '0002_auto_20200508_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='trails',
            field=models.ManyToManyField(to='map.Point'),
        ),
    ]
