from django.contrib.auth.models import User
from django.db import models

from map.models import Point


class Trail(models.Model):
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
                     ('Izrael', 'Izrael'))
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
    FOR_WHOM = (
        ('Dla wszystkich','Dla wszystkich') ,
        ('Dla dzieci', 'Dla dzieci'),
        ('Dla dorosłych', 'Dla dorosłych'),
        ('Dla sportowców', 'Dla sportowców'),
        ('Dla wymagających', 'Dla wymagających')
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    country = models.CharField(max_length=15, choices=COUNTRY_TRAIL)
    region = models.CharField(max_length=15, choices=REGION, default='Nizinny')
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=15, choices=TYPE_TRAIL)
    for_whom = models.CharField(max_length=25, choices=FOR_WHOM, default='Dla wszystkich')
    image = models.ImageField(upload_to='media/img_trail/%Y/%m%d', blank=True)
    average_grade = models.DecimalField(max_digits=2, decimal_places=1)
    done = models.ManyToManyField(User, blank=True, related_name='done_trail')
    done_count = models.IntegerField(default=0)
    auditions = models.IntegerField(default=0)
    heart = models.ManyToManyField(User, blank=True, related_name='heart_trail')
    downloads = models.IntegerField(default=0)
    popular = models.BooleanField(default=False)
    points = models.ManyToManyField(Point)

    def __str__(self):
        return self.name

    def get_type_trail(self):
        return self.TYPE_TRAIL

    def get_region_trail(self):
        return self.REGION

    def get_country_trail(self):
        return self.COUNTRY_TRAIL

class Rate_trail(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    opinion = models.TextField()