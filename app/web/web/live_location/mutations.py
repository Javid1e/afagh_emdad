# live_location/mutations.py
import graphene
from .models import LiveLocation
from .types import LiveLocationType
from django.core.exceptions import ValidationError


class CreateLiveLocation(graphene.Mutation):
    live_location = graphene.Field(LiveLocationType)

    class Arguments:
        request_id = graphene.Int(required=True)
        latitude = graphene.Float(required=True)
        longitude = graphene.Float(required=True)

    def mutate(self, info, request_id, latitude, longitude):
        live_location = LiveLocation(request_id=request_id, latitude=latitude, longitude=longitude)
        try:
            live_location.full_clean()
            live_location.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateLiveLocation(live_location=live_location)


class UpdateLiveLocation(graphene.Mutation):
    live_location = graphene.Field(LiveLocationType)

    class Arguments:
        id = graphene.Int(required=True)
        latitude = graphene.Float()
        longitude = graphene.Float()

    def mutate(self, info, id, latitude=None, longitude=None):
        live_location = LiveLocation.objects.get(pk=id)
        if latitude:
            live_location.latitude = latitude
        if longitude:
            live_location.longitude = longitude
        try:
            live_location.full_clean()
            live_location.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateLiveLocation(live_location=live_location)


class DeleteLiveLocation(graphene.Mutation):
    live_location = graphene.Field(LiveLocationType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        live_location = LiveLocation.objects.get(pk=id)
        live_location.delete()
        return DeleteLiveLocation(live_location=live_location)
