from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from reviews.models import Category, Genre, Title, Review, Comment


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    pass


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    list_display = ('name', 'year', 'category', 'display_genre')
    list_filter = ('category', 'genre')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('genre',)

    def display_genre(self, obj):
        """Возвращает строку из жанров, разделенных запятыми."""
        return ', '.join(genre.name for genre in obj.genre.all())
    display_genre.short_description = 'Жанры'


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'score', 'pub_date')
    search_fields = ('title__name', 'author__username')
    list_filter = ('score', 'pub_date')
    ordering = ('pub_date',)


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('review', 'author', 'pub_date')
    search_fields = ('review__title__name', 'author__username')
    list_filter = ('pub_date',)
    ordering = ('pub_date',)


User = get_user_model()


@admin.register(User)
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    pass
