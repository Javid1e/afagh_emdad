# requests/validations.py
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point

def validate_location(value):
    if not isinstance(value, Point):
        raise ValidationError('Location must be a Point object.')

def validate_status(value):
    allowed_statuses = ['pending', 'accepted', 'completed', 'cancelled']
    if value not in allowed_statuses:
        raise ValidationError(f'Status must be one of {allowed_statuses}.')
