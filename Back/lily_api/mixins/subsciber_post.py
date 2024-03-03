from rest_framework.response import Response
from rest_framework.views import APIView
from mixins.serializers import EmailSerializer


class SubscriberPost:
    def post(self, request):
        if 'email' in request.data:
            serializer = EmailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("have got the email ", serializer)
