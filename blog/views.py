from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin, View

from shop.models import Category
from .models import Post


class PostsListView(TemplateResponseMixin, View):
    """ Widok wyświetlający wszystkie posty na blogu. """
    model = Post
    template_name = 'blog/list.html'

    def get(self, request):
        category = Category.objects.all()
        post = Post.objects.all()
        return self.render_to_response({'category': category, 'posts': post})

class PostDetailView(DetailView):
    """ Widok wyświetlający konkretny post na stronie. """
    model = Post
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(id=self.kwargs['pk']).first()
        return render(request, self.template_name,{'post':post})