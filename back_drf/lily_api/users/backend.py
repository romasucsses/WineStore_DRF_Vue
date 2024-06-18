from django.shortcuts import redirect

from users.models import User
from django.contrib.auth.backends import ModelBackend


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, is_active=False):

        try:
            user = User.objects.get(email=username)
            if user.is_active:
                return user

        except User.DoesNotExist:
            return None
