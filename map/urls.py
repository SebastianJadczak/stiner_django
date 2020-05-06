from django.urls import path, include
from map.views import PointViewsets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'points', PointViewsets)
urlpatterns = [

    path('api/', include(router.urls)),

]

