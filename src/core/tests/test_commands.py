from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class TestCommands(TestCase):
    @patch("django.db.utils.ConnectionHandler.__getitem__", return_value=True)
    def test_wait_for_db_ready(self, mock):
        call_command("wait_for_db")
        self.assertEqual(mock.call_count, 1)

    @patch("core.management.commands.wait_for_db.time", return_value=True)
    def test_wait_for_db(self, mock_ts):
        with patch("django.db.utils.ConnectionHandler.__getitem__", return_value=True) as mock_gi:
            mock_gi.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            self.assertEqual(mock_gi.call_count, 6)
