from django.db import models
from django.conf import settings
from time import strptime


class Profile(models.Model):
    """Nadpisanie modelu User."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=30, null=True, blank=True)
    surname = models.TextField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/img/%Y/%m%d', null=True, blank=True)
    country = models.TextField(max_length=30, null=True, blank=True)
    city = models.TextField(max_length=30, null=True, blank=True)
    street = models.TextField(max_length=30, null=True, blank=True)
    house_number = models.IntegerField(max_length=30, null=True, blank=True)
    apartment_number = models.IntegerField(max_length=10,null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    main_language = models.CharField(max_length=25, null=True, blank=True)
    other_language = models.CharField(max_length=20, null=True, blank=True)
    phone = models.TextField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=50 ,null=True, blank=True)

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
        if date_with_model is not None:
            new_format = strptime(str(date_with_model), '%Y-%m-%d')
            return '{} {} {}'.format(new_format.tm_mday, self.MONTHS[new_format.tm_mon], new_format.tm_year)
        else:
            return None

    def language_fields_filled(self):
        """Sprawdza czy wszystkie pola z sekcji Adres są wypełnione."""
        user = list(Profile.objects.filter(user=self.user))
        len_section = 2
        section = []
        for element in user:
            if element.main_language: section.append(element.main_language)
            if element.other_language: section.append(element.other_language)
        if len(section) == 0: return self.COLORS[0]
        if len(section) < 2 and len(section) > 0:
            return self.COLORS[1]
        else:
            return self.COLORS[2]

    def address_fields_filled(self):
        """Sprawdza czy wszystkie pola z sekcji Adres są wypełnione."""
        user = list(Profile.objects.filter(user=self.user))
        len_section = 6
        section = []
        for element in user:
            if element.country: section.append(element.country)
            if element.city: section.append(element.city)
            if element.street: section.append(element.street)
            if element.house_number: section.append(element.house_number)
            if element.apartment_number: section.append(element.apartment_number)
            if element.postal_code: section.append(element.postal_code)
        if len(section) == 0: return self.COLORS[0]
        if len(section) < 6 and len(section) > 0:
            return self.COLORS[1]
        else:
            return self.COLORS[2]

    def contact_fields_filled(self):
        """Sprawdza czy wszystkie pola z sekcji Kontakt są wypełnione."""
        user = list(Profile.objects.filter(user=self.user))
        contact_fields = []
        self.address_fields_filled()
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

    COLORS = ['red', 'yellow', '#04d900']

    def preference_fields_filled(self):
        """Sprawdza czy wszystkie pola z sekcji Preferencje są wypełnione."""
        user = list(Preference.objects.filter(user=self.user))
        print(user)
        len_section = 5
        section = []
        for element in user:
            if element.favorite_country: section.append(element.favorite_country)
            if element.favorite_region: section.append(element.favorite_region)
            if element.favorite_city: section.append(element.favorite_city)
            if element.favorite_place: section.append(element.favorite_place)
            if element.favorite_restaurant: section.append(element.favorite_restaurant)
        if len(section) == 0: return self.COLORS[0]
        if len(section) < len_section and len(section) > 0:
            return self.COLORS[1]
        else:
            return self.COLORS[2]
