import graphene
from graphene_django import DjangoObjectType
from .models import Transaction
from .mutations import CreateTransaction, UpdateTransaction, DeleteTransaction
from .types import TransactionType


class Query(graphene.ObjectType):
    all_transactions = graphene.List(TransactionType)
    transaction = graphene.Field(TransactionType, id=graphene.Int())

    def resolve_all_transactions(self, info, **kwargs):
        return Transaction.objects.all()

    def resolve_transaction(self, info, id):
        return Transaction.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_transaction = CreateTransaction.Field()
    update_transaction = UpdateTransaction.Field()
    delete_transaction = DeleteTransaction.Field()
