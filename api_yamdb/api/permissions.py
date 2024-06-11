from rest_framework import permissions


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на изменение и удаление Отзыва и Комментария
        Автором/Модератором/Админом."""

    message = 'У вас нет доступа для совершения этого действия.'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == 'moderator'
            or request.user.role == 'admin'
            or request.user.is_staff is True
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на изменение и удаление Произведения,
        Жанра и Категории Админом."""

    message = 'У вас нет доступа для совершения этого действия.'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.role == 'admin'
                     or request.user.is_staff is True))
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == 'admin'
            or request.user.is_staff is True
        )


class IsAdmin(permissions.BasePermission):
    """Разрешение на доступ к пользователям."""

    message = 'У вас нет доступа для совершения этого действия.'

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.role == 'admin'
                     or request.user.is_staff is True)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'admin'
            or request.user.is_staff is True
        )