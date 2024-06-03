# cars/models.py
from django.db import models
from ..users.models import User


class Car(models.Model):
    user = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    make = models.CharField(maxlength=50)
    model = models.CharField(maxlength=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(maxlength=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Car {self.make} {self.model} ({self.license_plate})"
