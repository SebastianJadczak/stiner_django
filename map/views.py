from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets, request
from rest_framework.response import Response

# from account.models import UserRole
from account.models import UserRole
from map.api.serializers import PointSerializer, LocationMapSerializer
from map.forms import FormularzRejestracji
from map.models import Point, Coordinates, NewsletterEmail, News, AdvertisementNews, Country
from shop.models import Category
from trails.models import Trail
from trails.views import MethodTrail
from user_trails.models import UserTrail


class Map(View, MethodTrail):
    template_name = 'map/map_index.html'
    category = Category.objects.all()
    coordinates = Coordinates.objects.all()
    points = Point.objects.all()
    trails = Trail.objects.all()
    news = News.objects.all()
    country = Country.objects.all()

    def get(self, request):
        # ---------------------------------------
        # if (str(request.user) != 'AnonymousUser'):
        #     self.userRole = UserRole.objects.filter(user=request.user).first()
        # ---------------------------------------
        return render(request, self.template_name, {'category': self.category, 'coordinates': self.coordinates,
                                                    'coordinatesLength': len(self.coordinates), 'news': self.news[:3],
                                                    'newsBig': self.news[3:5], 'pointLength': len(self.points),
                                                    'trailLength': len(self.trails), 'countryLength': len(self.country),
                                                    'country': self.country})

    def add_to_Newsletter(self, request):
        if (len(NewsletterEmail.objects.filter(email=request.POST.get('email'))) == 0):
            NewsletterEmail.objects.create(email=request.POST.get('email'))

    def post(self, request, *args, **kwargs):
        """Obsługa formularzy na stronie głównej."""
        if request.POST.get('email'):
            self.add_to_Newsletter(request)
            return render(request, self.template_name, )
        else:
            search = self.search_trail(request, 'all_trail')
            return render(request, 'trails/all_trails/all_trails.html',
                          {'search': search, 'city': self.get_city(), 'top_rate': self.get_top_rate_trails(),
                           'popular_trail': self.get_wached_trails(),
                           'type_trail': self.get_type_trail(), 'region_trail': self.get_region_trail(),
                           'country_trail': self.get_country_trail()})


class PointViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        points = Point.objects.filter(type=params['pk'])
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)


class MapCenterViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = LocationMapSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        location = Coordinates.objects.filter(name=params['pk'])
        serializer = LocationMapSerializer(location, many=True)
        return Response(serializer.data)


class UserFormView(View):
    """Rejestracja użytkownika"""
    form_class = FormularzRejestracji
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('../')

        return render(request, self.template_name, {'form': form})


class MapFullScreen(View):
    template_name = 'map/map.html'
    coordinates = Coordinates.objects.all()
    country = Country.objects.all()


    def get(self, request):
        # --------------------------------------
        # if (str(request.user) != 'AnonymousUser'):
        #     self.userRole = UserRole.objects.filter(user=request.user).first()
        # --------------------------------------
        return render(request, self.template_name,
                      {'coordinates': self.coordinates, 'countryLength': len(self.country), 'country': self.country})


class FavoriteList(ListView):
    template_name = 'favorite/favorite.html'
    model = Trail
    coordinates = Coordinates.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def post(self, request):
        search = self.request.POST.get('search')
        print(search)
        self.favorite_trail = Trail.objects.exclude(name__exact='').filter(heart=self.request.user, name__contains=search)
        self.favorite_point = Point.objects.exclude(name__exact='').filter(heart=self.request.user, name__contains=search)
        return render(request, self.template_name,
                      {'trail_favorite': self.favorite_trail, 'point_favorite': self.favorite_point, 'country': self.country,
                       'city': self.coordinates})

    def get_context_data(self, **kwargs):
        self.favorite_trail = Trail.objects.filter(heart=self.request.user)
        self.favorite_point = Point.objects.filter(heart=self.request.user)
        sorting = self.request.GET.get('sorting',
                                       "")  # http//..../done/?sorting=rate ---  geting rate or done and adding to url
        filtercity = self.request.GET.get('filtercity', "")
        filtercountry = self.request.GET.get('filtercountry', "")

        if (filtercity != '' or filtercountry != "" or sorting == "rate" or sorting == "done"):
            self.favorite_point = self.favorite_point.exclude(location__exact='', country__exact='').filter(
                location__contains=filtercity,
                country__contains=filtercountry)
            self.favorite_trail = self.favorite_trail.exclude(city__exact='', country__exact='').filter(city__contains=filtercity,
                                                                                                        country__contains=filtercountry)
            if sorting == "rate":
                self.favorite_point = self.favorite_point.order_by('-average_grade')
                self.favorite_trail = self.favorite_trail.order_by('-average_grade')
            elif sorting == "done":
                self.favorite_point = self.favorite_point.order_by('-done_count')
                self.favorite_trail = self.favorite_trail.order_by('-done_count')
                pass

        context = super().get_context_data(**kwargs)
        context['trail_favorite'] = self.favorite_trail
        context['point_favorite'] = self.favorite_point
        context['country'] = self.country
        context['city'] = self.coordinates
        return context


