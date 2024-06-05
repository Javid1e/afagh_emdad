# otp/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import OTP
from .mutations import CreateOTP, UpdateOTP, DeleteOTP
from .types import OTPType


class Query(graphene.ObjectType):
    all_otps = graphene.List(OTPType)
    otp = graphene.Field(OTPType, id=graphene.Int())

    def resolve_all_otps(self, info, **kwargs):
        return OTP.objects.all()

    def resolve_otp(self, info, id):
        return OTP.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_otp = CreateOTP.Field()
    update_otp = UpdateOTP.Field()
    delete_otp = DeleteOTP.Field()
