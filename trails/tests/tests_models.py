from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Trail, Rate_trail


class TrailModelTestCase(TestCase):
    """Klasa odpowiedzialna za testy dla modelu Trail."""

    def setUp(self):
        """Zdefiniowanie obiektu na podstawie modelu."""
        self.trail = Trail.objects.create(name='Testowa', descriptions='Przykładowy opis trasy', country='Polska',
                                          region='Mazury', city='', type='Rekreacyjna', image=None, average_grade=4.0,
                                          watched=100,
                                          popular=True)
        self.user = User.objects.create_user(username='admin', password='Test123')
        self.rate_trail = Rate_trail.objects.create(user=self.user, trail=self.trail, rate=5, opinion='Testowa opinia')

    def test_set_Trail(self):
        """Test tworzenia i zapisu obiektu w bazie."""
        self.assertIsNotNone(self.trail.id)

    def test_set_Rate_Trail(self):
        """Test tworzenia opini trasy."""
        self.assertIsNotNone(self.rate_trail.id)
