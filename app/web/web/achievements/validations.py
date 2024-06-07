# achievements/validations.py
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(value):
    if value > timezone.now().date():
        raise ValidationError('Date cannot be in the future.')
