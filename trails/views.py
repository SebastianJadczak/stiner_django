from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework import generics

from map.models import Point, Opinion_about_Point, Coordinates
from shop.models import Category
from trails.api.serializers import PointTrailsSerializer
from trails.models import Trail, Rate_trail
from user_trails.models import UserTrail
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.urls import reverse


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static
        mUrl = settings.MEDIA_URL  # Typically /media
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

def point_render_pdf_view(request, pk):
    template_path = 'pdf1.html'
    point = Point.objects.filter(id=pk).first()
    context = {'point': point}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="point.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    point = get_object_or_404(Point, id=pk)
    point.downloads.add(request.user)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def trail_render_pdf_view(request, pk):
    template_path = 'trailsPDF.html'
    trail = Trail.objects.filter(id=pk).first()
    trail.downloads += 1
    trail.save()
    points = list(list(Trail.objects.filter(id=pk))[0].points.all())
    last_point =points[(len(points) - 1)]
    context = {'trail': trail, 'points':points, 'first_point':points[0],'last_point': last_point}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="trail.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8', link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



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
                      {'list': self.list,'city':Coordinates.objects.all(), 'type':Point.TYPE_POINT})

    def get_context_data(self, **kwargs):
        context = super(PointsListView, self).get_context_data(**kwargs)
        context['city'] = Coordinates.objects.all()
        context['type'] = Point.TYPE_POINT
        context['list'] = Point.objects.all()
        return context


class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def calculation_mean(self, point_id):
        rate_point = list(Opinion_about_Point.objects.filter(point=Point.objects.get(id=point_id)))
        average_grade = 0
        for element in rate_point:
            average_grade = average_grade + element.rating
        average_grade = average_grade / len(rate_point)
        point = Point.objects.get(id=point_id)
        point.average_grade = average_grade
        point.save()

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
            self.calculation_mean(point_id)
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

    def get_top_rate_point(self):
        top_rate_trails = Point.objects.order_by('average_grade').reverse()
        if len(top_rate_trails) >= 10:
            top_rate_trails = top_rate_trails[0:10]
        return top_rate_trails

    def get(self, request, *args, **kwargs):
        opinion = list(Opinion_about_Point.objects.filter(point=self.kwargs['pk']))
        point = Point.objects.filter(id=self.kwargs['pk'])
        point_id = self.kwargs['pk']
        gallery = point.first().gallery.all()
        gallery = self.getGallery(gallery)
        stuff = get_object_or_404(Point, id=self.kwargs['pk'])
        point_liked = False
        if stuff.heart.filter(id=self.request.user.id).exists():
            point_liked = True
        point_dones = False
        if stuff.done.filter(id=self.request.user.id).exists():
            point_dones = True
        return render(request, self.template_name,
                      {'opinion': opinion, 'point': point[0], 'point_id': point_id, 'gallery': gallery, 'point_liked': point_liked,
                       'point_dones': point_dones, 'top_rate_point': self.get_top_rate_point()})

    def point_heart(request, pk):
        point = get_object_or_404(Point, id=request.POST.get('heart_id'))
        if point.heart.filter(id=request.user.id).exists():
            point.heart.remove(request.user)
        else:
            point.heart.add(request.user)

        return HttpResponseRedirect(reverse('trails:point_detail', args=[str(pk)]))

    def point_done(request, pk):
        point = get_object_or_404(Point, id=request.POST.get('point_done'))
        if point.done.filter(id=request.user.id).exists():
            point.done.remove(request.user)
            point.done_count -= 1
            point.save()
        else:
            point.done.add(request.user)
            point.done_count += 1
            point.save()
        return HttpResponseRedirect(reverse('trails:point_detail', args=[str(pk)]))

