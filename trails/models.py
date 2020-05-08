from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField()

    def __str__(self):
        return self.name
