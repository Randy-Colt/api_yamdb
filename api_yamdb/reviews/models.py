from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from reviews.abstract_model import CategoryGenreBaseModel, ReviewCommBaseModel
from reviews.constants import MAX_SCORE, MIN_SCORE, NAME_MAX
from reviews.validators import validate_year

User = get_user_model()


class Category(CategoryGenreBaseModel):
    """Модель категории."""

    class Meta(CategoryGenreBaseModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(CategoryGenreBaseModel):
    """Модель для представления жанра произведения."""

    class Meta(CategoryGenreBaseModel.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """Модель для хранения информации о произведении."""

    name = models.CharField(verbose_name='Название', max_length=NAME_MAX)
    year = models.SmallIntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year])
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

    def __str__(self):
        return self.name


class Review(ReviewCommBaseModel):
    """Модель отзыва к произведению."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(
                MIN_SCORE,
                message=f'Нельзя поставить оценку ниже {MIN_SCORE}!'
            ),
            MaxValueValidator(
                MAX_SCORE,
                message=f'Нельзя поставить оценку выше {MAX_SCORE}!'
            )
        ]
    )

    class Meta(ReviewCommBaseModel.Meta):
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]


class Comment(ReviewCommBaseModel):
    """Модель комментария к отзыву."""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )

    class Meta(ReviewCommBaseModel.Meta):
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
