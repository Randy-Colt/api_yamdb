from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

User = get_user_model()

# Расширяем ImportExportModelAdmin для включения модели пользователя
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    pass

# Регистрируем модель пользователя с расширенным администратором
admin.site.register(User, CustomUserAdmin)
