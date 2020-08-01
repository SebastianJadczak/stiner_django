import json
from urllib import request

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, TemplateView, DetailView

from cart.forms import CartAddProductForm
from map.models import Point
from trails.models import Trail


class UserTrailsListView(ListView):
    """Klasa odpowiedzialna za wyświetlenie widoku Tras zwiedzania użytkowników"""
    template_name = 'trails/user_trails/user_trails.html'
    model = Trail


class UserTrailFormAdd(ListView):
    """Klasa odpowiedzialna za wyświetlenie obiektów które możesz dodasz do szkicu trasy"""
    template_name ='trails/user_trails/form_trails.html'
    model = Point
    list = Point.objects.all()
    user = []
    zmienna = ""


    def z(self, query):
        for a in self.user:
            for z in a:
                if query == str(z):
                    return False

    def get(self, request, *args, **kwargs):
        request.GET._mutable = True
        query = request.GET.get('add_point')
        if query:
            z = self.z(query)
            if z == False:
                self.zmienna+="Nie możesz dodać tego zabytku. Istnieje już w bazie"
            else:
                self.user.append(self.list.filter(name=query))
        len_user = len(self.user)

        return render(request, self.template_name,
                      {'list': self.list, 'user':self.user, 'len_user':len_user, 'zmienna':self.zmienna })

class UserTrailDraft(UserTrailFormAdd):
    """Klasa odpowiedzialna za Szkic trasy zwiedzania"""
    template_name = 'trails/user_trails/draft/trail.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DetailPoint(DetailView):
    template_name = 'trails/user_trails/detail.html'
    model = Point

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



