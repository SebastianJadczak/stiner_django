from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('category/<slug:name_category>', views.ProductContentListView.as_view(), name='products_list_category')
]

