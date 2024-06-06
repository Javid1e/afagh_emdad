# tests/test_faqs.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_faq():
    client = Client(schema)
    mutation = '''
        mutation {
            createFAQ(question: "Test FAQ", answer: "FAQ Answer") {
                faq {
                    id
                    question
                    answer
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createFAQ']['faq']['question'] == 'Test FAQ'
    assert executed['data']['createFAQ']['faq']['answer'] == 'FAQ Answer'


@pytest.mark.django_db
def test_get_faqs():
    client = Client(schema)
    query = '''
        query {
            allFAQs {
                id
                question
                answer
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allFAQs'], list)
