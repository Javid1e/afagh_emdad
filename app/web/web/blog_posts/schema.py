# blog_posts/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import BlogPost, Comment, Like
from .mutations import CreateBlogPost, UpdateBlogPost, DeleteBlogPost, CreateComment, UpdateComment, DeleteComment, \
    CreateLike, DeleteLike
from .types import BlogPostType, CommentType, LikeType


class Query(graphene.ObjectType):
    all_blog_posts = graphene.List(BlogPostType)
    blog_post = graphene.Field(BlogPostType, id=graphene.Int())

    def resolve_all_blog_posts(self, info, **kwargs):
        return BlogPost.objects.all()

    def resolve_blog_post(self, info, id):
        return BlogPost.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    delete_blog_post = DeleteBlogPost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
    create_like = CreateLike.Field()
    delete_like = DeleteLike.Field()
