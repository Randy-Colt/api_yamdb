from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    class Role(models.TextChoices):
        USER = 'user'
        MODER = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField('Почта', unique=True)
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
        unique=True,
        blank=True,
        null=True,
        editable=False
    )


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        verbose_name='Категория',
        max_length=256,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    pass


class Title(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
