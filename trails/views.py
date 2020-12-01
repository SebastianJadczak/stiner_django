import json

from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from numpy import sort
from rest_framework import generics

from map.models import Point, Opinion_about_Point, Coordinates
from shop.models import Category
from trails.api.serializers import PointTrailsSerializer
from trails.models import Trail, Rate_trail


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
    model = Point
    list = Point.objects.all()

    def search_point(self, name=None, type=None, location=None):
        if name and location and type:
            self.list = self.list.filter(name__contains=name, type=type, location__contains=location)
        if name and location :
            self.list = self.list.filter(name__contains=name, location__contains=location)
        if name and type:
            self.list = self.list.filter(name__contains=name, type=type)
        if location and type:
            self.list = self.list.filter( type=type, location__contains=location)
        if name:
            self.list = self.list.filter(name__contains=name)
        if location:
                self.list = self.list.filter(location__contains=location)
        if type:
            self.list = self.list.filter(type=type)

    def post(self, request, *args, **kwargs):
        template_name = 'points/points.html'
        query_name = request.POST.get('search')
        query_location = request.POST.get('location_points')
        query_type = request.POST.get('point_type')
        self.search_point(query_name, query_type, query_location)
        return render(request, template_name,
                      {'list': self.list})

    def get_context_data(self, **kwargs):
        context = super(PointsListView, self).get_context_data(**kwargs)
        context['list'] = Point.objects.all()
        return context

class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def post(self, request, *args, **kwargs):
        nick = request.user
        star = request.POST.get('star')
        point_id = request.POST.get('point_id')
        recension = request.POST.get('recension')
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
        point = Point.objects.filter(id=self.kwargs['pk'])
        point_id = self.kwargs['pk']

        return render(request, self.template_name, {'opinion': opinion, 'point':point[0], 'point_id': point_id})


class TrailsListView(ListView):
    template_name = 'trails/all_trails/all_trails.html'
    model = Trail

    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        return top_rate_trails

    def get_wached_trails(self):
        watched_trails = Trail.objects.order_by('watched').reverse()
        return watched_trails

    def get_city(self):
        city=list(Coordinates.objects.all())
        return city

    def get_context_data(self, **kwargs):
        context = super(TrailsListView, self).get_context_data(**kwargs)
        context['city'] = self.get_city()
        context['top_rate'] = self.get_top_rate_trails()
        context['popular_trail'] = self.get_wached_trails()
        return context

    def get_queryset(self):
        trails = super(TrailsListView, self).get_queryset()
        return trails

    def post(self, request, *args, **kwargs):
        list_trails = []
        for key, value in request.POST.items():
            if 'name' in key:
                pass
            if 'city' in key:
                pass
            if 'star' in key:
                list_trails.append(Trail.objects.filter(average_grade__gte=int(value), average_grade__lte=(int(value)+1)))

        return render(request, 'map/map_index.html',
                      {'list': list_trails})

class TrailDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'trails/all_trails/trail/trail_detail.html'
    model = Trail


    def calculation_mean(self, trail_name):
        rate_trail = list(Rate_trail.objects.filter(trail=trail_name))
        average_grade = 0
        for element in rate_trail:
            average_grade= average_grade+ element.rate
        average_grade = average_grade/len(rate_trail)
        trail = Trail.objects.get(id=trail_name)
        trail.average_grade = average_grade
        trail.save()

    def post(self, request, *args, **kwargs):
        nick = request.user
        star = request.POST.get('star')
        trail_id = request.POST.get('trail_id')
        recension = request.POST.get('recension')
        if nick and star and recension:
            Rate_trail.objects.create(user=nick,
                                               opinion=recension,
                                               rate=star,
                                               trail=Trail.objects.get(id=trail_id))
            self.calculation_mean(trail_id)
        else:
            if nick == "":
                print('brak nicku')
            elif star == None:
                print('Brak gwiazdy')
            elif recension == "":
                print('Brak recenzji')
        return redirect('../../trail_detail/' + trail_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trail'] = list(Trail.objects.filter(id=self.kwargs['pk']))[0]
        context['trail_id'] = self.kwargs['pk']
        return context


class TrailApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = PointTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Point.objects.filter(trails=pk)
