from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import OrdersSerializer


class OrdersViewAPI(APIView):
    def get(self, request):
        all_orders = OrderInfo.objects.all()
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
