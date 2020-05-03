from django.urls import path, include

from . import views

app_name = 'trails'

urlpatterns = [
    path('', views.Trails.as_view(), name='basic_trails'),
]

