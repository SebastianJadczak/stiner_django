# Generated by Django 3.1.2 on 2020-10-20 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]
