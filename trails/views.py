from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View, TemplateResponseMixin
from rest_framework import viewsets, generics

from map.models import Point
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

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

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

