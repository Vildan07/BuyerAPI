from rest_framework.permissions import BasePermission


class AuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method == 'GET' or request.method == 'POST':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False

