
from django.urls import path


from . import views


app_name = 'user_trails'



urlpatterns = [
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add'),
    path('add_point_to_trail/<int:element_id>/', views.AddPointToTrail, name='add_point_to_trail')
]

