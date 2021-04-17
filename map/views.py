from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets, request
from rest_framework.response import Response

from map.api.serializers import PointSerializer, LocationMapSerializer
from map.forms import FormularzRejestracji
from map.models import Point, Coordinates
from shop.models import Category


class Map(View):
    template_name = 'map/map_index.html'
    category = Category.objects.all()
    coordinates = Coordinates.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'category': self.category, 'coordinates': self.coordinates})


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
