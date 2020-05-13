from django.urls import path, include

from . import views

app_name = 'trails'

urlpatterns = [
    path('', views.Trails.as_view(), name='basic_trails'),
    path('points/', views.PointsListView.as_view(), name='points'),
    path('point/<int:pk>/', views.PointDetailView.as_view(), name='point_detail'),
    path('all_trails', views.TrailsListView.as_view(), name='all_trails'),
    path('user_trails', views.UserTrailsListView.as_view(), name='user_trails'),
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add')
]

