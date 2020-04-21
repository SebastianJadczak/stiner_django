from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from map.views import Map
from django.conf import settings
from django.conf.urls.static import static

from shop.views import ProductContentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Map.as_view(), name='map'),
    path('blog/', include('blog.urls'), name='blog'),
    path('shop/', ProductContentListView.as_view(), name='list_products'),
    path('shop/', include('shop.urls'), name='shop'),
    path('management/', include('management.urls'), name='management'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
