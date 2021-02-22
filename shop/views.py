from random import randint

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import context
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from cart.forms import CartAddProductForm
from .models import Category, Product, Message
from django.views.generic.list import ListView


class Search(TemplateView):
    """Klasa bazowa odpowiedzialna za odnalezienie produktu i wyświetlenie wyniku wyszukania"""
    template_name = 'shop/search/search.html'

    def search(self, xx):
        zz = dict(xx.lists())
        my_list = []
        for key, value in zz.items():
            my_list.append(value)
        products = Product.objects.filter(name=my_list[0][0])

        return products

    def get(self, request, **kwargs):
        category = Category.objects.all()
        put_up_for_sale = Product.objects.filter(owner=self.request.user, sold=False, available=True)
        sold = Product.objects.filter(owner=self.request.user, sold=True, available=False)
        unsold_product = Product.objects.filter(owner=self.request.user, sold=False, available=False)
        purchased_products = Product.objects.filter(sold=True, available=False, bought_by=self.request.user)
        return self.render_to_response(
            {'category': category, 'put_up_for_sale': put_up_for_sale, 'sold': sold, 'unsold': unsold_product,
             'purchased_products': purchased_products})

    def post(self, request):
        category = Category.objects.all()
        xx = request.POST
        products = self.search(xx)
        self.template_name = 'shop/search/search.html'
        return self.render_to_response({'products': products,
                                        'category': category})


class ProductContentListView(Search, TemplateResponseMixin):
    """ Klasa odpowiedzialna za wyświetlenie wszystkich produktów """
    template_name = 'shop/products/list.html'

    def get(self, request, pk=None):
        category = Category.objects.all()
        products = Product.objects.all()
        random_product = Product.objects.filter(id=randint(2, 5))[0]
        slice_products = products[:5]
        print(random_product)
        print(randint(1, 6))
        if pk:
            products = Product.objects.filter(category=pk)
            self.template_name = 'shop/search/search.html'
        return self.render_to_response({'products': products,
                                        'category': category,
                                        'slice_products':slice_products,
                                        'random_product': random_product})


class ProductDetailListView(Search, TemplateResponseMixin, View):
    template_name = 'shop/products/product/detail.html'

    def get(self, request, id_product):
        product = get_object_or_404(Product, id=id_product)
        cart_product_form = CartAddProductForm()
        category = Category.objects.all()
        return self.render_to_response(
            {'product': product, 'cart_product_form': cart_product_form, 'category': category})


# -------------------------------------------
# Widoki odpowiedzialne za wiadomości

class RecipientMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""

    def get_queryset(self):
        qs = super(RecipientMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, important=False, delete=False)


def important(request):
    xx = request.POST
    zz = dict(xx.lists())
    my_list = []
    for key, value in zz.items():
        my_list.append(value)
    for i in my_list[1]:
        message = Message.objects.get(id=i)
        message.important = True
        message.save()
    return HttpResponse(request.GET.get('data', ''))


class CategoryProductInMessage(ListView):
    def get_context_data(self, **kwargs):
        context = super(CategoryProductInMessage, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class MessagesBox(RecipientMixin, CategoryProductInMessage):
    """Klasa odpowiedzialna za wyświetlenie wiadomości odebranych"""
    template_name = 'shop/user/messages/messages-box.html'
    model = Message


class AuthorMixin(object):
    """Mixin który filtruje wiadomości po autorze"""

    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user, delete=False, important=False)


class MessagesBoxSend(AuthorMixin, CategoryProductInMessage):
    """Klasa odpowiedzialna za wyświetlenie wiadomości wysłanych"""
    template_name = 'shop/user/messages/messages-box-send.html'
    model = Message


class ImportantMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""

    def get_queryset(self):
        qs = super(ImportantMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, important=True, delete=False)


class MessagesBoxImportant(ImportantMixin, CategoryProductInMessage):
    """Klasa odpowiedzialna za wyświetlenie ważnych wiadomości"""
    template_name = 'shop/user/messages/messages-box-important.html'
    model = Message


class DeleteMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""

    def get_queryset(self):
        qs = super(DeleteMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, delete=True)


class MessagesBoxDelete(DeleteMixin, CategoryProductInMessage):
    """Klasa odpowiedzialna za wyświetlenie wiadomości wysłanych"""
    template_name = 'shop/user/messages/messages-box-delete.html'
    model = Message


def delete(request):
    """Metoda odpowiedzialna za usunięcie wiadomości ze skrzynek"""
    xx = request.POST
    zz = dict(xx.lists())
    my_list = []
    for key, value in zz.items():
        my_list.append(value)
    for i in my_list[1]:
        message = Message.objects.get(id=i)
        message.delete = True
        message.save()
    return HttpResponse(request.GET.get('data', ''))


def MessagesBoxNew(request):
    """ metoda odpowiedzialna za wyświetlenie wszystkich produktów """
    template_name = 'shop/user/messages/messages-new.html'
    category = Category.objects.all()
    if request.POST:
        author = request.POST.get('author')
        recipient = request.POST.get('recipient')
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_author = User.objects.get(username=author)
        try:
            user_recipient = User.objects.get(username=recipient)
            new_message = Message(author=user_author, recipient=user_recipient, title=title, content=content)
            new_message.save()
            text = 'Twoja wiadomość została wysłana'
        except:
            text = 'Taki użytkownik nie istnieje'

        return render(request, template_name, {'text': text, 'category': category})
    return render(request, template_name, {'category': category})


# -------------------------------------------------------------------------------
# Sekcja Konto Użytkownika


class PutUpForSale(Search, TemplateResponseMixin):
    """Klasa odpowiedzialna za wyświetlenie produktów wystawionych na sprzedaż przez danego użytkownika."""
    template_name = 'shop/user/account/put_up_for_sale.html'


class SellProduct(Search, TemplateResponseMixin):
    """Klasa odpowiedzialna za wyświetlenie sprzedanych produktów"""
    template_name = 'shop/user/account/sell_product.html'


class UserData(Search, TemplateResponseMixin):
    """Klasa odpowiedzialna za wyświetlenie danych użytkownika"""
    template_name = 'shop/user/account/user_data.html'


class Payments(Search, TemplateResponseMixin):
    """Klasa odpowiedzialna za wyświetlenie danych o płatnościach"""
    template_name = 'shop/user/account/payments.html'


class PurchasedProducts(Search, TemplateResponseMixin):
    """Klasa odpowiedzialna za wyświetlenie danych o kupionych produktach"""
    template_name = 'shop/user/account/purchased_products.html'


class UnsoldProduct(Search, TemplateResponseMixin):
    template_name = 'shop/user/account/unsold_product.html'
