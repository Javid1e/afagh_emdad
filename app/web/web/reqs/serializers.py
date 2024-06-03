from rest_framework import serializers
from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'client', 'rescuer', 'status', 'location', 'description', 'created_at', 'updated_at']
