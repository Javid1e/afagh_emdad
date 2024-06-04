# media/serializers.py
from rest_framework import serializers
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'associated_model', 'object_id', 'file_url', 'file_type', 'created_at', 'updated_at']
