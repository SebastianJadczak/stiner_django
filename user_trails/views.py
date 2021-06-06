from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.loader import get_template
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from rest_framework import generics
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.urls import reverse

from map.models import Point, Coordinates
from trails.models import Trail
from trails.views import MethodTrail
from user_trails.models import UserTrail, UserPoint
from .api.serializers import UserTrailsSerializer
from .forms import UserTrailCreateForm


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
def trail_render_pdf_view(request, pk):
    template_path = 'trailsPDF.html'
    trail = UserTrail.objects.filter(id=pk).first()
    trail.downloads += 1
    trail.save()
    points = list(list(UserTrail.objects.filter(id=pk))[0].points.all())
    last_point = points[(len(points) - 1)]
    context = {'trail': trail, 'points': points, 'first_point': points[0], 'last_point': last_point}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="trail.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8', link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class UserTrailsListView(ListView, MethodTrail):
    """Klasa odpowiedzialna za wyświetlenie widoku Tras zwiedzania użytkowników"""
    template_name = 'trails/user_trails/user_trails.html'
    model = UserTrail

    def post(self, request, *args, **kwargs):
        search = self.search_trail(request, 'user_trail')

        return render(request, self.template_name,
                      {'search': search, 'city': self.get_city(), 'top_rate': self.get_top_rate_trails(),
                       'popular_trail': self.get_wached_trails(),
                       'type_trail': self.get_type_trail(), 'region_trail': self.get_region_trail(),
                       'country_trail': self.get_country_trail()})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_trails'] = UserTrail.objects.filter(user=self.request.user)
        context['user_trails_point'] = UserPoint.objects.all()
        context['city'] = self.get_city()
        context['top_rate'] = self.get_top_rate_trails()
        context['popular_trail'] = self.get_wached_trails()
        context['type_trail'] = self.get_type_trail()
        context['region_trail'] = self.get_region_trail()
        context['country_trail'] = self.get_country_trail()
        return context

class SearchUserTrails(UserTrailsListView):
    """Klasa odpowiedzialna za wyświetlenie wyników wyszukania tras użytkownika."""
    template_name = 'trails/user_trails/search_user_trails.html'
    model = UserTrail




class UserTrailFormAdd(ListView, MethodTrail):
    """Klasa odpowiedzialna za wyświetlenie obiektów które możesz dodasz do szkicu trasy"""
    template_name = 'trails/user_trails/form_trails.html'
    model = Point
    list = Point.objects.all()
    user_trail = []
    zmienna = ""

    def checkQueryinUserDraftTrail(self, query):
        for a in self.user_trail:
            for z in a:
                if query == str(z):
                    return False
    def get(self, request, *args, **kwargs):

        query = request.GET.get('add_point')
        if query:
            result = self.checkQueryinUserDraftTrail(query)
            if result == False:
                self.zmienna += "Nie możesz dodać tego zabytku. Istnieje już w bazie"
            else:
                self.user_trail.append(self.list.filter(name=query))
        len_user = len(self.user_trail)

        return render(request, self.template_name,
                      {'list': self.list, 'city': self.get_city(), 'type': self.get_type_trail(),
                       'region': self.get_region_trail(), 'country': self.get_country_trail(),
                       'user_trail': self.user_trail, 'len_user': len_user,
                       'zmienna': self.zmienna})

    def post(self, request):
        list_point = Point.objects.all()
        name = ''
        city = ''
        country = ''
        region = ''
        for key, value in request.POST.items():
            if 'name' in key and value != '':
                name = value

            if 'country' in key and value != '':
                country = value

            if 'region' in key and value != '':
                region = value

            if 'city' in key and value != '':
                city = value

        list_point = list_point.exclude(name__exact='', country__exact='', region__exact=region,
                                        location__exact=city).filter(
            name__contains=name, country__contains=country, region__contains=region, location__contains=city)
        return render(request, self.template_name, {'list_point': list_point, 'city': self.get_city(), 'type': self.get_type_trail(),
                       'region': self.get_region_trail(), 'country': self.get_country_trail(),
                       'user_trail': self.user_trail, 'search':'true',
                       'zmienna': self.zmienna})

