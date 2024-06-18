from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lily_api import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/stripe-api/', include('stripe_api.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
