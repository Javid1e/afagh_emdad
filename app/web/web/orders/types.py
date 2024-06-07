from graphene_django import DjangoObjectType
from .models import Order


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
