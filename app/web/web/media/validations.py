# media/validations.py
from django.core.exceptions import ValidationError


def validate_file_type(value):
    allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
    if value not in allowed_types:
        raise ValidationError(f'File type must be one of {allowed_types}.')
