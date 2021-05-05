from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsListView.as_view(), name='list_posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail')
]
