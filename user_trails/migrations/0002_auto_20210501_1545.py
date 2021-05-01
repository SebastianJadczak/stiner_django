# Generated by Django 3.1.2 on 2021-05-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_trails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrail',
            name='average_grade',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='country',
            field=models.CharField(choices=[('Polska', 'Polska'), ('Niemcy', 'Niemcy'), ('Czechy', 'Czechy'), ('Słowacja', 'Słowacja'), ('Rosja', 'Rosja'), ('Ukraina', 'Ukraina'), ('Białoruś', 'Białoruś'), ('Litwa', 'Litwa'), ('Estonia', 'Estonia'), ('Włochy', 'Włochy'), ('Izrael', 'Izrael')], default='Polska', max_length=15),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/img_trail/%Y/%m%d'),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='region',
            field=models.CharField(choices=[('Góry', 'Góry'), ('Pojezierze', 'Pojezierze'), ('Morze', 'Morze'), ('Nizinny', 'Nizinny')], default='Nizinny', max_length=15),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='type',
            field=models.CharField(blank=True, choices=[('Krajoznawcza', 'krajoznawcza'), ('Rodzinna', 'Rodzinna'), ('Górska', 'Górska'), ('Wymagająca', 'Wymagająca'), ('Wakacyjna', 'Wakacyjna'), ('Inna', 'Inna')], max_length=15),
        ),
        migrations.AddField(
            model_name='usertrail',
            name='watched',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
