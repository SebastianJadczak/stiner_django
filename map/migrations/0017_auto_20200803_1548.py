# Generated by Django 3.0.4 on 2020-08-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0016_auto_20200803_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='type',
            field=models.CharField(choices=[('Zamki', 'Zamki'), ('Forty', 'Forty'), ('Kościoły', 'Kościoły'), ('Muzeum', 'Muzeum'), ('Parki', 'Parki'), ('Ogrody', 'Ogrody'), ('Pomniki', 'Pomniki'), ('Rynki', 'Rynki'), ('Mosty', 'Mosty'), ('Wieże', 'Wieże'), ('Stadiony', 'Stadiony'), ('Cmentarze', 'Cmentarze'), ('Budowle', 'Budowle'), ('Porty', 'Porty'), ('Filcharmonie', 'Filcharmonie')], max_length=15),
        ),
    ]