
from django.test import TestCase

from map.models import Coordinates

class MapModelTestCase(TestCase):
    """Klasa odpowiedzialna za testy dla modelu Trail."""

    def setUp(self):
        """Zdefiniowanie obiektu na podstawie modelu."""
        self.city = Coordinates.objects.create(name='Kraków', coordinateX=50.0556332, coordinateY=19.408547 )

    def test_set_Coordinates(self):
        """Test tworzenia i zapisu obiektu w bazie."""
        self.assertIsNotNone(self.city.id)


