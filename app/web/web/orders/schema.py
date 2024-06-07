# orders/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Order
from .mutations import CreateOrder, UpdateOrder, DeleteOrder
from .types import OrderType


class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)
    order = graphene.Field(OrderType, id=graphene.Int())

    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_order(self, info, id):
        return Order.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()
