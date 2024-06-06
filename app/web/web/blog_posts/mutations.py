# blog_posts/mutations.py
import graphene
from graphene_django import DjangoObjectType
from .models import Comment
from .types import CommentType


class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        post_id = graphene.Int(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, post_id, content):
        comment = Comment(post_id=post_id, content=content)
        comment.save()
        return CreateComment(comment=comment)


class UpdateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        id = graphene.Int(required=True)
        content = graphene.String()

    def mutate(self, info, id, content):
        comment = Comment.objects.get(pk=id)
        if content:
            comment.content = content
        comment.save()
        return UpdateComment(comment=comment)


class DeleteComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return DeleteComment(comment=comment)
