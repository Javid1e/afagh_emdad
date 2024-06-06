# tests/test_reviews.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_review():
    client = Client(schema)
    mutation = '''
        mutation {
            createReview(userId: 1, content: "This is a test review", rating: 5) {
                review {
                    id
                    content
                    rating
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createReview']['review']['content'] == 'This is a test review'
    assert executed['data']['createReview']['review']['rating'] == 5


@pytest.mark.django_db
def test_get_reviews():
    client = Client(schema)
    query = '''
        query {
            allReviews {
                id
                content
                rating
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allReviews'], list)


@pytest.mark.django_db
def test_update_review():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createReview(userId: 1, content: "This is a test review", rating: 5) {
                review {
                    id
                    content
                    rating
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    review_id = executed['data']['createReview']['review']['id']

    update_mutation = f'''
        mutation {{
            updateReview(id: {review_id}, content: "Updated review content", rating: 4) {{
                review {{
                    id
                    content
                    rating
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateReview']['review']['content'] == 'Updated review content'
    assert executed['data']['updateReview']['review']['rating'] == 4


@pytest.mark.django_db
def test_delete_review():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createReview(userId: 1, content: "This is a test review", rating: 5) {
                review {
                    id
                    content
                    rating
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    review_id = executed['data']['createReview']['review']['id']

    delete_mutation = f'''
        mutation {{
            deleteReview(id: {review_id}) {{
                review {{
                    id
                    content
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteReview']['review']['id'] == review_id
