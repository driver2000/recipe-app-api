from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class TestCommands(TestCase):
    def test_wait_for_db(self):
        pass
