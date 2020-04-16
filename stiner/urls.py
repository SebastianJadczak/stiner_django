from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from map.views import map
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map, name='map'),
    path('blog/', include('blog.urls'), name='blog'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
