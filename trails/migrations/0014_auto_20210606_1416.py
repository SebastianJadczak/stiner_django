# Generated by Django 3.1.2 on 2021-06-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0013_trail_auditions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='auditions',
        ),
        migrations.AddField(
            model_name='trail',
            name='auditions',
            field=models.IntegerField(default=0),
        ),
    ]