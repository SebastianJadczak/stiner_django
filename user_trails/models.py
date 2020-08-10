from django.contrib.auth.models import User
from django.db import models

class UserTrail(models.Model):
    """Model odpowiedzialny za trasę użytkownika."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descriptions = models.TextField()

    def __str__(self):
        return self.name

class UserPoint(models.Model):
    """Model przechowywujący informacje o punkcie w trasie użytkownika."""

    trails = models.ForeignKey(UserTrail, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    location = models.CharField(max_length=30)
    coordinateX = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    coordinateY = models.DecimalField(max_length=30, decimal_places=7, max_digits=100)
    image = models.ImageField()
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.name