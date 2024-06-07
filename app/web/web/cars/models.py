# cars/models.py
from django.db import models
from users.models import User
from .validations import validate_license_plate, validate_year


class Car(models.Model):
    user = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[validate_year])
    license_plate = models.CharField(max_length=20, validators=[validate_license_plate])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Car {self.make} {self.model} ({self.license_plate})"
