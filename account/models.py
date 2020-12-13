from django.db import models
from django.conf import settings
from time import strptime


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
    house_number = models.IntegerField(blank=True)
    apartment_number = models.IntegerField(blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    main_language = models.CharField(max_length=25, blank=True)
    other_language = models.CharField(max_length=20, blank=True)
    phone = models.TextField(max_length=10)
    email = models.EmailField()

    MONTHS = ['', 'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień',
              'Październik', 'Listopad', 'Grudzień']

    COLORS = ['red', 'yellow', '#04d900']

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)

    def full_name(self):
        """Metoda zwracająca imię i nazwisko użytkownika."""
        return '{} {}'.format(self.name, self.surname)

    def date_of_birth_user(self):
        date_with_model = self.date_of_birth
        new_format = strptime(str(date_with_model), '%Y-%m-%d')
        return '{} {} {}'.format(new_format.tm_mday, self.MONTHS[new_format.tm_mon], new_format.tm_year)

    def contact_fields_filled(self):
        """Sprawdza czy wszystkie pola z sekcji Kontakt są wypełnione."""
        user = list(Profile.objects.filter(user=self.user))
        contact_fields = []
        for element in user:
            if element.email:
                contact_fields.append(element.email)
            if element.phone:
                contact_fields.append(element.phone)
        return self.COLORS[len(contact_fields)]

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
