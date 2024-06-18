from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, username=None, password=None,  **extra_fields):
        if not email:
            email = username

        if not username:
            username = email

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self,  username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    DoesNotExist = None
    username = models.CharField(max_length=155, unique=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=355)
    name = models.CharField(max_length=155, null=True)
    last_name = models.CharField(max_length=155, null=True)
    user_shipping_address = models.ForeignKey('orders.ShippingInfo', on_delete=models.CASCADE, null=True)
    date_joining = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'User {self.email}'

