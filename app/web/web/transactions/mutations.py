import graphene
from .models import Transaction
from .types import TransactionType
from django.core.exceptions import ValidationError


class CreateTransaction(graphene.Mutation):
    transaction = graphene.Field(TransactionType)

    class Arguments:
        amount = graphene.Float(required=True)
        status = graphene.String(required=True)
        user_id = graphene.Int(required=True)

    def mutate(self, info, amount, status, user_id):
        transaction = Transaction(amount=amount, status=status, user_id=user_id)
        try:
            transaction.full_clean()
            transaction.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateTransaction(transaction=transaction)


class UpdateTransaction(graphene.Mutation):
    transaction = graphene.Field(TransactionType)

    class Arguments:
        id = graphene.Int(required=True)
        amount = graphene.Float()
        status = graphene.String()

    def mutate(self, info, id, amount=None, status=None):
        transaction = Transaction.objects.get(pk=id)
        if amount:
            transaction.amount = amount
        if status:
            transaction.status = status
        try:
            transaction.full_clean()
            transaction.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateTransaction(transaction=transaction)


class DeleteTransaction(graphene.Mutation):
    transaction = graphene.Field(TransactionType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        transaction = Transaction.objects.get(pk=id)
        transaction.delete()
        return DeleteTransaction(transaction=transaction)
