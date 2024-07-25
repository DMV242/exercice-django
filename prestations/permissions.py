from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
     The permission that allows authenticated users to create objects,
    but allows everyone to see the list of objects.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allows access to secure methods (GET, HEAD, OPTIONS) for all users
            return True
            # Allows only authenticated users to create, update, or delete
        return request.user and request.user.is_authenticated
