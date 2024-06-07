# transactions/validations.py
from django.core.exceptions import ValidationError


def validate_transaction_type(value):
    allowed_types = ['otp_reward', 'payment']
    if value not in allowed_types:
        raise ValidationError(f'Transaction type must be one of {allowed_types}.')
