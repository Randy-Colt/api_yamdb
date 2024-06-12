from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    class Role(models.TextChoices):
        """Определение возможных ролей пользователей."""

        USER = 'user'
        MODER = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField('Почта', max_length=254, unique=True)
    bio = models.TextField(
        verbose_name='Биография',
        max_length=300,
        blank=True,
        null=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )
    confirmation_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
