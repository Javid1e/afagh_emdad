# orders/mutations.py
import graphene
from .models import Order
from .types import OrderType
from django.core.exceptions import ValidationError


class CreateOrder(graphene.Mutation):
    order = graphene.Field(OrderType)

    class Arguments:
        user_id = graphene.Int(required=True)
        total = graphene.Float(required=True)
        status = graphene.String()

    def mutate(self, info, user_id, total, status=None):
        order = Order(user_id=user_id, total=total, status=status)
        try:
            order.full_clean()
            order.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateOrder(order=order)


class UpdateOrder(graphene.Mutation):
    order = graphene.Field(OrderType)

    class Arguments:
        id = graphene.Int(required=True)
        total = graphene.Float()
        status = graphene.String()

    def mutate(self, info, id, total=None, status=None):
        order = Order.objects.get(pk=id)
        if total:
            order.total = total
        if status:
            order.status = status
        try:
            order.full_clean()
            order.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateOrder(order=order)


class DeleteOrder(graphene.Mutation):
    order = graphene.Field(OrderType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        order = Order.objects.get(pk=id)
        order.delete()
        return DeleteOrder(order=order)
