from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from shop.models import Product


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


""" Widoki sekcji Blog """

class BlogOwnerPostMixin(OwnerMixin, LoginRequiredMixin):
    """ Widok odpowiedzialny za wyświetlenie informacji o poście na stronie i przekierowanie moderatora po poprawnej
    edycji """
    model = Post
    fields = ['title', 'image', 'body', 'slug', 'status', 'owner']
    success_url = reverse_lazy('management:blog_manage_post_list')


class BlogOwnerPostEditMixin(BlogOwnerPostMixin, OwnerEditMixin):
    """ Widok odpowiedzialny za edycję posta"""
    fields = ['owner', 'title', 'slug', 'image', 'body', 'publish', 'status']
    success_url = reverse_lazy('management:blog_manage_post_list')
    template_name = 'blog/manage/posts/form.html'


class BlogManagePostListView(PermissionRequiredMixin, ListView):
    """ Widok wyświetlający wszystkie posty stworzone przez konkretnego użytkownika """
    model = Post
    permission_required = 'blog.add_post'
    template_name = 'blog/manage/posts/list.html'

class BlogEditPostListView(PermissionRequiredMixin, ListView):
    """ Widok odpowiedzialny za edytowanie postów w panelu administracyjnym """
    template_name = 'blog/manage/posts/edit-list.html'
    permission_required = 'blog.change_post'
    model = Post

    def get_queryset(self):
        qs = super(BlogEditPostListView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class BlogDeletePostListView(PermissionRequiredMixin, ListView):
    """ Widok odpowiedzialny za edytowanie postów w panelu administracyjnym """
    template_name = 'blog/manage/posts/delete-list.html'
    permission_required = 'blog.delete_post'
    model = Post

    def get_queryset(self):
        qs = super(BlogDeletePostListView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class BlogPostCreateView(PermissionRequiredMixin, BlogOwnerPostEditMixin, CreateView):
    """ Widok odpowiedzialny za dodawanie postów na stronie """
    permission_required = 'blog.add_post'


class BlogPostUpdateView(PermissionRequiredMixin, BlogOwnerPostEditMixin, UpdateView):
    """ Widok odpowiedzialny za aktualizacje postów na blogu """
    template_name = 'blog/manage/posts/form.html'
    permission_required = 'blog.change_post'


class BlogPostDeleteView(BlogOwnerPostMixin, DeleteView):
    """ Widok odpowiedzialny za usuwanie widoków na blogu """
    template_name = 'blog/manage/posts/delete.html'
    success_url = reverse_lazy('management:blog_manage_post_list')
    permission_required = 'blog.delete_post'


""" Widoki sekcji Shop """

class ShopManageProductsListView(PermissionRequiredMixin, ListView):
    """ Widok wyświetlający wszystkie posty stworzone przez konkretnego użytkownika """
    model = Product
    permission_required = 'shop.view_product'
    template_name = 'shop/manage/products/list.html'