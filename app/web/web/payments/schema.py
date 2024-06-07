# payments/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Payment
from .mutations import CreatePayment, UpdatePayment, DeletePayment
from .types import PaymentType


class Query(graphene.ObjectType):
    all_payments = graphene.List(PaymentType)
    payment = graphene.Field(PaymentType, id=graphene.Int())

    def resolve_all_payments(self, info, **kwargs):
        return Payment.objects.all()

    def resolve_payment(self, info, id):
        return Payment.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_payment = CreatePayment.Field()
    update_payment = UpdatePayment.Field()
    delete_payment = DeletePayment.Field()
