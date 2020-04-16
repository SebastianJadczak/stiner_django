from django.contrib import admin
from django.urls import path, include
from map.views import map
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map, name='map'),
    path('blog/', include('blog.urls'), name='blog')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
