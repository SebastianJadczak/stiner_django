from django.contrib.auth.models import User
from django.db import models


class Point(models.Model):
    TYPE_POINT = (
        ('Zamki', 'Zamki'),
        ('Forty', 'Forty'),
        ('Kościoły', 'Kościoły'),
        ('Muzeum', 'Muzeum'),
        ('Parki', 'Parki'),
        ('Ogrody', 'Ogrody'),
        ('Pomniki', 'Pomniki'),
        ('Rynki', 'Rynki'),
        ('Mosty', 'Mosty'),
        ('Wieże', 'Wieże'),
        ('Stadiony', 'Stadiony'),
        ('Cmentarze', 'Cmentarze'),
        ('Budowle', 'Budowle'),
        ('Porty', 'Porty'),
        ('Filcharmonie', 'Filcharmonie')
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    location = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    image = models.ImageField(upload_to='media/img_point/%Y/%m%d')
    type = models.CharField(max_length=15, choices=TYPE_POINT)

    def __str__(self):
        return self.name


class Opinion_about_Point(models.Model):
    """Model opisujący opinie o Punkcie."""
    user = models.CharField(max_length=30)
    opinion = models.CharField(max_length=530)
    rating = models.IntegerField()
    point = models.ForeignKey(Point, blank=True, on_delete=models.CASCADE)


class Coordinates(models.Model):
    """Model opisujący położenie miast."""
    name = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)

    def __str__(self):
        return self.name
