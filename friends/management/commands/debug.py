from django.core.management import BaseCommand


class Command(BaseCommand):
    """
        command: python manage.py debug
    """

    def handle(self, *args, **options):
        print(args, options)
