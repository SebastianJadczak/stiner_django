# Generated by Django 3.1.2 on 2020-10-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
    ]
