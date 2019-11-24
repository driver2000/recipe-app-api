from django.contrib.auth import get_user_model
from django.test import TestCase


class TestModel(TestCase):
    def test_create_user_with_email(self):
        email = "test@foo.com"
        password = "verysecure123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = "test@FOO.com"
        user = get_user_model().objects.create_user(email, "123")
        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "pass123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser("test@super.com", "pass123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
