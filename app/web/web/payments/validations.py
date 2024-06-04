# payments/validations.py
from django.core.exceptions import ValidationError


def validate_amount(value):
    if value <= 0:
        raise ValidationError('Amount must be a positive number.')


def validate_status(value):
    allowed_statuses = ['pending', 'completed', 'failed']
    if value not in allowed_statuses:
        raise ValidationError(f'Status must be one of {allowed_statuses}.')
