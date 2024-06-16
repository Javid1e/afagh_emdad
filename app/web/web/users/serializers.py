from rest_framework import serializers
from django.utils.translation import gettext as _
from .models import User
from .validations import validate_name, validate_last_name, validate_phone_number, validate_email, validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    @staticmethod
    def validate_name(value):
        validate_name(value)
        return value

    @staticmethod
    def validate_last_name(value):
        validate_last_name(value)
        return value

    @staticmethod
    def validate_phone_number(value):
        validate_phone_number(value)
        return value

    @staticmethod
    def validate_email(value):
        validate_email(value)
        return value

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return value


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'last_name', 'phone_number', 'email', 'password')

    @staticmethod
    def validate_name(value):
        validate_name(value)
        return value

    @staticmethod
    def validate_last_name(value):
        validate_last_name(value)
        return value

    @staticmethod
    def validate_phone_number(value):
        validate_phone_number(value)
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(_("Phone number already exists"))
        return value

    @staticmethod
    def validate_email(value):
        validate_email(value)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email already exists"))
        return value

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['phone_number'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, validators=[validate_phone_number])
    password = serializers.CharField(max_length=128, write_only=True)

    @staticmethod
    def validate_phone_number(value):
        validate_phone_number(value)
        return value

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return value


class OTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, validators=[validate_phone_number])

    @staticmethod
    def validate_phone_number(value):
        validate_phone_number(value)
        return value


class OTPVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, validators=[validate_phone_number])
    otp = serializers.CharField(max_length=6)

    @staticmethod
    def validate_phone_number(value):
        validate_phone_number(value)
        return value

    @staticmethod
    def validate_otp(value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError(_("OTP must be a 6-digit number."))
        return value
