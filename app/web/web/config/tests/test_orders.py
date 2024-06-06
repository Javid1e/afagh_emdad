# tests/test_orders.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_order():
    client = Client(schema)
    mutation = '''
        mutation {
            createOrder(userId: 1, description: "This is a test order") {
                order {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createOrder']['order']['description'] == 'This is a test order'
    assert executed['data']['createOrder']['order']['status'] == 'pending'


@pytest.mark.django_db
def test_get_orders():
    client = Client(schema)
    query = '''
        query {
            allOrders {
                id
                description
                status
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allOrders'], list)


@pytest.mark.django_db
def test_update_order():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createOrder(userId: 1, description: "This is a test order") {
                order {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    order_id = executed['data']['createOrder']['order']['id']

    update_mutation = f'''
        mutation {{
            updateOrder(id: {order_id}, description: "Updated order description", status: "completed") {{
                order {{
                    id
                    description
                    status
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateOrder']['order']['description'] == 'Updated order description'
    assert executed['data']['updateOrder']['order']['status'] == 'completed'


@pytest.mark.django_db
def test_delete_order():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createOrder(userId: 1, description: "This is a test order") {
                order {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    order_id = executed['data']['createOrder']['order']['id']

    delete_mutation = f'''
        mutation {{
            deleteOrder(id: {order_id}) {{
                order {{
                    id
                    description
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteOrder']['order']['id'] == order_id
