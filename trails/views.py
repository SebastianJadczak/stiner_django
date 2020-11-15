from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework import generics

from map.models import Point, Opinion_about_Point
from shop.models import Category
from trails.api.serializers import PointTrailsSerializer
from trails.models import Trail


class Trails(TemplateView):
    """ Widok podstawowy zakładki Trasy """
    template_name = 'trails/trails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


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
            self.list = self.list.filter(name__contains=query_name, type=query_type, location__contains=query_location)
        return render(request, template_name,
                      {'list': self.list})


class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def post(self, request, *args, **kwargs):
        nick = request.POST.get('nick')
        star = request.POST.get('star')
        point_id = request.POST.get('point_id')
        recension = request.POST.get('recension')
        opinion = list(Opinion_about_Point.objects.filter(point=self.kwargs['pk']))
        if nick and star and recension:
            Opinion_about_Point.objects.create(user=nick,
                                               opinion=recension,
                                               rating=star,
                                               point=Point.objects.get(id=point_id))
        else:
            if nick == "":
                print('brak nicku')
            elif star == None:
                print('Brak gwiazdy')
            elif recension == "":
                print('Brak recenzji')
        return redirect('../../point/' + point_id)

    def get(self, request, *args, **kwargs):
        opinion = list(Opinion_about_Point.objects.filter(point=self.kwargs['pk']))
        point_id = self.kwargs['pk']
        return render(request, self.template_name, {'opinion': opinion, 'point_id': point_id})


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrailApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = PointTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Point.objects.filter(trails=pk)
