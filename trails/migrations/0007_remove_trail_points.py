# Generated by Django 3.0.5 on 2020-05-15 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='points',
        ),
    ]
