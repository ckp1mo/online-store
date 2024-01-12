from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@skystore.com',
            first_name='admin',
            last_name='Skystore',
            is_staff=True,
            is_superuser=True,
            avatar='users/avatar-admin.jpg'
        )
        user.set_password('qwerty321')
        user.save()
