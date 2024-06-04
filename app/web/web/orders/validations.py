# orders/validations.py
from django.core.exceptions import ValidationError


def validate_service_type(value):
    allowed_services = ['towing', 'battery', 'tire', 'lockout']
    if value not in allowed_services:
        raise ValidationError(f'Service type must be one of {allowed_services}.')


def validate_status(value):
    allowed_statuses = ['pending', 'completed', 'cancelled']
    if value not in allowed_statuses:
        raise ValidationError(f'Status must be one of {allowed_statuses}.')
