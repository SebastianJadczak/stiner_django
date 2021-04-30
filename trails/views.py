from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
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

    def search_point(self, request):
        search = ''
        location = ''
        type = ''

        for key, value in request.POST.items():
            if 'search' in key and value != '':
                search = value
            if 'location' in key and value != '':
                location = value
            if 'type' in key and value != '':
                type = value
        self.list = self.list.exclude(name__exact='', location__exact='', type__exact='').filter(
            name__contains=search, type__contains =type, location__contains=location)

    def post(self, request, *args, **kwargs):
        template_name = 'points/points.html'
        self.search_point(request)
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

    def getGallery(self, gallery):
        galleryArray = []

        for i in gallery:
            if i.image1 != '':
                galleryArray.append(i.image1)
            if i.image2 != '':
                galleryArray.append(i.image2)
            if i.image3 != '':
                galleryArray.append(i.image3)
            if i.image4 != '':
                galleryArray.append(i.image4)
            if i.image5 != '':
                galleryArray.append(i.image5)
        return galleryArray


    def get(self, request, *args, **kwargs):
        opinion = list(Opinion_about_Point.objects.filter(point=self.kwargs['pk']))
        point = Point.objects.filter(id=self.kwargs['pk'])
        point_id = self.kwargs['pk']
        gallery = point.first().gallery.all()
        gallery = self.getGallery(gallery)
        return render(request, self.template_name,
                      {'opinion': opinion, 'point': point[0], 'point_id': point_id, 'gallery': gallery})


class TrailsListView(ListView):
    template_name = 'trails/all_trails/all_trails.html'
    model = Trail
    list_trails = Trail.objects.all()

    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        return top_rate_trails

    def get_wached_trails(self):
        watched_trails = Trail.objects.order_by('watched').reverse()
        return watched_trails

    def get_city(self):
        city = list(Coordinates.objects.all())
        return city

    def get_type_trail(self):
        type_trail =[value for key, value in Trail.get_type_trail(Trail)]
        return type_trail

    def get_region_trail(self):
        region_trail = [value for key,value in Trail.get_region_trail(Trail)]
        return region_trail

    def get_country_trail(self):
        country_trail = [value for key,value in Trail.get_country_trail(Trail)]
        return country_trail

    def get_context_data(self, **kwargs):
        context = super(TrailsListView, self).get_context_data(**kwargs)
        context['city'] = self.get_city()
        context['top_rate'] = self.get_top_rate_trails()
        context['popular_trail'] = self.get_wached_trails()
        context['popular_trail_only_three'] = self.get_wached_trails()[:3]
        context['type_trail'] = self.get_type_trail()
        context['region_trail'] = self.get_region_trail()
        context['country_trail'] = self.get_country_trail()
        return context

    def get_queryset(self):
        trails = super(TrailsListView, self).get_queryset()
        return trails

    def search_trail(self, request):
        name = ''
        country = ''
        region = ''
        city = ''
        type_trail = ''
        star = (int(0), (float(5) + 0.9))
        popular = False
        for key, value in request.POST.items():
            if 'name' in key and value != '':
                name = value
            if 'country' in key and value != '':
                country = value
            if 'region' in key and value != '':
                region = value
            if 'city' in key and value != '':
                city = value
            if 'type_trail' in key and value != '':
                type_trail = value
            if 'star' in key and value != '':
                star = (int(value), (float(value) + 0.9))
            if 'popular' in key and value != False:
                popular = value

        self.list_search = self.list_trails.exclude(name__exact='', country__exact='', region__exact='', city__exact='',
                                                    type__exact='').filter(
            name__contains=name, country__contains=country,
            region__contains=region, city__contains=city,
            type__contains=type_trail, average_grade__range=star,
            popular=popular)
        if (len(self.list_search) == 0): self.list_search = 'Brak wyników wyszukiwania'
        return self.list_search

    def post(self, request, *args, **kwargs):
        search = self.search_trail(request)

        return render(request, self.template_name,
                      {'search': search, 'city': self.get_city(), 'top_rate': self.get_top_rate_trails(),
                       'popular_trail': self.get_wached_trails(),
                       'popular_trail_only_three': self.get_wached_trails()[:3],
                       'type_trail': self.get_type_trail(), 'region_trail': self.get_region_trail(),
                       'country_trail': self.get_country_trail()})


class TrailDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'trails/all_trails/trail/trail_detail.html'
    model = Trail



    def calculation_mean(self, trail_name):
        rate_trail = list(Rate_trail.objects.filter(trail=trail_name))
        average_grade = 0
        for element in rate_trail:
            average_grade = average_grade + element.rate
        average_grade = average_grade / len(rate_trail)
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
        context['points'] =list(list(Trail.objects.filter(id=self.kwargs['pk']))[0].points.all())
        return context


class TrailApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = PointTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return list(Trail.objects.filter(id=pk))[0].points.all()
