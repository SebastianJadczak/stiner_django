from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin, View, TemplateView
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


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user)

class MessagesBox(OwnerMixin, ListView):
    template_name = 'shop/user/messages/messages-box.html'
    model = Message
