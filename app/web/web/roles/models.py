# roles/models.py
from django.db import models


class Role(models.Model):
    name = models.CharField(maxlength=100)
    permissions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
