# roles/mutations.py
import graphene
from .models import Role
from .types import RoleType
from django.core.exceptions import ValidationError


class CreateRole(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        name = graphene.String(required=True)
        permissions = graphene.List(graphene.String)

    def mutate(self, info, name, permissions=None):
        role = Role(name=name)
        if permissions:
            role.permissions.set(permissions)
        try:
            role.full_clean()
            role.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateRole(role=role)


class UpdateRole(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        permissions = graphene.List(graphene.String)

    def mutate(self, info, id, name=None, permissions=None):
        role = Role.objects.get(pk=id)
        if name:
            role.name = name
        if permissions:
            role.permissions.set(permissions)
        try:
            role.full_clean()
            role.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateRole(role=role)


class DeleteRole(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        role = Role.objects.get(pk=id)
        role.delete()
        return DeleteRole(role=role)
