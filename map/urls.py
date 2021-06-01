from django.urls import path, include

from map import views
from map.views import PointViewsets, MapCenterViewsets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'points', PointViewsets)
router.register(r'mapCenter', MapCenterViewsets)
urlpatterns = [

    path('api/', include(router.urls)),
    path('sort/', views.DoneList, name='sort'),
    path('news/<int:pk>/', views.NewsDetail.as_view(), name='news'),
    path('regulations/', views.Regulations.as_view(), name='regulations')
]

