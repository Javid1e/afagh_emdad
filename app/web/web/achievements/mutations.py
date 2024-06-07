# achievements/mutations.py
import graphene
from .models import Achievement
from .types import AchievementType
from django.core.exceptions import ValidationError


class CreateAchievement(graphene.Mutation):
    achievement = graphene.Field(AchievementType)

    class Arguments:
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, user_id, title, description=None):
        achievement = Achievement(user_id=user_id, title=title, description=description)
        try:
            achievement.full_clean()
            achievement.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateAchievement(achievement=achievement)


class UpdateAchievement(graphene.Mutation):
    achievement = graphene.Field(AchievementType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, title=None, description=None):
        achievement = Achievement.objects.get(pk=id)
        if title:
            achievement.title = title
        if description:
            achievement.description = description
        try:
            achievement.full_clean()
            achievement.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateAchievement(achievement=achievement)


class DeleteAchievement(graphene.Mutation):
    achievement = graphene.Field(AchievementType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        achievement = Achievement.objects.get(pk=id)
        achievement.delete()
        return DeleteAchievement(achievement=achievement)
