# roles/models.py
from django.db import models
from .validations import validate_permissions


class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.JSONField(validators=[validate_permissions])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
