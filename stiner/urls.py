
from django.contrib import admin
from django.urls import path, include
from map.views import map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map, name='map'),
    path('blog/', include('blog.urls'), name='blog')
]
