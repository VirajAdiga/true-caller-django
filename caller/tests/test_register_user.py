import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from caller.models.user import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_register_user(api_client):
    response = api_client.post(reverse('register'), {
        'name': 'testuser',
        'phone_number': '1234567890',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert User.objects.filter(name='testuser').exists()
