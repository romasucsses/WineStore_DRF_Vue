from django.urls import path
from .views import *


urlpatterns = [
    path('', OrdersViewAPI.as_view(), name='all_orders'),
    path('<int:order_id>/', DetailOrderViewAPI.as_view(), name='view_order'),
    path('shipping-info/', ShippingInfoViewAPI.as_view(), name='shipping_info'),
]