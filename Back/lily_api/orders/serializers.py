from rest_framework import serializers
from .models import OrderInfo


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'