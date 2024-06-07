# requests/mutations.py
import graphene
from .models import Request
from .types import RequestType
from django.core.exceptions import ValidationError


class CreateRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        client_id = graphene.Int(required=True)
        rescuer_id = graphene.Int()
        status = graphene.String()
        location = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, client_id, location, rescuer_id=None, status=None, description=None):
        request = Request(client_id=client_id, location=location, rescuer_id=rescuer_id, status=status,
                          description=description)
        try:
            request.full_clean()
            request.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateRequest(request=request)


class UpdateRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        id = graphene.Int(required=True)
        status = graphene.String()
        location = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, status=None, location=None, description=None):
        request = Request.objects.get(pk=id)
        if status:
            request.status = status
        if location:
            request.location = location
        if description:
            request.description = description
        try:
            request.full_clean()
            request.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateRequest(request=request)


class DeleteRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        request = Request.objects.get(pk=id)
        request.delete()
        return DeleteRequest(request=request)
