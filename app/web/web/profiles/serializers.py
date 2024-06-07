# profiles/serializers.py
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'personal_information', 'car_information', 'created_at', 'updated_at']
