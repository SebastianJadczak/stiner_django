from django.contrib.auth.models import User
from django.db import models

class Trail(models.Model):
    COUNTRY_TRAIL=(
        ('Polska', 'Polska'),
        ('Niemcy', 'Niemcy')
    )
    TYPE_TRAIL=(
        ('Krajoznawcza', 'krajoznawcza'),
        ('Rodzinna', 'Rodzinna'),
        ('Górska', 'Górska'),
        ('Wymagająca', 'Wymagająca'),
        ('Wakacyjna', 'Wakacyjna'),
        ('Inna', 'Inna')
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    country = models.CharField(max_length=15, choices=COUNTRY_TRAIL)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=15, choices=TYPE_TRAIL)
    image = models.ImageField(upload_to='media/img_trail/%Y/%m%d', blank=True)
    average_grade = models.DecimalField(max_digits=2, decimal_places=1)
    watched = models.IntegerField()
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Rate_trail(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    opinion = models.TextField()