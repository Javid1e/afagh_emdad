# cities/models.py
from django.db import models
from .validations import validate_city_name


class City(models.Model):
    name = models.CharField(max_length=100, validators=[validate_city_name])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
