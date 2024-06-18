from django.urls import path
from .views import *


urlpatterns = [
    path('all-orders/', OrdersViewAPI.as_view(), name='all_orders'),
    path('<int:order_id>/', DetailOrderViewAPI.as_view(), name='view_order'),
    path('shipping-info/', ShippingInfoViewAPI.as_view(), name='shipping_info'),
    path('create-new-order/', CreateOrderAPI.as_view(), name='create_new_order'),
    path('contact-us/', ContactUsViewAPI.as_view(), name='contact_us')
]
