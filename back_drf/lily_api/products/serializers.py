from rest_framework import serializers
from products.models import *
from lily_api import settings


class ProductSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_img_url(self, obj):
        return f'{settings.BASE_URL}{obj.image.url}'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
