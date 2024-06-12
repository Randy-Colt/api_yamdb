from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from users.models import User
from reviews.models import Category, Genre, Title, Review, Comment


# Расширяем ImportExportModelAdmin для включения модели пользователя
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    pass


# Регистрируем модель пользователя с расширенным администратором
admin.site.register(User, CustomUserAdmin)


# Регистрируем другие модели
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    pass


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    pass
