from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    pass


class Genre(models.Model):
    """Модель для представления жанра произведения."""

    name = models.CharField(max_length=256, vernose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Slug', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """Модель для хранения информации о произведении."""

    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(null=True, verbose_name='Описание')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        default_related_name = 'titles'
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    pass


class Comment(models.Model):
    """Модель комментария к произведению."""

    text = models.TextField(verbose_name='Текст комментария')

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
