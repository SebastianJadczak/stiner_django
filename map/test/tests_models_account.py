from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Profile, Preference

class PostModelTestCase(TestCase):
    """Klasa odpowiedzialna za testy dla modeli Profile i Preference."""

    def setUp(self):
        """Zdefiniujemy obiekty na podstawie modelu."""
        self.user = User.objects.create_user(username='admin', password='Test123')
        self.profile = Profile.objects.create()


    def test_set_Profile(self):
        """Test sprawdzenia czy obiekt został stworzony."""
        self.assertIsNotNone()

    def test_set_Preference(self):
        """Test sprawdzenia czy obiekt został stworzony."""
        self.assertIsNotNone()