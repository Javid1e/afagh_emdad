# reviews/models.py
from django.db import models
from users.models import User
from .validations import validate_rating


class Review(models.Model):
    client = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[validate_rating])
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.id} by {self.client.username}"
