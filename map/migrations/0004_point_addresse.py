# Generated by Django 3.1.2 on 2021-04-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_point_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='addresse',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
