from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from map.models import Point

class Trails(TemplateView):
    template_name= 'trails/trails.html'


class PointsListView(ListView):
    template_name= 'points/points.html'
    list = Point.objects.all()

    def get(self, request, *args, **kwargs):
        template_name = 'points/points.html'
        query = request.GET.get('search')

        if query:
            self.list = self.list.filter(name=query)
            self.flaga = True
        return render(request, template_name,
                      {'list': self.list})

