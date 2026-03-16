from rest_framework.permissions import BasePermission

class IsMechanic(BasePermission):
    """
    Allows access only to users with role='mechanic'
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'mechanic')

class IsAdmin(BasePermission):
    """
    Allows access only to users with role='admin'
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class IsOwnerOrAdmin(BasePermission):
    """
    Allows access if user is the object owner or an admin
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.role == 'admin'
