from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework import  generics

from map.models import Point, Opinion_about_Point
from trails.api.serializers import PointTrailsSerializer
from trails.models import Trail


class Trails(TemplateView):
    """ Widok podstawowy zakładki Trasy """
    template_name = 'trails/trails.html'


class PointsListView(ListView):
    """ Widok odpowiedzialny za listę punktów + wyszukiwarka """
    template_name = 'points/points.html'
    list = Point.objects.all()

    def get(self, request, *args, **kwargs):
        template_name = 'points/points.html'
        query_name = request.GET.get('search')
        query_location = request.GET.get('location_points')
        query_type = request.GET.get('point_type')
        if query_name or query_location or query_type:
            self.list = self.list.filter(name__contains=query_name, type=query_type, location__contains= query_location)
        return render(request, template_name,
                      {'list': self.list})



class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def get(self, request, *args, **kwargs):
        nick = request.GET.get('nick')
        star = request.GET.get('star')
        recension = request.GET.get('recension')
        object = list(Point.objects.filter(id=self.kwargs['pk']))
        opinion = list(Opinion_about_Point.objects.filter(point=self.kwargs['pk']))
        if nick and star and recension:
            Opinion_about_Point.objects.create(user=request.user,
                                               opinion=recension,
                                               rating=star,
                                               point=object[0])
        else:
            if nick== "":
                print('brak nicku')
            elif star== None:
                print('Brak gwiazdy')
            elif recension== "" :
                print('Brak recenzji')

        return render(request, self.template_name, {'object':object, 'opinion':opinion})


class TrailsListView(ListView):
    template_name = 'trails/all_trails/all_trails.html'
    model = Trail

    def get_queryset(self):
        trails = super(TrailsListView, self).get_queryset()

        return trails



class TrailDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Trail

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrailApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = PointTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Point.objects.filter(trails=pk)

