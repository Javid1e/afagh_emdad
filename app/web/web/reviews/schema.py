# reviews/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Review
from .mutations import CreateReview, UpdateReview, DeleteReview
from .types import ReviewType


class Query(graphene.ObjectType):
    all_reviews = graphene.List(ReviewType)
    review = graphene.Field(ReviewType, id=graphene.Int())

    def resolve_all_reviews(self, info, **kwargs):
        return Review.objects.all()

    def resolve_review(self, info, id):
        return Review.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    delete_review = DeleteReview.Field()
