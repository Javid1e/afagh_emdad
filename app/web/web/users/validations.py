# users/validations.py
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError('Phone number must be entered in the format: "09XXXXXXXXX". 11 digits required.')

def validate_email(value):
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
        raise ValidationError('Enter a valid email address.')
