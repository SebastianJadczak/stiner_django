from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin, View

from map.models import Point, AdvertisementNews
from shop.models import Category
from .models import Post


class PostsListView(TemplateResponseMixin, View):
    """ Widok wyświetlający wszystkie posty na blogu. """
    model = Post
    template_name = 'blog/list.html'

    def get_top_rate_points(self):
        top_rate_trails = Point.objects.order_by('average_grade').reverse()
        if len(top_rate_trails) >=10:
            top_rate_trails = top_rate_trails[0:10]
        return top_rate_trails

    def get(self, request):
        category = Category.objects.all()
        post = Post.objects.all()
        return self.render_to_response({'category': category, 'posts': post,'top_rate_points': self.get_top_rate_points()})

class PostDetailView(DetailView):
    """ Widok wyświetlający konkretny post na stronie. """
    model = Post
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(id=self.kwargs['pk']).first()
        ad = AdvertisementNews.objects.filter(active=True)
        return render(request, self.template_name,{'post':post, 'ads':ad})