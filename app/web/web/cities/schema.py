# cities/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import City
from .mutations import CreateCity, UpdateCity, DeleteCity
from .types import CityType


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    city = graphene.Field(CityType, id=graphene.Int())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_city(self, info, id):
        return City.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_city = CreateCity.Field()
    update_city = UpdateCity.Field()
    delete_city = DeleteCity.Field()
