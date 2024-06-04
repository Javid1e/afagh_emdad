# payments/serializers.py
from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'request', 'amount', 'status', 'transaction_details', 'created_at', 'updated_at']
