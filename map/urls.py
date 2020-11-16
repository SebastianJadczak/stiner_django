from django.urls import path, include

from map import views
from map.views import PointViewsets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'points', PointViewsets)
urlpatterns = [

    path('api/', include(router.urls)),
    # path('monuments', views.Monuments.as_view(), name='monuments'),

]

