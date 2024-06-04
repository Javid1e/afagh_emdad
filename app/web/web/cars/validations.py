# cars/validations.py
from django.core.exceptions import ValidationError


def validate_license_plate(value):
    if len(value) < 6 or len(value) > 10:
        raise ValidationError('License plate must be between 6 and 10 characters long.')


def validate_year(value):
    if value < 1886 or value > timezone.now().year:
        raise ValidationError(f'Year must be between 1886 and {timezone.now().year}.')
