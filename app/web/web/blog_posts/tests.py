# blog_posts/tests.py
from django.test import TestCase
from users.models import User
from .models import BlogPost, Comment, Like


class BlogPostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_blog_post(self):
        blog_post = BlogPost.objects.create(title='My First Post', content='This is my first post', author=self.user)
        self.assertEqual(blog_post.title, 'My First Post')
        self.assertEqual(blog_post.content, 'This is my first post')
        self.assertEqual(blog_post.author, self.user)

    def test_create_comment(self):
        blog_post = BlogPost.objects.create(title='My First Post', content='This is my first post', author=self.user)
        comment = Comment.objects.create(blog_post=blog_post, author=self.user, content='Great post!')
        self.assertEqual(comment.blog_post, blog_post)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, 'Great post!')

    def test_create_like(self):
        blog_post = BlogPost.objects.create(title='My First Post', content='This is my first post', author=self.user)
        like = Like.objects.create(blog_post=blog_post, user=self.user)
        self.assertEqual(like.blog_post, blog_post)
        self.assertEqual(like.user, self.user)
