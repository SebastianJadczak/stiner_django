from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsListView.as_view(), name='list_posts')
]
