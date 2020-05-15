from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import TrailApiFilterListView

app_name = 'trails'

# router = routers.SimpleRouter()
# router.register(r'points', TrailApiFilterListView)



urlpatterns = [
    path('', views.Trails.as_view(), name='basic_trails'),
    path('points/', views.PointsListView.as_view(), name='points'),
    path('point/<int:pk>/', views.PointDetailView.as_view(), name='point_detail'),
    path('all_trails', views.TrailsListView.as_view(), name='all_trails'),
    path('user_trails', views.UserTrailsListView.as_view(), name='user_trails'),
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add'),
    path('trail_detail/<int:pk>/', views.TrailDetailView.as_view(), name='trail_detail'),
    # path('api/', include(router.urls)),
    path('api/<int:pk>', views.TrailApiFilterListView.as_view()),
]

