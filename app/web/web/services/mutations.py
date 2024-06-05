# services/mutations.py
import graphene
from .models import Service
from .types import ServiceType
from django.core.exceptions import ValidationError


class CreateService(graphene.Mutation):
    service = graphene.Field(ServiceType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, name, description=None):
        service = Service(name=name, description=description)
        try:
            service.full_clean()
            service.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateService(service=service)


class UpdateService(graphene.Mutation):
    service = graphene.Field(ServiceType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name=None, description=None):
        service = Service.objects.get(pk=id)
        if name:
            service.name = name
        if description:
            service.description = description
        try:
            service.full_clean()
            service.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateService(service=service)


class DeleteService(graphene.Mutation):
    service = graphene.Field(ServiceType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        service = Service.objects.get(pk=id)
        service.delete()
        return DeleteService(service=service)
