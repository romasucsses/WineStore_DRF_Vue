from rest_framework import serializers
from products.models import *


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        image = obj.diaryimage_set.all()
        return ProductImageSerializer(instance=image, many=True, context=self.context).data
