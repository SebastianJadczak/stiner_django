from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from map import views
from map.views import Map, MapFullScreen, FavoriteList
from django.conf import settings
from django.conf.urls.static import static
from shop.views import ProductContentListView
from user_trails.views import UserTrailsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Map.as_view(), name='map'),
    path('mapFullScreen/', MapFullScreen.as_view(), name='mapFullScreen'),
    path('map/', include('map.urls')),
    path('account/', include('account.urls')),
    path('favorite/', FavoriteList.as_view(), name='favorite'),
    path('blog/', include('blog.urls'), name='blog'),
    # path('orders/', include('orders.urls', namespace='orders')),
    path('trails/', include('trails.urls', namespace='trails')),
    path('yours_trails/', UserTrailsListView.as_view(), name='yours_trails'),
    path('user_trails/', include('user_trails.urls',namespace='user_trails')),
    path('management/', include('management.urls'), name='management'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserFormView.as_view(), name='register'),
    # path('cart/', include('cart.urls', namespace='cart')),
    path('contact', include('contact.urls', namespace='contact')),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset/done',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
