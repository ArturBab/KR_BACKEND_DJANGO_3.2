from rest_framework import permissions
from backend.models import *


class IsAuthorUpdateOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если пользователь (или автор) тот самый, который создал свою запись -> True else False
        return obj.user == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)