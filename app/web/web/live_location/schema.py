# live_location/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import LiveLocation
from .mutations import CreateLiveLocation, UpdateLiveLocation, DeleteLiveLocation
from .types import LiveLocationType


class Query(graphene.ObjectType):
    all_live_locations = graphene.List(LiveLocationType)
    live_location = graphene.Field(LiveLocationType, id=graphene.Int())

    def resolve_all_live_locations(self, info, **kwargs):
        return LiveLocation.objects.all()

    def resolve_live_location(self, info, id):
        return LiveLocation.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_live_location = CreateLiveLocation.Field()
    update_live_location = UpdateLiveLocation.Field()
    delete_live_location = DeleteLiveLocation.Field()
