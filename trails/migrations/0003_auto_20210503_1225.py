# Generated by Django 3.1.2 on 2021-05-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0002_auto_20210430_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='country',
            field=models.CharField(choices=[('Polska', 'Polska'), ('Niemcy', 'Niemcy'), ('Czechy', 'Czechy'), ('Słowacja', 'Słowacja'), ('Rosja', 'Rosja'), ('Ukraina', 'Ukraina'), ('Białoruś', 'Białoruś'), ('Litwa', 'Litwa'), ('Estonia', 'Estonia'), ('Włochy', 'Włochy'), ('Izraelski', 'Izraelski')], max_length=15),
        ),
    ]