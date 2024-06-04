# faqs/validations.py
from django.core.exceptions import ValidationError


def validate_question(value):
    if len(value) < 5:
        raise ValidationError('Question must be at least 5 characters long.')


def validate_answer(value):
    if len(value) < 10:
        raise ValidationError('Answer must be at least 10 characters long.')
