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
    template_name = 'trails/user_trails/user_trails.html'
    model = Trail


class UserTrailFormAdd(ListView):
    template_name ='trails/user_trails/form_trails.html'
    model = Point
    list = Point.objects.all()
    user = []

    def get(self, request, *args, **kwargs):
        query = request.GET.get('add_point')
        if query:
            self.user.append(self.list.filter(name=query))

            return redirect('user_trails:user_trail_add')
        len_user = len(self.user)
        return render(request, self.template_name,
                      {'list': self.list, 'user':self.user, 'len_user':len_user})

class UserTrailDraft(UserTrailFormAdd):
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



