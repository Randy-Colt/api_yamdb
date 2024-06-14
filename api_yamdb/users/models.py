from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    class Role(models.TextChoices):
        """Определение возможных ролей пользователей."""

        USER = 'user'
        MODER = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField('Почта', unique=True)
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
        null=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=max([len(x[0]) for x in Role.choices]),
        choices=Role.choices,
        default=Role.USER,
    )

    @property
    def is_personal(self):
        return any(
            (self.role == self.Role.ADMIN,
             self.is_superuser,
             self.is_staff,
             self.role == self.Role.MODER)
        )

    @property
    def is_admin(self):
        return any((self.role == self.Role.ADMIN, self.is_superuser))

    class Meta:
        ordering = 'username',
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
