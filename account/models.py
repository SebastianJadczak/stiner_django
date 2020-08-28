from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Nadpisanie modelu User."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    country = models.TextField(max_length=30, blank=True)
    city = models.TextField(max_length=30, blank=True)
    street = models.TextField(max_length=30, blank=True)
    house_number = models.IntegerField( blank=True)
    apartment_number = models.IntegerField( blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    main_language = models.CharField(max_length=25, blank=True)
    other_language = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)