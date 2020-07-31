# Generated by Django 3.0.3 on 2020-07-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_auto_20200520_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='coordinateX',
            field=models.DecimalField(decimal_places=7, max_digits=100, max_length=30),
        ),
        migrations.AlterField(
            model_name='point',
            name='coordinateY',
            field=models.DecimalField(decimal_places=7, max_digits=100, max_length=30),
        ),
    ]