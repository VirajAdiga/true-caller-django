import random
from django.core.management.base import BaseCommand
from faker import Faker
from caller.models import User, Contact, SpamReport


class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create users
        for _ in range(100):
            user = User.objects.create_user(
                phone_number=fake.phone_number()[:15],
                password='password',
                name=fake.name()[:255],
                email=fake.email()
            )

            # Create contacts for each user
            for _ in range(random.randint(0, 10)):
                Contact.objects.create(
                    user=user,
                    name=fake.name()[:255],
                    phone_number=fake.phone_number()[:15],
                    email=fake.email()
                )

            # Create spam reports
            for _ in range(random.randint(0, 5)):
                SpamReport.objects.create(
                    phone_number=fake.phone_number()[:15],
                    reported_by=user,
                    reason=fake.text()
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data'))
