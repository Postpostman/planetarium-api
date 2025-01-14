from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )
        self.admin_user = self.User.objects.create_superuser(
            username="adminuser",
            email="adminuser@example.com",
            password="adminpassword123",
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_list_users_as_admin(self):
        """Test listing users as an admin."""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_list_users_as_non_admin(self):
        """Test that non-admin users cannot list users."""
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 403)


class CreateTokenViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )

    def test_create_token(self):
        """Test that a token is created for valid credentials."""
        response = self.client.post(
            "/auth/token/",
            {"username": "testuser", "password": "testpassword123"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_create_token_invalid_credentials(self):
        """Test that token creation fails with invalid credentials."""
        response = self.client.post(
            "/auth/token/",
            {"username": "testuser", "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertNotIn("token", response.data)


class ManageUserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_retrieve_user_profile(self):
        """Test retrieving the profile of the authenticated user."""
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user_profile(self):
        """Test updating the profile of the authenticated user."""
        payload = {"username": "updateduser", "email": "updateduser@example.com"}
        response = self.client.patch("/profile/", payload)
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, payload["username"])
        self.assertEqual(self.user.email, payload["email"])
