# Generated by Django 3.1.2 on 2020-11-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201028_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='important',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]