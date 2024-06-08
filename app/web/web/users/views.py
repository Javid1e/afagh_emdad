# users/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.translation import gettext as _
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, OTPSerializer, OTPVerifySerializer
from .utils import generate_otp, verify_otp
from django.contrib.auth import authenticate
from graphql_jwt.shortcuts import get_token
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("User created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating user"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("User updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating user"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("User deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting user"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            user = authenticate(request, username=phone_number, password=password)
            if user is not None:
                token = get_token(user)
                return Response({'token': token, 'message': _("Login successful")})
            else:
                return Response({'error': _("Invalid credentials")}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        request.user.auth_token.delete()
        return Response({'message': _("Logout successful")}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='profile')
    def profile(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': _("Registration successful")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='otp')
    def send_otp(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = generate_otp()
            # Here you would integrate with an SMS gateway to send the OTP
            # For now, we'll just return the OTP for testing purposes
            return Response({'otp': otp, 'message': _("OTP sent to phone number")})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='verify-otp')
    def verify_otp(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            user_otp = serializer.validated_data['otp']
            otp = serializer.validated_data['otp']
            if verify_otp(user_otp, otp):
                return Response({'message': _("OTP verified")})
            else:
                return Response({'error': _("Invalid OTP")}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
