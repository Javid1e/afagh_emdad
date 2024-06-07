# tests/test_blog_posts.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from blog_posts.models import BlogPost
import json
from graphene_django.utils.testing import GraphQLTestCase


class BlogPostModelTest(TestCase):
    def setUp(self):
        self.author = User.objects.create(username='authoruser', email='author@example.com', phone_number='09123456789',
                                          role='client')
        self.blog_post = BlogPost.objects.create(
            title='پست وبلاگ تستی',
            content='این یک پست وبلاگ تستی است',
            author=self.author
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.blog_post.title, 'پست وبلاگ تستی')
        self.assertEqual(self.blog_post.content, 'این یک پست وبلاگ تستی است')
        self.assertEqual(self.blog_post.author.username, 'authoruser')


class BlogPostAPITest(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='authoruser', email='author@example.com',
                                               phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.author)
        self.blog_post = BlogPost.objects.create(title='پست وبلاگ تستی', content='این یک پست وبلاگ تستی است',
                                                 author=self.author)

    def test_create_blog_post(self):
        url = reverse('blogpost-list')
        data = {'title': 'پست وبلاگ جدید', 'content': 'محتوای جدید', 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'پست وبلاگ جدید')

    def test_get_blog_post(self):
        url = reverse('blogpost-detail', kwargs={'pk': self.blog_post.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog_post.title)


class BlogPostGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='authoruser', email='author@example.com',
                                               phone_number='09123456789', password='password', role='client')
        self.blog_post = BlogPost.objects.create(title='پست وبلاگ تستی', content='این یک پست وبلاگ تستی است',
                                                 author=self.author)

    def test_all_blog_posts_query(self):
        response = self.query(
            '''
            query {
                allBlogPosts {
                    title
                    content
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allBlogPosts'][0]['title'], self.blog_post.title)

    def test_create_blog_post_mutation(self):
        response = self.query(
            '''
            mutation {
                createBlogPost(title: "پست وبلاگ جدید", content: "محتوای جدید", authorId: ''' + str(self.author.id) + ''') {
                    blogPost {
                        title
                        content
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createBlogPost']['blogPost']['title'], 'پست وبلاگ جدید')
