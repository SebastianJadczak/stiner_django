from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('my_account', views.UserAccount.as_view(), name='user_account'),
]

