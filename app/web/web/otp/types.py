from graphene_django import DjangoObjectType
from .models import OTP


class OTPType(DjangoObjectType):
    class Meta:
        model = OTP
