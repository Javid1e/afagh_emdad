# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validations import validate_phone_number, validate_email


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, validators=[validate_phone_number])
    email = models.EmailField(unique=True, validators=[validate_email])
    role = models.CharField(max_length=20, choices=[('client', 'Client'), ('rescuer', 'Rescuer'), ('admin', 'Admin'),
                                                    ('super_admin', 'Super Admin')])
    address = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
