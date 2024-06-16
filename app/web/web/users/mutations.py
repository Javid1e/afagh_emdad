import graphene
from graphql import GraphQLError
from django.utils.translation import gettext_lazy as _
from users.models import User
from users.serializers import RegisterSerializer
from users.types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)

    @staticmethod
    def mutate(info, name, last_name, phone_number, email, password, role):
        serializer = RegisterSerializer(data={
            'name': name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'password': password,
            'role': role
        })

        if serializer.is_valid():
            user = serializer.save()
            return CreateUser(user=user)
        else:
            raise GraphQLError(_("Error creating user: ") + str(serializer.errors))


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        last_name = graphene.String()
        phone_number = graphene.String()
        email = graphene.String()
        password = graphene.String()
        role = graphene.String()

    @staticmethod
    def mutate(info, id, name=None, last_name=None, phone_number=None, email=None, password=None, role=None):
        user = User.objects.get(pk=id)
        if name:
            user.name = name
        if last_name:
            user.last_name = last_name
        if phone_number:
            user.phone_number = phone_number
        if email:
            user.email = email
        if password:
            user.set_password(password)
        if role:
            user.role = role
        user.save()
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID(required=True)

    @staticmethod
    def mutate(info, id):
        user = User.objects.get(pk=id)
        user.delete()
        return DeleteUser(user=user)


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        phone_number = graphene.String(required=True)
        password = graphene.String(required=True)

    @staticmethod
    def mutate(info, phone_number, password):
        user = User.objects.filter(phone_number=phone_number).first()
        if user and user.check_password(password):
            return LoginUser(user=user)
        raise GraphQLError(_('Invalid credentials'))


class LogoutUser(graphene.Mutation):
    success = graphene.Boolean()

    @staticmethod
    def mutate(info):
        # Handle logout logic
        return LogoutUser(success=True)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()
    logout_user = LogoutUser.Field()
