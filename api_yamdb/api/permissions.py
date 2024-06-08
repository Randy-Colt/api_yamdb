from rest_framework import permissions

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     message = 'У вас нет доступа для совершения этого действия.'

#     def has_permission(self, request, view):
#         return (
#                 request.method in permissions.SAFE_METHODS
#                 or request.user.is_authenticated
#             )

#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user


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
