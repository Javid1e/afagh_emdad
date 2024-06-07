# otp/mutations.py
import graphene
from .models import OTP
from .types import OTPType
from django.core.exceptions import ValidationError


class CreateOTP(graphene.Mutation):
    otp = graphene.Field(OTPType)

    class Arguments:
        phone_number = graphene.String(required=True)

    def mutate(self, info, phone_number):
        otp = OTP(phone_number=phone_number)
        try:
            otp.full_clean()
            otp.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateOTP(otp=otp)


class UpdateOTP(graphene.Mutation):
    otp = graphene.Field(OTPType)

    class Arguments:
        id = graphene.Int(required=True)
        phone_number = graphene.String()

    def mutate(self, info, id, phone_number=None):
        otp = OTP.objects.get(pk=id)
        if phone_number:
            otp.phone_number = phone_number
        try:
            otp.full_clean()
            otp.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateOTP(otp=otp)


class DeleteOTP(graphene.Mutation):
    otp = graphene.Field(OTPType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        otp = OTP.objects.get(pk=id)
        otp.delete()
        return DeleteOTP(otp=otp)