class AddToTrail(UserTrailFormAdd):
    elements = Point.objects.all()
    def post(self, request):
        if request.POST:
            result = self.checkQueryinUserDraftTrail(request.POST.get('id'))
            if result == False:
                response = JsonResponse({"message": "Taki element już istnieje"})
                response.status_code = 403
                return response
            else:
                self.user_trail.append(self.list.filter(name=request.POST.get('id')))
                response = JsonResponse({"message": "Dodano element"})
                response.status_code = 200
                return response

class UserTrailDraft(UserTrailFormAdd):
    """Klasa odpowiedzialna za Szkic trasy zwiedzania"""
    template_name = 'trails/user_trails/draft/trail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get('delete')
        if query:
            for z in self.user_trail:
                for i in z:
                    if i.name == query:
                        self.user_trail.remove(z)
                        break

        return render(request, self.template_name, {'list': self.list, 'user_trail': self.user_trail, 'zmienna': self.zmienna, 'len_user_trail':len(self.user_trail)})


class DetailPoint(DetailView):
    template_name = 'trails/user_trails/detail.html'
    model = Point

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SaveDraftTrailUser(UserTrailFormAdd):
    """Klasa odpowiedzialna za formularz zapisu trasy użytkownika."""
    template_name = 'trails/user_trails/draft/save_draft_trail.html'

    def clear_board_user(self):
        del self.user_trail[:]

    def get(self, request):
        form = UserTrailCreateForm()
        return render(request, self.template_name, {'form': form, 'user_trail': self.user_trail})

    def set_region(self):
        table = [i[0].id for i in self.user_trail]
        points = []
        result = False
        for i in range(len(table)):
            points.append(Point.objects.filter(id=table[i]).first().region)
        if len(points) > 0:
            result = all(elem == points[0] for elem in points)
        if result == False:
            return 'Różne'
        else:
            return points[0]

    def check_image(self,request):
        try:
            print('image')
            return request.FILES['image']
        except:
            return staticfiles_storage.url('./grece.jpg')

    def set_country(self):
        table = [i[0].id for i in self.user_trail]
        points = []
        result = False
        for i in range(len(table)):
            points.append(Point.objects.filter(id=table[i]).first().country)
        if len(points) > 0:
            result = all(elem == points[0] for elem in points)
        if result == False:
            return 'Różne'
        else:
            return points[0]

    def set_city(self):
        table = [i[0].id for i in self.user_trail]
        points = []
        result = False
        for i in range(len(table)):
            points.append(Point.objects.filter(id=table[i]).first().location)
        if len(points) > 0:
            result = all(elem == points[0] for elem in points)
        if result == False:
            return 'Różne'
        else:
            return points[0]

    def post(self, request):
        form = UserTrailCreateForm(request.POST, request.FILES)
        if form.is_valid():
            table = [i[0].id for i in self.user_trail]
            if self.user_trail:
                userTrail = UserTrail()
                userTrail.user = request.user
                userTrail.name = request.POST.get('name')
                userTrail.descriptions = request.POST.get('descriptions')
                userTrail.city = self.set_city()
                userTrail.country = self.set_country()
                userTrail.image = self.check_image(request)
                userTrail.region = self.set_region()
                userTrail.downloads = 0
                userTrail.auditions = 0
                userTrail.save()
                userTrail.points.set(table)
            self.clear_board_user()
            # return render(request, 'trails/user_trails/user_trails.html', {'form': form, 'user_trail': self.user_trail})
            return redirect('yours_trails')
        else:
            print(form.errors)


class UserTrailDetail(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'trails/user_trails/user_trail_detail.html'
    model = UserTrail
    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        if len(top_rate_trails) >=10:
            top_rate_trails = top_rate_trails[0:10]
        return top_rate_trails

    def audioCount(request, pk):
        trail = get_object_or_404(UserTrail, id=pk)
        trail.auditions += 1
        trail.save()
        return HttpResponseRedirect(reverse('user_trails:user_trail_detail', args=[str(pk)]))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_trail'] = list(UserTrail.objects.filter(id=self.kwargs['pk']))[0]
        context['points'] = list(list(UserTrail.objects.filter(id=self.kwargs['pk']))[0].points.all())
        context['top_rate_trails'] = self.get_top_rate_trails()
        context['user_trail_id'] = self.kwargs['pk']
        return context

class TrailUserApiFilterListView(generics.ListAPIView):
    """ Widok odpowiedzialny za filtrowanie obiektów w zależności od trasy którą użytkownik wybierze :) """
    serializer_class = UserTrailsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return list(UserTrail.objects.filter(id=pk))[0].points.all()

