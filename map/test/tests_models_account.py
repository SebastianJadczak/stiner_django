
from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Profile, Preference

class PostModelTestCase(TestCase):
    """Klasa odpowiedzialna za testy dla modeli Profile i Preference."""

    def setUp(self):
        """Zdefiniujemy obiekty na podstawie modelu."""
        self.user = User.objects.create_user(username='admin', password='Test123')
        self.profile = Profile.objects.create(user=self.user, name='Sebastian', surname='Jadczak', date_of_birth='1990-6-21', photo=None, country='Polska',  city='Warszawa', street='Testowa', house_number=12,
                                              apartment_number=1, postal_code='01-111', main_language='Polish',  other_language="English", phone='123456789', email='test@test.pl')
        self.preference = Preference.objects.create(user=self.user, favorite_country='Polska', favorite_region='Mazury',
                                                    favorite_city='Kraków', favorite_place='Molo w Sopocie', favorite_restaurant='Dolce Vita')

    def test_set_Profile(self):
        """Test sprawdzenia czy obiekt został stworzony."""
        self.assertIsNotNone(self.profile.id)

    def test_method_full_name_Profile(self):
        """Test sprawdzający poprawność metody zwracającą imię i nazwisko użytkownika."""
        self.assertEqual(self.profile.full_name(), 'Sebastian Jadczak')

    def test_set_Preference(self):
        """Test sprawdzenia czy obiekt został stworzony."""
        self.assertIsNotNone(self.preference.id)