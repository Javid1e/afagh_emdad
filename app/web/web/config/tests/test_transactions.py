# tests/test_transactions.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_transaction():
    client = Client(schema)
    mutation = '''
        mutation {
            createTransaction(userId: 1, amount: 100.0, description: "Test Transaction") {
                transaction {
                    id
                    amount
                    description
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createTransaction']['transaction']['amount'] == 100.0
    assert executed['data']['createTransaction']['transaction']['description'] == 'Test Transaction'


@pytest.mark.django_db
def test_get_transactions():
    client = Client(schema)
    query = '''
        query {
            allTransactions {
                id
                amount
                description
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allTransactions'], list)
