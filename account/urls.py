from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # path('my_account', views.UserAccount.as_view(), name='user_account'),
       path('password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',
                                                           email_template_name='account/password_reset_email.html'),
         name="password_reset"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

