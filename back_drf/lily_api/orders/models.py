from django.contrib.sessions.models import Session
from django.db import models


class Coupon(models.Model):
    coupons = models.CharField(max_length=155)
    date_expiration = models.DateField(format('%Y/%m/%d'))
    percent_discount = models.FloatField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)


class ShippingInfo(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    country = models.CharField(max_length=255)
    street_address_1 = models.TextField()
    street_address_2 = models.TextField(null=True)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155, null=True)
    zip_code = models.CharField(max_length=55)
    phone = models.CharField(max_length=155)
    email = models.EmailField()


class OrderInfo(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_to_deliver = models.DateTimeField(null=True)

    STATUS_LIST = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_LIST, default=STATUS_LIST[0][1])
    cart_data = models.JSONField()
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, default=None)
    coupon = models.OneToOneField(Coupon, on_delete=models.PROTECT, null=True)
    total_sum = models.DecimalField(decimal_places=2, max_digits=15)

    user = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True, related_name='user_orders')
    shipping_data = models.ForeignKey('orders.ShippingInfo', on_delete=models.CASCADE, null=True,
                                      related_name='shipping_orders')



    def __str__(self):
        return f'Order Nr.{self.pk}'


class EmailSubscription(models.Model):
    email = models.EmailField()
    date_subscription = models.DateField(auto_now=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
