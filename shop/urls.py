from django.urls import path, include

import orders
from . import views

app_name = 'shop'

urlpatterns = [
    # path('category/<int:pk>', views.ProductContentListView.as_view(), name='products_list_category'),
    # path('category/', views.Search.as_view(), name='products_list_category'),
    # path('product/<slug:id_product>', views.ProductDetailListView.as_view(), name='product_detail'),
    # path('product/', views.Search.as_view(), name='product_detail'),
    # path('user/messages', views.MessagesBox.as_view(), name='messages-box'),
    # path('user/', views.Search.as_view(), name='search'),
    # path('user/messages-new', views.MessagesBoxNew, name='messages-box-new'),
    # path('user/messages-send', views.MessagesBoxSend.as_view(), name='messages-box-send'),
    # path('user/messages/important', views.important, name='important'),
    # path('user/messages/delete', views.delete, name='delete'),
    # path('user/messages-important',  views.MessagesBoxImportant.as_view(), name='messages-box-important'),
    # path('user/messages-delete',  views.MessagesBoxDelete.as_view(), name='messages-box-delete'),
    # path('user/put-up-for-sale',  views.PutUpForSale.as_view(), name='put-up-for-sale'),
    # path('user/payments',  views.Payments.as_view(), name='payments'),
    # path('user/purchased_products',  views.PurchasedProducts.as_view(), name='purchased_products'),
    # path('user/user_data',  views.UserData.as_view(), name='user_data'),
    # path('user/sell_product',  views.SellProduct.as_view(), name='sell_product'),
    # path('user/unsold_product',  views.UnsoldProduct.as_view(), name='unsold_product'),
]

