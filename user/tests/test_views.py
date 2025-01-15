from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = "testuser"
    email = "testuser@example.com"
    password = "testpassword123"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override to handle password hashing."""
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class UserViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin_user = UserFactory(username="adminuser", email="admin@example.com", is_staff=True, is_superuser=True)

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_list_users_as_admin(self):
        """Test that an admin user can list all users."""
        self.client.force_authenticate(user=self.admin_user)
        url = reverse("user-list")  # Adjust the name to match your route
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_list_users_as_non_admin(self):
        """Test that a non-admin user cannot list users."""
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


class CreateTokenViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

    def test_create_token(self):
        """Test that a token is created for valid credentials."""
        url = reverse("token_obtain")
        response = self.client.post(
            url,
            {"username": self.user.username, "password": "testpassword123"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_create_token_invalid_credentials(self):
        """Test that token creation fails with invalid credentials."""
        url = reverse("token_obtain")
        response = self.client.post(
            url,
            {"username": self.user.username, "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertNotIn("token", response.data)


class ManageUserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()


        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_retrieve_user_profile(self):
        """Test retrieving the authenticated user's profile."""
        url = reverse("user-profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user_profile(self):
        """Test updating the authenticated user's profile."""
        url = reverse("user-profile")
        payload = {"username": "updateduser", "email": "updateduser@example.com"}
        response = self.client.patch(url, payload)
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, payload["username"])
        self.assertEqual(self.user.email, payload["email"])
