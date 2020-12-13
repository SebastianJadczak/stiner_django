from django.db import models
from django.conf import settings

class Profile(models.Model):
    """Nadpisanie modelu User."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=30)
    surname = models.TextField(max_length=30)
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
    phone = models.TextField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)

    def full_name(self):
        return '{} {}'.format(self.name, self.surname)


class Preference(models.Model):
    """Model preferencji użytkonika"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_country = models.TextField(max_length=30, blank=True, null=True)
    favorite_region = models.TextField(max_length=30, blank=True, null=True)
    favorite_city = models.TextField(max_length=30, blank=True, null=True)
    favorite_place = models.TextField(max_length=30, blank=True, null=True)
    favorite_restaurant = models.TextField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "Preferencje"