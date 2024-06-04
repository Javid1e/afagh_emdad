# blog_posts/tasks.py
from celery import shared_task
from .models import BlogPost, Comment, Like


@shared_task
def notify_new_comment(blog_post_id, comment_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    comment = Comment.objects.get(id=comment_id)
    blog_post.author.notify(
        _("New comment on your blog post: {content}").format(content=comment.content)
    )


@shared_task
def notify_new_like(blog_post_id, like_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    like = Like.objects.get(id=like_id)
    blog_post.author.notify(
        _("Your blog post has a new like.")
    )
