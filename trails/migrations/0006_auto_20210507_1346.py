# Generated by Django 3.1.2 on 2021-05-07 11:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trails', '0005_trail_for_whom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='watched',
        ),
        migrations.AddField(
            model_name='trail',
            name='watched',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
