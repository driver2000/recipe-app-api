import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB...")
        conn = None
        while not conn:
            try:
                conn = connections["default"]
            except OperationalError:
                self.stdout.write("DB is unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB available!"))
