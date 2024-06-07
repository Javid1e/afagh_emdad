# profiles/models.py
from django.db import models
from users.models import User
from .validations import validate_personal_information, validate_car_information


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    personal_information = models.JSONField(validators=[validate_personal_information])
    car_information = models.JSONField(validators=[validate_car_information])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
