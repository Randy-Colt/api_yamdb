from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from api_yamdb.settings import EMAIL

User = get_user_model()



def send_confirmation_email(email, confirmation_code):
    """Отправляет сгенерированный confirmation_code пользователю."""

    send_mail(
        'Данные для получения токена',
        f'Код подтверждения: {confirmation_code}',
        f'{EMAIL}',
        [email],
    )
