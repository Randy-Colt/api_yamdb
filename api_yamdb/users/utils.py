from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string

from users.models import User


def generate_confirmation_code():
    """Генерирует confirmation_code."""
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
    return get_random_string(20, chars)


def send_confirmation_email(email, confirmation_code):
    """Отправляет сгенерированный confirmation_code пользователю."""
    user = get_object_or_404(
        User,
        email=email,
    )
    user.confirmation_code = confirmation_code
    user.save()
    send_mail(
        'Данные для получения токена',
        f'Код подтверждения: {confirmation_code}',
        'token@yamdb.ru',
        [email],
    )