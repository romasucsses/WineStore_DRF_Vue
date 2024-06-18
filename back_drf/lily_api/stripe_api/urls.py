from django.urls import path
from .views import *

urlpatterns = [
    path('create-order/', CreatePaymentIntentView.as_view())
]
