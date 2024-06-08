from rest_framework import permissions


class IsAuthorAdminModerator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        return bool(
            request.user.role == 'moderator' and request.user.is_staff or
            request.user.role == 'admin' and request.user.is_superuser
        )
