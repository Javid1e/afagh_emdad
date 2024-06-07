from graphene_django import DjangoObjectType
from .models import Transaction


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
