from graphene_django import DjangoObjectType
from .models import BlogPost, Comment, Like


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
