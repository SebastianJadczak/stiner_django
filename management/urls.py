from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from management import views

app_name = 'management'

urlpatterns = [
    path('blog_manage/',views.BlogManagePostListView.as_view() , name='blog_manage_post_list'),
    path('blog_create/',views.BlogPostCreateView.as_view() , name='blog_post_create'),
    path('blog/<pk>/edit/',views.BlogPostUpdateView.as_view() , name='blog_post_edit'),
    path('blog/<pk>/delete/',views.BlogPostDeleteView.as_view() , name='blog_post_delete'),
    path('blog_edit/', views.BlogEditPostListView.as_view(), name='blog_posts_edit'),
    path('blog_delete/', views.BlogDeletePostListView.as_view(), name='blog_posts_delete'),
    # Shop
    path('shop_manage', views.ShopManageProductsListView.as_view(), name='shop_manage_product_list'),
    path('product_create/',views.ShopProductstCreateView.as_view() , name='shop_product_create'),
    path('product/<pk>/edit/',views.ShopProductsUpdateView.as_view() , name='shop_product_edit'),
    path('product/<pk>/delete/',views.ShopProductDeleteView.as_view() , name='shop_product_delete'),
    path('product_edit/', views.ShopManageEditListView.as_view(), name='shop_products_edit'),
    path('product_delete/', views.ShopDeleteProductsListView.as_view(), name='shop_products_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
