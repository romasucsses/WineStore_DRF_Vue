from django.urls import path
from .views import *


urlpatterns = [
    path('all-orders/', OrdersViewAPI.as_view(), name='all_orders'),
    path('create-new-order/', CreateOrderAPI.as_view(), name='create_new_order'),
    path('contact-us/', ContactUsViewAPI.as_view(), name='contact_us'),
]