class FavoritePoint(ListView):
    template_name = 'favorite/favorite_point.html'
    model = Point

    coordinates = Coordinates.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def post(self, request):
        search = self.request.POST.get('search')
        self.favorite_points = Point.objects.exclude(name__exact='').filter(heart=self.request.user,
                                                                            name__contains=search)
        return render(request, self.template_name,
                      {'point_favorite': self.favorite_points, 'country': self.country,
                       'city': self.coordinates})

    def get_context_data(self, **kwargs):
        self.favorite_point = Point.objects.filter(heart=self.request.user)
        sorting = self.request.GET.get('sorting',
                                       "")  # http//..../done/?sorting=rate ---  geting rate or done and adding to url
        filtercity = self.request.GET.get('filtercity', "")
        filtercountry = self.request.GET.get('filtercountry', "")

        if (filtercity != '' or filtercountry != "" or sorting == "rate" or sorting == "done"):
            self.favorite_point = self.favorite_point.exclude(location__exact='', country__exact='').filter(
                location__contains=filtercity,
                country__contains=filtercountry)
            if sorting == "rate":
                self.favorite_point = self.favorite_point.order_by('-average_grade')
            elif sorting == "done":
                self.favorite_point = self.favorite_point.order_by('-done_count')
                pass

        context = super().get_context_data(**kwargs)
        context['point_favorite'] = self.favorite_point
        context['country'] = self.country
        context['city'] = self.coordinates
        return context


class FavoriteTrail(ListView):
    template_name = 'favorite/favorite_trail.html'
    model = Trail
    coordinates = Coordinates.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def post(self, request):
        search = self.request.POST.get('search')
        self.favorite_trail = Trail.objects.exclude(name__exact='').filter(heart=self.request.user,
                                                                           name__contains=search)
        return render(request, self.template_name,
                      {'trail_favorite': self.favorite_trail, 'country': self.country,
                       'city': self.coordinates})

    def get_context_data(self, **kwargs):
        self.favorite_trail = Trail.objects.filter(heart=self.request.user)
        sorting = self.request.GET.get('sorting',"")  # http//..../done/?sorting=rate ---  geting rate or done and adding to url
        filtercity = self.request.GET.get('filtercity', "")
        filtercountry = self.request.GET.get('filtercountry', "")

        if (filtercity != '' or filtercountry != "" or sorting == "rate" or sorting == "done"):
            print(self.favorite_trail)
            self.favorite_trail = self.favorite_trail.exclude(city__exact='', country__exact='').filter(city__contains=filtercity,
                                                                                                country__contains=filtercountry)
            print(self.favorite_trail)
            if sorting == "rate":
                print(self.favorite_trail)
                self.favorite_trail = self.favorite_trail.order_by('-average_grade')
            elif sorting == "done":
                self.favorite_trail = self.favorite_trail.order_by('-done_count')

        context = super().get_context_data(**kwargs)
        context['trail_favorite'] = self.favorite_trail
        context['country'] = self.country
        context['city'] = self.coordinates
        return context


class FavoriteYourTrail(ListView):
    template_name = 'favorite/favorite_your_trail.html'
    model = UserTrail

    def get_context_data(self, **kwargs):
        self.favorite_trail = UserTrail.objects.filter(heart=self.request.user)
        context = super().get_context_data(**kwargs)
        context['trail_favorite'] = self.favorite_trail
        return context


class DoneList(ListView):
    template_name = 'done/done.html'
    model = Trail
    done_trail = []
    done_point = []
    coordinates = Coordinates.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def post(self, request):
        search = self.request.POST.get('search')
        self.done_trail = Trail.objects.exclude(name__exact='').filter(done=self.request.user, name__contains=search)
        self.done_point = Point.objects.exclude(name__exact='').filter(done=self.request.user,  name__contains=search)
        return render(request, self.template_name, {'trail_done':self.done_trail, 'point_done':self.done_point,'country': self.country,'city' : self.coordinates})

    def get_context_data(self, **kwargs):
        self.done_trail = Trail.objects.filter(done=self.request.user)
        self.done_point = Point.objects.filter(done=self.request.user)
        sorting = self.request.GET.get('sorting', "") #http//..../done/?sorting=rate ---  geting rate or done and adding to url
        filtercity = self.request.GET.get('filtercity', "")
        filtercountry = self.request.GET.get('filtercountry', "")

        if(filtercity != '' or  filtercountry != "" or sorting == "rate" or sorting == "done"):
            self.done_point = self.done_point.exclude(location__exact='', country__exact='').filter(location__contains=filtercity,
                                                                                                    country__contains=filtercountry)
            self.done_trail = self.done_trail.exclude(city__exact='', country__exact='').filter(city__contains=filtercity,country__contains=filtercountry)
            if sorting == "rate":
                self.done_point = self.done_point.order_by('-average_grade')
                self.done_trail = self.done_trail.order_by('-average_grade')
            elif sorting == "done":
                self.done_point = self.done_point.order_by('-done_count')
                self.done_trail = self.done_trail.order_by('-done_count')

        context = super().get_context_data(**kwargs)
        context['trail_done'] = self.done_trail
        context['point_done'] = self.done_point
        context['country'] = self.country
        context['city'] = self.coordinates
        return context


class NewsDetail(DetailView):
    template_name = 'news/news.html'
    model = News

    def get_top_rate_trails(self):
        top_rate_trails = Trail.objects.order_by('average_grade').reverse()
        if len(top_rate_trails) >=10:
            top_rate_trails = top_rate_trails[0:10]
        return top_rate_trails

    def get_top_rate_points(self):
        top_rate_points = Point.objects.order_by('-average_grade')[0:4]
        return top_rate_points

    def get(self, request, *args, **kwargs):
        news = News.objects.filter(id=self.kwargs['pk']).first()
        ad = AdvertisementNews.objects.filter(active=True).first()
        return render(request, self.template_name, {'news': news, 'top_rate_trails': self.get_top_rate_trails(),
                                                    'top_rate_points':self.get_top_rate_points(), 'ad': ad})

class Regulations(TemplateView):
    template_name = 'regulations/regulations.html'
