# Generated by Django 3.1.2 on 2021-04-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210423_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='apartment_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='house_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='main_language',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_language',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]