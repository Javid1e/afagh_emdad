# blog_posts/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import BlogPost, Comment
from .types import BlogPostType, CommentType
from .mutations import CreateComment, UpdateComment, DeleteComment


class Query(graphene.ObjectType):
    all_blog_posts = graphene.List(BlogPostType)
    blog_post = graphene.Field(BlogPostType, id=graphene.Int())
    all_comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, id=graphene.Int())

    def resolve_all_blog_posts(self, info, **kwargs):
        return BlogPost.objects.all()

    def resolve_blog_post(self, info, id):
        return BlogPost.objects.get(pk=id)

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_comment(self, info, id):
        return Comment.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
