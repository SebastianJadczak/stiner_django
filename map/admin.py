from django.contrib import admin
from .models import Point, Opinion_about_Point, Coordinates

admin.site.register(Point)
admin.site.register(Opinion_about_Point)
admin.site.register(Coordinates)
