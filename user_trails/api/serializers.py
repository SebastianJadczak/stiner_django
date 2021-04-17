from rest_framework import serializers
from map.models import Point


class UserTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = "__all__"
