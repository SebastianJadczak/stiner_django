from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='media/img_trail/%Y/%m%d', blank=True)

    def __str__(self):
        return self.name
