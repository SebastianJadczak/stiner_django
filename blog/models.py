from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):

    STATUT_CHOICES = (
        ('draft', 'Szkic'),
        ('published', 'Opublikowany'),
    )
    owner = models.ForeignKey(User, related_name='posts_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='media/img/%Y/%m%d')
    body = models.TextField()
    short_description = models.CharField(max_length=60)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUT_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title