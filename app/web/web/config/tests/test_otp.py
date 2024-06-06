# tests/test_otp.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_otp():
    client = Client(schema)
    mutation = '''
        mutation {
            createOTP(phoneNumber: "09123456789") {
                otp {
                    id
                    phoneNumber
                    code
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createOTP']['otp']['phoneNumber'] == '09123456789'
    assert len(executed['data']['createOTP']['otp']['code']) == 6


@pytest.mark.django_db
def test_validate_otp():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createOTP(phoneNumber: "09123456789") {
                otp {
                    id
                    code
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    otp_code = executed['data']['createOTP']['otp']['code']

    validate_mutation = f'''
        mutation {{
            validateOTP(phoneNumber: "09123456789", code: "{otp_code}") {{
                valid
            }}
        }}
    '''
    executed = client.execute(validate_mutation)
    assert 'errors' not in executed
    assert executed['data']['validateOTP']['valid'] == True
