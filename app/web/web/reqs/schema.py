# reqs/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Request
from .mutations import CreateRequest, UpdateRequest, DeleteRequest
from .types import RequestType


class Query(graphene.ObjectType):
    all_requests = graphene.List(RequestType)
    request = graphene.Field(RequestType, id=graphene.Int())

    def resolve_all_requests(self, info, **kwargs):
        return Request.objects.all()

    def resolve_request(self, info, id):
        return Request.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
    update_request = UpdateRequest.Field()
    delete_request = DeleteRequest.Field()
