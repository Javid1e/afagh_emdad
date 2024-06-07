# notifications/mutations.py
import graphene
from .models import Notification
from .types import NotificationType
from django.core.exceptions import ValidationError


class CreateNotification(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        user_id = graphene.Int(required=True)
        message = graphene.String(required=True)

    def mutate(self, info, user_id, message):
        notification = Notification(user_id=user_id, message=message)
        try:
            notification.full_clean()
            notification.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateNotification(notification=notification)


class UpdateNotification(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        id = graphene.Int(required=True)
        message = graphene.String()

    def mutate(self, info, id, message=None):
        notification = Notification.objects.get(pk=id)
        if message:
            notification.message = message
        try:
            notification.full_clean()
            notification.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateNotification(notification=notification)


class DeleteNotification(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        notification = Notification.objects.get(pk=id)
        notification.delete()
        return DeleteNotification(notification=notification)
