import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from caller.tests.utils import create_user, create_contact, get_token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_detailed_view(api_client):
    user = create_user()
    contact_user = create_user('0987654321', 'Jane Doe', 'jane@example.com')
    create_contact(contact_user, '1234567890', 'John Doe', 'john@example.com')
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.get(reverse('detailed-view', kwargs={'phone_number': '1234567890'}))
    assert response.status_code == 200
    assert response.data['phone_number'] == '1234567890'
    assert response.data['name'] == 'John Doe'
    assert response.data['email'] is None


@pytest.mark.django_db
def test_detailed_view_with_email(api_client):
    user = create_user('1234567890', 'John Doe', 'john@example.com')
    contact_user = create_user('0987654321', 'Jane Doe', 'jane@example.com')
    create_contact(user, '0987654321', 'Jane Doe', 'jane@example.com')
    token = get_token(contact_user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.get(reverse('detailed-view', kwargs={'phone_number': '1234567890'}))
    assert response.status_code == 200
    assert response.data['phone_number'] == '1234567890'
    assert response.data['name'] == 'John Doe'
    assert response.data['email'] == 'john@example.com'
