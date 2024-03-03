from rest_framework import serializers
from orders.models import EmailSubscription


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ["email"]
