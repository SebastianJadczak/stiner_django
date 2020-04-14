from django.views.generic.list import ListView
from .models import Post

class PostsListView(ListView):
    model = Post
    template_name = 'blog/list.html'

    def get_queryset(self):
        posts = super(PostsListView, self).get_queryset()
        return posts
