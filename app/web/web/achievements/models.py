# achievements/models.py
from django.db import models


class Achievement(models.Model):
    title = models.CharField(maxlength=100)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
