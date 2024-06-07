# cars/serializers.py
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'user', 'make', 'model', 'year', 'license_plate', 'created_at', 'updated_at']
