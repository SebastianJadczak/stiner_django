from django.db import models

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