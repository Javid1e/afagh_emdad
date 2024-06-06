# tests/test_certificates.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_certificate():
    client = Client(schema)
    mutation = '''
        mutation {
            createCertificate(userId: 1, title: "Test Certificate", description: "Certificate Description") {
                certificate {
                    id
                    title
                    description
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createCertificate']['certificate']['title'] == 'Test Certificate'
    assert executed['data']['createCertificate']['certificate']['description'] == 'Certificate Description'


@pytest.mark.django_db
def test_get_certificates():
    client = Client(schema)
    query = '''
        query {
            allCertificates {
                id
                title
                description
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allCertificates'], list)
