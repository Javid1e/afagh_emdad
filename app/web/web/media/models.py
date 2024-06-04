# media/models.py
from django.db import models
from .validations import validate_file_type


class Media(models.Model):
    associated_model = models.ForeignKey(
        'contenttypes.ContentType', on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = models.GenericForeignKey('associated_model', 'object_id')
    file_url = models.URLField()
    file_type = models.CharField(max_length=50, validators=[validate_file_type])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Media {self.id} for {self.content_object}"
