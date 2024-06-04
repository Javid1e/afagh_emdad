# blog_posts/apps.py
from django.apps import AppConfig


class BlogPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_posts'

    def ready(self):
        import blog_posts.signals
