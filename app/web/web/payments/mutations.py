# payments/mutations.py
import graphene
from .models import Payment
from .types import PaymentType
from django.core.exceptions import ValidationError


class CreatePayment(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        request_id = graphene.Int(required=True)
        amount = graphene.Float(required=True)
        status = graphene.String()
        transaction_details = graphene.String()

    def mutate(self, info, request_id, amount, status=None, transaction_details=None):
        payment = Payment(request_id=request_id, amount=amount, status=status, transaction_details=transaction_details)
        try:
            payment.full_clean()
            payment.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreatePayment(payment=payment)


class UpdatePayment(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        id = graphene.Int(required=True)
        amount = graphene.Float()
        status = graphene.String()
        transaction_details = graphene.String()

    def mutate(self, info, id, amount=None, status=None, transaction_details=None):
        payment = Payment.objects.get(pk=id)
        if amount:
            payment.amount = amount
        if status:
            payment.status = status
        if transaction_details:
            payment.transaction_details = transaction_details
        try:
            payment.full_clean()
            payment.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdatePayment(payment=payment)


class DeletePayment(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        payment = Payment.objects.get(pk=id)
        payment.delete()
        return DeletePayment(payment=payment)
