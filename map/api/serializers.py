from rest_framework import serializers
from ..models import Point, Coordinates


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = "__all__"


class LocationMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"
