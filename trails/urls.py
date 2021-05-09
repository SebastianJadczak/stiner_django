
from django.urls import path


from . import views


app_name = 'trails'



urlpatterns = [
    path('', views.Trails.as_view(), name='basic_trails'),
    path('points/', views.PointsListView.as_view(), name='points'),
    path('point/<int:pk>/', views.PointDetailView.as_view(), name='point_detail'),
    path('all_trails', views.TrailsListView.as_view(), name='all_trails'),
    path('trail_detail/<int:pk>/', views.TrailDetailView.as_view(), name='trail_detail'),
    path('api/<int:pk>', views.TrailApiFilterListView.as_view()),
    path('pdf_point/',views.render_pdf_view, name='pdf_point')
]

