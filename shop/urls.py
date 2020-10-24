from django.urls import path, include

import orders
from . import views

app_name = 'shop'

urlpatterns = [
    path('category/<int:pk>', views.ProductContentListView.as_view(), name='products_list_category'),
    path('product/<slug:id_product>', views.ProductDetailListView.as_view(), name='product_detail'),
]

