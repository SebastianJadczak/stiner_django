from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets, request
from rest_framework.response import Response

from account.models import UserRole
from map.api.serializers import PointSerializer, LocationMapSerializer
from map.forms import FormularzRejestracji
from map.models import Point, Coordinates, NewsletterEmail
from shop.models import Category


class Map(View):
    template_name = 'map/map_index.html'
    category = Category.objects.all()
    coordinates = Coordinates.objects.all()
    userRole = ''
    def get(self, request):
        # ---------------------------------------
        # Pobiera dane o roli użytkownika
        if (str(request.user) != 'AnonymousUser'):
            self.userRole = UserRole.objects.filter(user=request.user).first()
        # ---------------------------------------
        return render(request, self.template_name, {'userRole':self.userRole,'category': self.category, 'coordinates':self.coordinates})

    def post(self, request):
        if(len(NewsletterEmail.objects.filter(email=request.POST.get('email'))) ==0):
            NewsletterEmail.objects.create(email=request.POST.get('email'))
        else:
            return render(request, self.template_name, )
        return render(request, self.template_name,)


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
