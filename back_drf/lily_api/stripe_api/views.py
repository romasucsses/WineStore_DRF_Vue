from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from .stripe_config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


class CreatePaymentIntentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            # amount = request.data.get('amount')
            currency = 'usd'

            stripe.PaymentIntent.create(
                amount=100,
                currency=currency,
                payment_method_types=['card'],
                description='Test payment intent'
            )

            return Response({'order created'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

