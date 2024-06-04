from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    pass


class Genre(models.Model):
    pass


class Title(models.Model):
    pass


class Review(models.Model):
    """Модель отзыва к произведению."""

    title__id = models.IntegerField()  # Временная заглушка пока нет произведения.
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.IntegerField(verbose_name='Автор отзыва')  # Временная заглушка пока нет юзера.
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Рейтинг'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время отзыва')

    class Meta:
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    """Модель комментария к отзыву."""

    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
    )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.IntegerField(verbose_name='Автор комментария')  # Временная заглушка пока нет юзера.
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время комментария')

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
