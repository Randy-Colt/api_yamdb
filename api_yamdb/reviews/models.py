from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.db import models

from api.constants import GENRE_SLUG_MAX, MIN_SCORE, MAX_SCORE, NAME_MAX


User = get_user_model()


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        verbose_name='Категория',
        max_length=NAME_MAX,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = 'name',
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """Модель для представления жанра произведения."""

    name = models.CharField(
        verbose_name='Название',
        max_length=NAME_MAX,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг', max_length=GENRE_SLUG_MAX, unique=True)

    class Meta:
        ordering = 'name',
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """Модель для хранения информации о произведении."""

    name = models.CharField(verbose_name='Название', max_length=NAME_MAX)
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        ordering = 'name',
        default_related_name = 'titles'
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    """Модель отзыва к произведению."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва')
    score = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(MIN_SCORE), MaxValueValidator(MAX_SCORE)]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время отзыва')

    class Meta:
        ordering = 'pub_date',
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]


class Comment(models.Model):
    """Модель комментария к отзыву."""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время комментария')

    class Meta:
        ordering = 'pub_date',
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
