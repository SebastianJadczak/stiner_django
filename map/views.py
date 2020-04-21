from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views import View


class Map(View):
    template_name= 'map/map.html'

    def get(self, request):
        return render(request, self.template_name,)