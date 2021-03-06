from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    """ Klasa odpowiedzialna z wygląd koszyka na zakupy """

    def __init__(self, request):
        """ Inicjalizacja koszyka na zakupy """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """ Iteracja po produktach i pobranie obiektów z bazy """

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """ obliczamy liczbę wszystkich obiektów w koszyku """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ Metoda zliczająca 'wartość' koszyka """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """ Usunięcie koszyka z sesji """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def add(self, product, quantity=1, update_quantity=False):
        """ Dodanie / lub zmiana ilości towaru w koszyku """
        print(str(product.id))
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """ Oznacznie sesji jako zmodyfikowana """
        self.session.modified = True

    def remove(self, product):
        """ usuwanie produktów z koszyka """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