class MethodTrail():
    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        return top_rate_trails

    def get_wached_trails(self):
        watched_trails = Trail.objects.order_by('done').reverse()
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

    def search_trail(self, request, type):
        name = ''
        country = ''
        region = ''
        city = ''
        type_trail = ''
        star = (int(0), (float(5) + 0.9))
        popular = False
        self.list_trails =[]
        if(type == 'all_trail'):
            self.list_trails = Trail.objects.all()
        elif(type=='user_trail'):
            self.list_trails = UserTrail.objects.all()

        for key, value in request.POST.items():
            if 'name' in key and value != '':
                name = value
            if 'country' in key and value != '':
                country = value
            if 'region' in key and value != '':
                region = value
            if 'city' in key and value != '':
                city = value
            if 'type' in key and value != '':
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

class TrailsListView(ListView, MethodTrail):
    template_name = 'trails/all_trails/all_trails.html'
    model = Trail

    def get_context_data(self, **kwargs):
        context = super(TrailsListView, self).get_context_data(**kwargs)
        context['city'] = self.get_city()
        context['top_rate'] = self.get_top_rate_trails()
        context['popular_trail'] = self.get_wached_trails()
        context['type_trail'] = self.get_type_trail()
        context['region_trail'] = self.get_region_trail()
        context['country_trail'] = self.get_country_trail()
        return context

    def get_queryset(self):
        trails = super(TrailsListView, self).get_queryset()
        return trails



    def post(self, request, *args, **kwargs):
        search = self.search_trail(request,'all_trail')

        return render(request, self.template_name,
                      {'search': search, 'city': self.get_city(), 'top_rate': self.get_top_rate_trails(),
                       'popular_trail': self.get_wached_trails(),
                       'type_trail': self.get_type_trail(), 'region_trail': self.get_region_trail(),
                       'country_trail': self.get_country_trail()})


class TrailDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'trails/all_trails/trail/trail_detail.html'
    model = Trail

    def audioCount(request, pk):
        trail = get_object_or_404(Trail, id=pk)
        trail.auditions += 1
        trail.save()
        return HttpResponseRedirect(reverse('trails:trail_detail', args=[str(pk)]))

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

    def trail_done(request, pk):
        trail = get_object_or_404(Trail, id=request.POST.get('done_trail'))
        if trail.done.filter(id=request.user.id).exists():
            trail.done.remove(request.user)
            trail.done_count -= 1
            trail.save()
        else:
            trail.done.add(request.user)
            trail.done_count += 1
            trail.save()
        return HttpResponseRedirect(reverse('trails:trail_detail', args=[str(pk)]))

    def trail_heart(request, pk):
        trail = get_object_or_404(Trail, id=request.POST.get('heart_trail'))
        if trail.heart.filter(id=request.user.id).exists():
            trail.heart.remove(request.user)
        else:
            trail.heart.add(request.user)
        return HttpResponseRedirect(reverse('trails:trail_detail', args=[str(pk)]))

    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        if len(top_rate_trails) >=10:
            top_rate_trails = top_rate_trails[0:10]
        return top_rate_trails

    def get_context_data(self, *args, **kwargs):
        stuff = get_object_or_404(Trail, id=self.kwargs['pk'])
        trail_dones = False
        if stuff.done.filter(id=self.request.user.id).exists():
            trail_dones = True
        trail_liked = False
        if stuff.heart.filter(id=self.request.user.id).exists():
            trail_liked = True
        context = super().get_context_data(**kwargs)
        context['trail_liked'] = trail_liked
        context['trail_dones'] = trail_dones
        context['trail'] = list(Trail.objects.filter(id=self.kwargs['pk']))[0]
        context['trail_id'] = self.kwargs['pk']
        context['points'] =list(list(Trail.objects.filter(id=self.kwargs['pk']))[0].points.all())
        context['opinion_trail'] = list(list(Rate_trail.objects.filter(trail=self.kwargs['pk'])))
        context['top_rate_trails'] = self.get_top_rate_trails()
        return context


class TrailApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = PointTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return list(Trail.objects.filter(id=pk))[0].points.all()
