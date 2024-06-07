# achievements/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Achievement
from .mutations import CreateAchievement, UpdateAchievement, DeleteAchievement
from .types import AchievementType


class Query(graphene.ObjectType):
    all_achievements = graphene.List(AchievementType)
    achievement = graphene.Field(AchievementType, id=graphene.Int())

    def resolve_all_achievements(self, info, **kwargs):
        return Achievement.objects.all()

    def resolve_achievement(self, info, id):
        return Achievement.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_achievement = CreateAchievement.Field()
    update_achievement = UpdateAchievement.Field()
    delete_achievement = DeleteAchievement.Field()
