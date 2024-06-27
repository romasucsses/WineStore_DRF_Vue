from rest_framework import serializers
from .models import *


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = '__all__'
