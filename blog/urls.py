from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsListView.as_view(), name='list_posts'),
    path('manage/',views.ManagePostListView.as_view() , name='manage_post_list'),
    path('create/',views.PostCreateView.as_view() , name='post_create'),
    path('<pk>/edit/',views.PostUpdateView.as_view() , name='post_edit'),
    path('<pk>/delete/',views.PostDeleteView.as_view() , name='post_delete'),
]

