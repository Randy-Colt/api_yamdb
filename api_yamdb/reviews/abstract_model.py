from django.contrib.auth import get_user_model
from django.db import models

from reviews.constants import NAME_MAX

User = get_user_model()


class CategoryGenreBaseModel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=NAME_MAX,
        unique=True
    )
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    class Meta:
        abstract = True
        ordering = 'name',

    def __str__(self):
        return self.name


class ReviewCommBaseModel(models.Model):
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время публикации')

    class Meta:
        abstract = True
        ordering = 'pub_date',

    def __str__(self):
        return f'Публикация автора {self.author}'  # наверное, поменяем
