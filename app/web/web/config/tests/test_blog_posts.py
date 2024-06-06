# tests/test_blog_posts.py
import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_blog_post():
    client = Client(schema)
    mutation = '''
        mutation {
            createBlogPost(userId: 1, title: "Test Blog Post", content: "Blog Post Content") {
                blogPost {
                    id
                    title
                    content
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createBlogPost']['blogPost']['title'] == 'Test Blog Post'
    assert executed['data']['createBlogPost']['blogPost']['content'] == 'Blog Post Content'


@pytest.mark.django_db
def test_get_blog_posts():
    client = Client(schema)
    query = '''
        query {
            allBlogPosts {
                id
                title
                content
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allBlogPosts'], list)
