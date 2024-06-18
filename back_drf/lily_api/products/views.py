from django.http import JsonResponse
from rest_framework.views import APIView
from products.serializers import *
from products.models import *
from rest_framework.response import Response
from utils.subsciber_post import SubscriberPost
from users.permissions import *
from utils.cache_logic import *
from .pagination import ReviewsPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class ShopViewAPI(SubscriberPost, APIView):
    permission_classes = [AnyOne]

    def get_category(self):
        return None


    def get(self, request):
        category = self.get_category()

        if category:
            cache_name = PRODUCTS_LIST_CACHE_ALL_NAME + f"_{category}"
            products = Product.objects.filter(category=category)
            result = get_set_cache(
                queryset=products,
                serializer=ProductSerializer,
                cache_name=cache_name,
                type_data='list'

            )
        else:
            products = Product.objects.all()
            result = get_set_cache(
                queryset=products,
                serializer=ProductSerializer,
                cache_name=PRODUCTS_LIST_CACHE_ALL_NAME,
                type_data='list'
            )

        query_action = request.GET.get('ordering_by', None)
        if query_action:
            print(query_action)
            return self.ordering_records(request, query_action, products)
        return Response(result)

    @method_decorator(cache_page(20 * (60 * 60)))
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


class DetailProductViewAPI(APIView):
    permission_classes = [AnyOne]


    def get(self, request, uniq_url_slug):
        print(uniq_url_slug)
        product = Product.objects.get(slug_url=uniq_url_slug)
        result = get_set_cache(
            queryset=product,
            serializer=ProductSerializer,
            cache_name= PRODUCT_DETAIL_CACHE_NAME + uniq_url_slug,
            type_data='detail'

        )
        return Response(result)


class ReviewsAPI(APIView, ReviewsPagination):
    permission_classes = [AnyOne]

    def getProduct(self, product_id):
        return Product.objects.get(pk=product_id)

    @method_decorator(cache_page(20 * (60 * 60)))
    def get(self, request, product_id):
        product = self.getProduct(product_id)
        reviews = self.paginate_queryset(Reviews.objects.filter(product=product), request)
        if reviews is None:
            return JsonResponse("Have not one yet", safe=False)
        else:
            serializer = ReviewSerializer(reviews, many=True)
            result = get_set_cache(
                queryset=product,
                serializer=ProductSerializer,
                cache_name=PRODUCT_DETAIL_CACHE_NAME,
                type_data='detail'
            )
            return self.get_paginated_response(serializer.data)

    def post(self, request, product_id):
        new_review = ReviewSerializer(data=request.data)
        if new_review.is_valid():
            product = self.getProduct(product_id)
            new_review.save(product=product)

            return JsonResponse('New Review Added Successful', safe=False)
        return JsonResponse('Not Added!', safe=False)
