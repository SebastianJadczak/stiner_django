from django.urls import path, include
from map.views import map_json, PointViewsets
from rest_framework import routers
#
# urlpatterns = [
#     path('', map_json, name='map_json'),
# ]
router = routers.SimpleRouter()
router.register(r'points', PointViewsets)
urlpatterns = [

    path('api/', include(router.urls)),
]

