from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from users.permissions import *


class CreateOrderAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        new_order = OrdersSerializer(data=request.data)
        if new_order.is_valid():
            if request.user.is_authenticated:
                user = request.user
                new_order.save(user=user, shipping_data=user.user_shipping_address)
            else:
                new_order.save()

            return Response('New Order have been created')
        return Response('Did not created')


class OrdersViewAPI(APIView):
    def get(self, request):
        all_orders = OrderInfo.objects.all(user=request.user)
        return Response({'orders': OrdersSerializer(all_orders, many=True)})

    def post(self, request):
        pass


class DetailOrderViewAPI(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass


class ShippingInfoViewAPI(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass


class ContactUsViewAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        new_msg = ContactUsSerializer(data=request.data)
        if new_msg.is_valid():
            new_msg.save()
            return Response('The msg have been created')
        return Response('Not created')
