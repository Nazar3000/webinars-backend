from rest_framework import permissions


class IsOwnerOrIsAdmin(permissions.BasePermission):
    """
    Allow access only to owner or admin.
    """

    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user or request.user.is_staff)
