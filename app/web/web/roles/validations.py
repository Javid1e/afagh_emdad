# roles/validations.py
from django.core.exceptions import ValidationError


def validate_permissions(value):
    if not isinstance(value, dict):
        raise ValidationError('Permissions must be a JSON object.')
