from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerPostMixin(OwnerMixin, LoginRequiredMixin):
    model = Post
    fields = ['title', 'image', 'body', 'slug']
    success_url = reverse_lazy('blog:manage_post_list')

class OwnerPostEditMixin(OwnerPostMixin, OwnerEditMixin):
    fields =['title', 'image', 'body', 'slug']
    success_url = reverse_lazy('blog:manage_post_list')
    template_name = 'blog/manage/posts/form.html'

class ManagePostListView(PermissionRequiredMixin,ListView):
    """ Widok wyświetlający wszystkie posty stworzone przez konkretnego użytkownika """
    model = Post
    permission_required = 'blog.add_post'
    template_name = 'blog/manage/posts/list.html'

class PostCreateView(PermissionRequiredMixin ,OwnerPostEditMixin, CreateView):
   permission_required = 'blog.add_post'

class PostUpdateView(PermissionRequiredMixin ,OwnerPostEditMixin, UpdateView):
    template_name = 'blog/manage/posts/form.html'
    permission_required = 'blog.change_post'

class PostDeleteView(OwnerPostMixin, DeleteView):
    template_name = 'blog/manage/posts/delete.html'
    success_url = reverse_lazy('blog:manage_post_list')
    permission_required = 'blog.delete_post'


class PostsListView(ListView):
    """ Widok wyświetlający wszystkie posty na blogu """
    model = Post
    template_name = 'blog/list.html'

    def get_queryset(self):
        posts = super(PostsListView, self).get_queryset()
        return posts
