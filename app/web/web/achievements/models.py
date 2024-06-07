# achievements/models.py
from django.db import models
from .validations import validate_date


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(validators=[validate_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
