
from django.urls import path


from . import views


app_name = 'user_trails'



urlpatterns = [
    path('user_trails_add', views.UserTrailFormAdd.as_view(), name='user_trail_add'),
]

