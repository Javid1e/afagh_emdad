# tests/test_payments.py
import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_payment():
    client = Client(schema)
    mutation = '''
        mutation {
            createPayment(requestId: 1, amount: 1000.0) {
                payment {
                    id
                    amount
                    status
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createPayment']['payment']['amount'] == 1000.0
    assert executed['data']['createPayment']['payment']['status'] == 'pending'


@pytest.mark.django_db
def test_get_payments():
    client = Client(schema)
    query = '''
        query {
            allPayments {
                id
                amount
                status
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allPayments'], list)


@pytest.mark.django_db
def test_update_payment():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createPayment(requestId: 1, amount: 1000.0) {
                payment {
                    id
                    amount
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    payment_id = executed['data']['createPayment']['payment']['id']

    update_mutation = f'''
        mutation {{
            updatePayment(id: {payment_id}, amount: 2000.0, status: "completed") {{
                payment {{
                    id
                    amount
                    status
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updatePayment']['payment']['amount'] == 2000.0
    assert executed['data']['updatePayment']['payment']['status'] == 'completed'


@pytest.mark.django_db
def test_delete_payment():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createPayment(requestId: 1, amount: 1000.0) {
                payment {
                    id
                    amount
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    payment_id = executed['data']['createPayment']['payment']['id']

    delete_mutation = f'''
        mutation {{
            deletePayment(id: {payment_id}) {{
                payment {{
                    id
                    amount
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deletePayment']['payment']['id'] == payment_id
