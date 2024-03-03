from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

urlpatterns = [
    path('get-token/', TokenObtainPairView().as_view(), name='token_obtain_pair'),
    path('get-refresh-token/', TokenRefreshView().as_view(), name='token_refresh'),
    path('get-verify-token/', TokenVerifyView().as_view(), name='token_verify'),
    path('my-account-details/', MyAccountInfo().as_view(), name='account_details')
#     path('register/'),
#     path('login/'),
#     path('logout/'),
#     path('my-account/'),
]
