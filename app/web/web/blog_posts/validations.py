# blog_posts/validations.py
from django.core.exceptions import ValidationError


def validate_content(value):
    if len(value) < 20:
        raise ValidationError('Content must be at least 20 characters long.')
