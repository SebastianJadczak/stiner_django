from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View

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
    return HttpResponse(request.GET.get('data',''))

class MessagesBox(RecipientMixin, ListView):
    """Klasa odpowiedzialna za wyświetlenie wiadomości odebranych"""
    template_name = 'shop/user/messages/messages-box.html'
    model = Message

class AuthorMixin(object):
    """Mixin który filtruje wiadomości po autorze"""
    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user, delete=False, important=False)

class MessagesBoxSend(AuthorMixin, ListView):
    """Klasa odpowiedzialna za wyświetlenie wiadomości wysłanych"""
    template_name = 'shop/user/messages/messages-box-send.html'
    model = Message


class ImportantMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""
    def get_queryset(self):
        qs = super(ImportantMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, important=True, delete=False)

class MessagesBoxImportant(ImportantMixin, ListView):
    """Klasa odpowiedzialna za wyświetlenie ważnych wiadomości"""
    template_name = 'shop/user/messages/messages-box-important.html'
    model = Message

class DeleteMixin(object):
    """Mixin który filtruje wiadomości po odbiorcy"""
    def get_queryset(self):
        qs = super(DeleteMixin, self).get_queryset()
        return qs.filter(recipient=self.request.user, delete=True)

class MessagesBoxDelete(DeleteMixin, ListView):
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
    return HttpResponse(request.GET.get('data',''))

def MessagesBoxNew(request):
    """ metoda odpowiedzialna za wyświetlenie wszystkich produktów """
    template_name = 'shop/user/messages/messages-new.html'

    if request.POST:
        author = request.POST.get('author')
        recipient =request.POST.get('recipient')
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

        return render(request, template_name, {'text':text})
    return render(request, template_name)
