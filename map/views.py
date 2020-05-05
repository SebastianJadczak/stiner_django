from django.contrib.auth.models import Group
from django.core import serializers
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets
from map.api.serializers import PointSerializer
from map.models import Point


class Map(View):
    template_name= 'map/map_index.html'

    def get(self, request):
        return render(request, self.template_name,)

def map_render(request):
    points = Point.objects.all()
    return render(request,'map/map.html')


def map_json(request):
    data = [{
        "id": p.id,
        'descriptions':p.descriptions
     } for p in Point.objects.all()]
    return JsonResponse(data, safe=False)


class PointViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer