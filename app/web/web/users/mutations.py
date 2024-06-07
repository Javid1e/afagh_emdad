import graphene
from .models import User
from .types import UserType
from django.core.exceptions import ValidationError


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, email, phone_number, password):
        user = User(username=username, email=email, phone_number=phone_number)
        user.set_password(password)
        try:
            user.full_clean()
            user.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()

    def mutate(self, info, id, username=None, email=None, phone_number=None):
        user = User.objects.get(pk=id)
        if username:
            user.username = username
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number
        try:
            user.full_clean()
            user.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        user = User.objects.get(pk=id)
        user.delete()
        return DeleteUser(user=user)
