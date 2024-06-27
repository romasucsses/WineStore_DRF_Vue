from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from users.permissions import *
from .tasks import send_emails
from rest_framework import status


class CreateOrderAPI(APIView):
    permission_classes = [AllowAny]

    def sendEmailToAdminAndClient(self, client_email, order_data):
        emails_list = 'canalofmoney2020@gmail.com,canalofmoney2020@gmail.com'
        title = 'New Order on La Fleur Lily website'
        msg = (
            f'order data: Cart data - {order_data.cart_data} '
            f'Shipping data - {order_data.shipping_data}'
        )
        send_emails.delay(emails_list=emails_list, title=title, msg=msg)
        title = 'Thank You for Making Order at LaFleurLily'
        msg = (
            f'Hi {order_data.shipping_data.first_name}, your Order have been placed'
            f'ID Order is : #{order_data.id}'
            f'you also can call us : +1234253265 or email: supportLily@gmail.com'
        )
        send_emails.delay(emails_list=client_email, title=title, msg=msg)

    def post(self, request):
        if request.user.is_authenticated:
            new_order = OrdersSerializer(data=request.data)

            if new_order.is_valid():
                user = request.user
                shipping_address = user.user_shipping_address

                if shipping_address is None:
                    return Response({'message': 'Your Shipping Address is None', 'isShippingAddress': False})
                order = new_order.save(user=user, shipping_data=user.user_shipping_address)
                self.sendEmailToAdminAndClient(user.user_shipping_address.email, order)
                return Response({'message': 'Order was successfully created', 'order_id': order.id}, status=status.HTTP_201_CREATED)

            else:
                return Response({'error': 'Some error with data', 'details': new_order.errors}, status=status.HTTP_400_BAD_REQUEST)

        else:
            shipping_address = request.data.get('shipping_data', None)

            if not shipping_address:
                return Response({'error': 'Missing data about shipping address'}, status=status.HTTP_400_BAD_REQUEST)

            new_shipping_address = ShippingAddressSerializer(data=shipping_address)

            if new_shipping_address.is_valid():
                address = new_shipping_address.save()
                new_order_data = request.data.copy()
                new_order_data['shipping_data'] = address.id
                new_order = OrdersSerializer(data=new_order_data)

                if new_order.is_valid():
                    order = new_order.save()
                    self.sendEmailToAdminAndClient(address.email, order)
                    return Response({'message': 'New Order has been created for Guest', 'order_id': order.id}, status=status.HTTP_201_CREATED)
                return Response({'error': 'Some problems with order data', 'details': new_order.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Some problems with Shipping Address data', 'details': new_shipping_address.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrdersViewAPI(APIView):
    def get(self, request):
        all_orders = OrderInfo.objects.all(user=request.user)
        return Response({'orders': OrdersSerializer(all_orders, many=True)})


class ContactUsViewAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        new_msg = ContactUsSerializer(data=request.data)
        if new_msg.is_valid():
            new_msg.save()
            return Response('The msg have been created')
        return Response('Not created')


