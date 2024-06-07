# reviews/mutations.py
import graphene
from .models import Review
from .types import ReviewType
from django.core.exceptions import ValidationError


class CreateReview(graphene.Mutation):
    review = graphene.Field(ReviewType)

    class Arguments:
        user_id = graphene.Int(required=True)
        rating = graphene.Int(required=True)
        comment = graphene.String()

    def mutate(self, info, user_id, rating, comment=None):
        review = Review(user_id=user_id, rating=rating, comment=comment)
        try:
            review.full_clean()
            review.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateReview(review=review)


class UpdateReview(graphene.Mutation):
    review = graphene.Field(ReviewType)

    class Arguments:
        id = graphene.Int(required=True)
        rating = graphene.Int()
        comment = graphene.String()

    def mutate(self, info, id, rating=None, comment=None):
        review = Review.objects.get(pk=id)
        if rating:
            review.rating = rating
        if comment:
            review.comment = comment
        try:
            review.full_clean()
            review.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateReview(review=review)


class DeleteReview(graphene.Mutation):
    review = graphene.Field(ReviewType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        review = Review.objects.get(pk=id)
        review.delete()
        return DeleteReview(review=review)
