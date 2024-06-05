# cars/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Car
from .mutations import CreateCar, UpdateCar, DeleteCar
from .types import CarType


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    car = graphene.Field(CarType, id=graphene.Int())

    def resolve_all_cars(self, info, **kwargs):
        return Car.objects.all()

    def resolve_car(self, info, id):
        return Car.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()
    delete_car = DeleteCar.Field()
