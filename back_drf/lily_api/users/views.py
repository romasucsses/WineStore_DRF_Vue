from django.http import Http404, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import User
from orders.serializers import OrdersSerializer
from orders.models import OrderInfo


class MyAccountInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def patch(self, request):
        user = User.objects.get(pk=request.user.pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(user.name)
            return JsonResponse(data=serializer.data)
        return Response(serializer.errors)


class MyOrdersInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = OrderInfo.objects.filter(user=request.user)
        return Response(OrdersSerializer(orders, many=True).data)

    def post(self, request):
        pass


class MyDetailOrderInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = OrderInfo.objects.get(pk=pk)
        return Response(OrdersSerializer(order).data)

    def post(self, request):
        pass


class MyAddressInfo(APIView):
    permission_classes = [IsAuthenticated]

    def getUserAddress(self, request):
        return request.user.user_shipping_address

    def get(self, request):
        return Response(ShippingAddressSerializer(self.getUserAddress(request)).data)

    def patch(self, request):
        new_data = ShippingAddressSerializer(self.getUserAddress(request), data=request.data, partial=True)
        if new_data.is_valid():
            new_data.save()
            user = self.getUserAddress(request)
            user = new_data.instance
            user.save()
            return Response('Done Successful')
        return Response('Not Successful')


class SingUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        new_user = UserSignUpSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response('User have been created')

        return Response('User Not Created')
