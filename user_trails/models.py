from django.contrib.auth.models import User
from django.db import models

from map.models import Point


class UserTrail(models.Model):

    COUNTRY_TRAIL = (('Polska', 'Polska'),
                     ('Niemcy', 'Niemcy'),
                     ('Czechy', 'Czechy'),
                     ('Słowacja', 'Słowacja'),
                     ('Rosja', 'Rosja'),
                     ('Ukraina', 'Ukraina'),
                     ('Białoruś', 'Białoruś'),
                     ('Litwa', 'Litwa'),
                     ('Estonia', 'Estonia'),
                     ('Włochy', 'Włochy'),
                     ('Izrael', 'Izrael'),
                     ('Różne', 'Różne'))
    TYPE_TRAIL = (
        ('Krajoznawcza', 'krajoznawcza'),
        ('Rodzinna', 'Rodzinna'),
        ('Górska', 'Górska'),
        ('Wymagająca', 'Wymagająca'),
        ('Wakacyjna', 'Wakacyjna'),
        ('Inna', 'Inna')
    )
    REGION = (
        ('Góry', 'Góry'),
        ('Pojezierze', 'Pojezierze'),
        ('Morze', 'Morze'),
        ('Nizinny', 'Nizinny')
    )
    """Model odpowiedzialny za trasę użytkownika."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    country = models.CharField(max_length=15, choices=COUNTRY_TRAIL, default='Polska')
    region = models.CharField(max_length=15, choices=REGION, default='Nizinny')
    city = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_TRAIL, blank=True )
    image = models.ImageField(upload_to='media/img_trail/%Y/%m%d', blank=True)
    average_grade = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    watched = models.IntegerField(blank=True, default=False)
    popular = models.BooleanField(default=False)
    auditions = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    done = models.ManyToManyField(User, blank=True, related_name='done_your_trail')
    heart = models.ManyToManyField(User, blank=True, related_name='heart_your_trail')
    points = models.ManyToManyField(Point)

    def __str__(self):
        return self.name

class UserPoint(models.Model):
    """Model przechowywujący informacje o punkcie w trasie użytkownika."""

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    location = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    image = models.ImageField()
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.name