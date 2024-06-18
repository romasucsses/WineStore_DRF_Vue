from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class AnyOne(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated or user.is_anonymous
