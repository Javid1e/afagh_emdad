# complaints/serializers.py
from rest_framework import serializers
from .models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'user', 'order', 'description', 'status', 'resolution', 'created_at', 'updated_at']
