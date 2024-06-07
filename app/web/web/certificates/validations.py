# certificates/validations.py
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_expiry_date(value):
    if value < timezone.now().date():
        raise ValidationError('Expiry date cannot be in the past.')
