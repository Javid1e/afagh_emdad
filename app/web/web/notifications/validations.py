# notifications/validations.py
from django.core.exceptions import ValidationError


def validate_notification_type(value):
    allowed_types = ['email', 'sms', 'push']
    if value not in allowed_types:
        raise ValidationError(f'Notification type must be one of {allowed_types}.')
