from rest_framework.views import APIView
from products.serializers import ProductSerializer
from products.models import *
from rest_framework.response import Response
from mixins.subsciber_post import SubscriberPost


class ShopViewAPI(SubscriberPost, APIView):
    def get_category(self):
        return None

    def get(self, request):
        category = self.get_category()

        if category:
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        query_action = request.GET.get('ordering_by', None)
        if query_action:
            print(query_action)
            return self.ordering_records(request, query_action, products)
        return Response(ProductSerializer(products, many=True).data)

    def ordering_records(self, request, query_action, products):
        if query_action == 'popularity':
            products = products.order_by('price')
        if query_action == 'price-up':
            products = products.order_by('price')
        if query_action == 'price-down':
            products = products.order_by('-price')

        return Response(ProductSerializer(products, many=True).data)


class WineViewAPI(ShopViewAPI):
    def get_category(self):
        return 1


class SparklingViewAPI(ShopViewAPI):
    def get_category(self):
        return 2
# class ContactUsAPI(APIView):
#     def post(self, request):
#         serializer = ''
#         if serializer.is_valid():
#             serializer.save()
#             return Response()


