from graphene_django import DjangoObjectType
from .models import Payment


class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment
