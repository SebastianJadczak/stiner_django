# Generated by Django 3.0.5 on 2020-04-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/category/%Y/%m/%d'),
        ),
    ]
