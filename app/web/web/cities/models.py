# cities/models.py
from django.db import models


class City(models.Model):
    name = models.CharField(maxlength=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
