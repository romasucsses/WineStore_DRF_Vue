from django.urls import path
from products.views import *

urlpatterns = [
    path('', ShopViewAPI.as_view()),
    path('wine/', WineViewAPI.as_view()),
    path('sparkling/', SparklingViewAPI.as_view())
]