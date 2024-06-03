# certificates/models.py
from django.db import models
from ..users.models import User


# //Todo : {Certificate is For company}
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)
    name = models.CharField(maxlength=100)
    issued_by = models.CharField(maxlength=100)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
