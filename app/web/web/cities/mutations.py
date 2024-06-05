# cities/mutations.py
import graphene
from .models import City
from .types import CityType
from django.core.exceptions import ValidationError


class CreateCity(graphene.Mutation):
    city = graphene.Field(CityType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        city = City(name=name)
        try:
            city.full_clean()
            city.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateCity(city=city)


class UpdateCity(graphene.Mutation):
    city = graphene.Field(CityType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    def mutate(self, info, id, name=None):
        city = City.objects.get(pk=id)
        if name:
            city.name = name
        try:
            city.full_clean()
            city.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateCity(city=city)


class DeleteCity(graphene.Mutation):
    city = graphene.Field(CityType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        city = City.objects.get(pk=id)
        city.delete()
        return DeleteCity(city=city)
