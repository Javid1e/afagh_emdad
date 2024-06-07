# blog_posts/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BlogPost, Comment, Like
from .tasks import notify_new_comment, notify_new_like


@receiver(post_save, sender=Comment)
def notify_comment_on_create(sender, instance, created, **kwargs):
    if created:
        notify_new_comment.delay(instance.blog_post.id, instance.id)


@receiver(post_save, sender=Like)
def notify_like_on_create(sender, instance, created, **kwargs):
    if created:
        notify_new_like.delay(instance.blog_post.id, instance.id)
