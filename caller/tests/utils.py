from rest_framework_simplejwt.tokens import RefreshToken
from caller.models.user import User
from caller.models.contact import Contact


def create_user(phone_number='1234567890', name='John Doe', email='john@example.com', password='password'):
    user = User.objects.create_user(
        phone_number=phone_number,
        password=password,
        name=name,
        email=email
    )
    return user


def create_contact(user, phone_number, name, email):
    contact = Contact.objects.create(
        user=user,
        phone_number=phone_number,
        name=name,
        email=email
    )
    return contact


def get_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
