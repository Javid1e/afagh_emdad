# profiles/validations.py
from django.core.exceptions import ValidationError

def validate_personal_information(value):
    if not isinstance(value, dict):
        raise ValidationError('Personal information must be a JSON object.')

def validate_car_information(value):
    if not isinstance(value, dict):
        raise ValidationError('Car information must be a JSON object.')
