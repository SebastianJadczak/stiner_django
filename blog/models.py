from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):

    STATUT_CHOICES = (
        ('draft', 'Szkic'),
        ('published', 'Opublikowany'),
    )

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUT_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title