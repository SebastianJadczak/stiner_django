from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
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
        return render(request, template_name,
                      {'list': self.list})



class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
