from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post

class PostModelTestCase(TestCase):
    """Klasa odpowiedzialna za testy dla modelu Post."""

    def setUp(self):
        """Zdefiniujemy obiekty na podstawie modelu."""
        self.user = User.objects.create_user(username='admin', password='Test123')
        self.post = Post.objects.create(owner=self.user, title='Przykładowy post', slug='Przykładowy post',  image='../static/img/logo.png', body='Przykładowa treść',
                                        short_description='Krótki opis')

    def test_set_Post(self):
        """Test tworzenia i zapisu obiektu w bazie."""
        self.assertIsNotNone(self.post.id)
