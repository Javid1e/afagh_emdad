# otp/validations.py
from django.core.exceptions import ValidationError
import re


def validate_otp_code(value):
    if not re.match(r'^\d{6}$', value):
        raise ValidationError('OTP code must be a 6-digit number.')
