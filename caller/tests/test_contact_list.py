import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from caller.tests.utils import create_user, create_contact, get_token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_contact_list(api_client):
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    create_contact(user, '0987654321', 'Jane Doe', 'jane@example.com')

    response = api_client.get(reverse('contact-list'))
    assert response.status_code == 200
    assert len(response.data.get('results')) > 0
    assert response.data.get('results')[0]['name'] == 'Jane Doe'
