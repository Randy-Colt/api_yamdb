from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
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
    """Модель для представления жанра произведения."""

    name = models.CharField(max_length=256, vernose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Slug', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """ Модель для хранения информации о произведении."""
    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        default_related_name = 'titles'


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
