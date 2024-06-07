# faqs/models.py
from django.db import models
from .validations import validate_question, validate_answer


class FAQ(models.Model):
    question = models.CharField(max_length=200, validators=[validate_question])
    answer = models.TextField(validators=[validate_answer])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
