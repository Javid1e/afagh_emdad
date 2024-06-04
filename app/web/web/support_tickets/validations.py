# support_tickets/validations.py
from django.core.exceptions import ValidationError


def validate_subject(value):
    if len(value) < 5:
        raise ValidationError('Subject must be at least 5 characters long.')


def validate_status(value):
    allowed_statuses = ['open', 'in_progress', 'closed']
    if value not in allowed_statuses:
        raise ValidationError(f'Status must be one of {allowed_statuses}.')
