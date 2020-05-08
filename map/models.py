from django.db import models

from trails.models import Trail


class Point(models.Model):

    TYPE_POINT = (
        ('castle', 'Zamek'),
        ('church', 'Kościół')
    )

    name = models.CharField(max_length=30)
    coordinateX = models.CharField(max_length=30)
    coordinateY = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/img_point/%Y/%m%d')
    descriptions = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_POINT)
    trails = models.ManyToManyField(Trail)

    def __str__(self):
        return self.name
