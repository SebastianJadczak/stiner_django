from django.contrib.auth.models import User
from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='media/img_trail/%Y/%m%d', blank=True)
    average_grade = models.DecimalField(max_digits=2, decimal_places=1)
    watched = models.IntegerField()

    def __str__(self):
        return self.name

class Rate_trail(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    opinion = models.TextField()