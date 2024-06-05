from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    class Role(models.TextChoices):
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
        max_length=300,
        unique=True,
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """Модель для представления жанра произведения."""

    name = models.CharField(
        verbose_name='Название',
        max_length=256,
        unique=True
    )
    slug = models.SlugField(verbose_name='Слаг', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """ Модель для хранения информации о произведении."""

    name = models.CharField(verbose_name='Название', max_length=256)
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
        default_related_name = 'titles'
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    """Модель отзыва к произведению."""

    title_id = models.ForeignKey(
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
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время отзыва')

    class Meta:
        ordering = 'pub_date',
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    """Модель комментария к отзыву."""

    review_id = models.ForeignKey(
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
