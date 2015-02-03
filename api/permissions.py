# -*- encoding: utf-8 -*-
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # permitir solo a los dueños de los tickets poder modificarlos.
        return obj.usuario_id == request.user

class IsOwnerOrReadOnlyUsers(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # permitir solo a los dueños de los tickets poder modificarlos.
        return obj == request.user
