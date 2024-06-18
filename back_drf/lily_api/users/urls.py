from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

urlpatterns = [
    path('get-token/', TokenObtainPairView().as_view(), name='token_obtain_pair'),
    path('get-refresh-token/', TokenRefreshView().as_view(), name='token_refresh'),
    path('get-verify-token/', TokenVerifyView().as_view(), name='token_verify'),
    path('my-account-details/', MyAccountInfo().as_view(), name='account_details'),
    path('my-account-details/view-my-shipping-info/', MyAddressInfo.as_view(), name='account_shipping'),
    path('my-account-details/my-orders/', MyOrdersInfo.as_view(), name='all_user_orders'),
    path('my-account-details/my-detail-order/<int:pk>/', MyDetailOrderInfo.as_view(), name='all_user_orders'),
    path('sign-up/', SingUp.as_view(), name='sign_up_view')

]
