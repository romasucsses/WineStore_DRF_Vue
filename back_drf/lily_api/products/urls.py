from django.urls import path
from products.views import *

urlpatterns = [
    path('', ShopViewAPI.as_view()),
    path('wine/', WineViewAPI.as_view()),
    path('sparkling/', SparklingViewAPI.as_view()),
    path('product-detail/<slug:uniq_url_slug>/', DetailProductViewAPI.as_view()),
    path('product-reviews/<int:product_id>', ReviewsAPI.as_view())
]
