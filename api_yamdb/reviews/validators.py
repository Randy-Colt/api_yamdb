from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_year(value):
    if value > datetime.now().year:
        raise ValidationError(
            _(f"{value} больше текущего года"),
            params={"value": value},
        )
