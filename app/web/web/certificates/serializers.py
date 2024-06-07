# certificates/serializers.py
from rest_framework import serializers
from .models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'user', 'name', 'issued_by', 'issue_date', 'expiry_date', 'description', 'created_at',
                  'updated_at']
