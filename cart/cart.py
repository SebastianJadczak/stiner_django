from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):

    def __init__(self,request):
        """ Inicjalizacja koszyka na zakupy """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart