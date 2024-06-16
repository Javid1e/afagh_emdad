from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from django.utils import timezone

def validate_username(value):
    if len(value) < 3:
        raise ValidationError(_('Username must be at least 3 characters long.'))
    if len(value) > 30:
        raise ValidationError(_('Username must be at most 30 characters long.'))
def validate_password(value):
    if len(value) < 8:
        raise ValidationError(_('Password must be at least 8 characters.'))
    if not re.search(r'[A-Z]', value):
        raise ValidationError(_('Password must contain at least one uppercase letter.'))
    if not re.search(r'\d', value):
        raise ValidationError(_('Password must contain at least one digit.'))
    if not re.search(r'[!@#$%^&*()_+]', value):
        raise ValidationError(_('Password must contain at least one special character.'))

def validate_name(value):
    if len(value) < 3:
        raise ValidationError(_('Name must be at least 3 characters long.'))
    if len(value) > 30:
        raise ValidationError(_('Name must be at most 30 characters long.'))


def validate_last_name(value):
    if len(value) < 3:
        raise ValidationError(_('Last name must be at least 3 characters long.'))
    if len(value) > 30:
        raise ValidationError(_('Last name must be at most 30 characters long.'))


def validate_birthday(value):
    if value > timezone.now().date():
        raise ValidationError(_('Date cannot be in the future.'))


def validate_phone_number(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError(_('Phone number must be entered in the format: "09XXXXXXXXX". 11 digits required.'))


def validate_email(value):
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
        raise ValidationError(_('Enter a valid email address.'))






def validate_url(value):
    if not re.match(r'^https?://(?:[-\w.]|%[\da-fA-F]{2})+/(?:(?![-\w]|%[\da-fA-F]{2})[\w-./?=&#~]*)?', value):
        raise ValidationError(_('Enter a valid URL.'))
