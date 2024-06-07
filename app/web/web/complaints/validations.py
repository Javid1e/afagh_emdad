# complaints/validations.py
from django.core.exceptions import ValidationError


def validate_description(value):
    if len(value) < 10:
        raise ValidationError('Description must be at least 10 characters long.')


def validate_status(value):
    allowed_statuses = ['open', 'resolved', 'closed']
    if value not in allowed_statuses:
        raise ValidationError(f'Status must be one of {allowed_statuses}.')
