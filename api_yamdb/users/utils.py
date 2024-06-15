from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


def send_confirmation_email(email, confirmation_code):
    """Отправляет сгенерированный confirmation_code пользователю."""
    send_mail(
        'Данные для получения токена',
        f'Код подтверждения: {confirmation_code}',
        f'{settings.EMAIL}',
        [email],
    )
