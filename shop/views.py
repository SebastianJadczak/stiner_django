from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.generic import DetailView
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin, View, TemplateView
from rest_framework.utils import json

from cart.forms import CartAddProductForm
from .models import Category, Product, Message
from django.views.generic.list import ListView


class ProductContentListView(TemplateResponseMixin, View):
    """ Klasa odpowiedzialna za wyświetlenie wszystkich produktów """
    template_name = 'shop/products/list.html'

    def get(self, request, pk=None):
        category = Category.objects.all()
        products = Product.objects.all()
        if pk:
            products = Product.objects.filter(category=pk)
            self.template_name = 'shop/products/category.html'
        return self.render_to_response({'products': products,
                                        'category': category})


class ProductDetailListView(TemplateResponseMixin,View):
    template_name = 'shop/products/product/detail.html'

    def get(self, request, id_product):
        product = get_object_or_404(Product,id=id_product)
        cart_product_form = CartAddProductForm()
        category = Category.objects.all()
        return self.render_to_response({'product': product, 'cart_product_form':cart_product_form, 'category':category})


class RecipientMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""
    def get_queryset(self):
        qs = super(RecipientMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, important=False)

def test(request):
    xx = request.POST
    zz = dict(xx.lists())
    my_list = []
    for key, value in zz.items():
        my_list.append(value)
    for i in my_list[1]:
        message = Message.objects.get(id=i)
        message.important = True
        message.save()
    return HttpResponse(request.GET.get('data',''))

class MessagesBox(RecipientMixin, ListView):
    """Klasa odpowiedzialna za wyświetlenie wiadomości odebranych"""
    template_name = 'shop/user/messages/messages-box.html'
    model = Message






class AuthorMixin(object):
    """Mixin który filtruje wiadomości po autorze"""
    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user)

class MessagesBoxSend(AuthorMixin, ListView):
    """Klasa odpowiedzialna za wyświetlenie wiadomości wysłanych"""
    template_name = 'shop/user/messages/messages-box-send.html'
    model = Message