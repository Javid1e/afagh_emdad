# services/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Service
from .mutations import CreateService, UpdateService, DeleteService
from .types import ServiceType


class Query(graphene.ObjectType):
    all_services = graphene.List(ServiceType)
    service = graphene.Field(ServiceType, id=graphene.Int())

    def resolve_all_services(self, info, **kwargs):
        return Service.objects.all()

    def resolve_service(self, info, id):
        return Service.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_service = CreateService.Field()
    update_service = UpdateService.Field()
    delete_service = DeleteService.Field()
