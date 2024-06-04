# blog_posts/models.py
from django.db import models
from ..users.models import User
from .validations import validate_content


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(validators=[validate_content])
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"


class Like(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blog_post', 'user')

    def __str__(self):
        return f"Like by {self.user.username} on {self.blog_post.title}"
