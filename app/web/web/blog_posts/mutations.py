# blog_posts/mutations.py
import graphene
from .models import BlogPost
from .types import BlogPostType
from django.core.exceptions import ValidationError


class CreateBlogPost(graphene.Mutation):
    blog_post = graphene.Field(BlogPostType)

    class Arguments:
        author_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, author_id, title, content):
        blog_post = BlogPost(author_id=author_id, title=title, content=content)
        try:
            blog_post.full_clean()
            blog_post.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateBlogPost(blog_post=blog_post)


class UpdateBlogPost(graphene.Mutation):
    blog_post = graphene.Field(BlogPostType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, id, title=None, content=None):
        blog_post = BlogPost.objects.get(pk=id)
        if title:
            blog_post.title = title
        if content:
            blog_post.content = content
        try:
            blog_post.full_clean()
            blog_post.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateBlogPost(blog_post=blog_post)


class DeleteBlogPost(graphene.Mutation):
    blog_post = graphene.Field(BlogPostType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.delete()
        return DeleteBlogPost(blog_post=blog_post)
