# cities/validations.py
from django.core.exceptions import ValidationError


def validate_city_name(value):
    if len(value) < 3:
        raise ValidationError('City name must be at least 3 characters long.')
