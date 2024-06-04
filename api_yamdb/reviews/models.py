from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    pass


class Genre(models.Model):
    pass


class Title(models.Model):
    pass
    blablabla


class Review(models.Model):
    pass


class Comment(models.Model):
    """Модель комментария к произведению."""

    text = models.TextField(verbose_name='Текст комментария')

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
