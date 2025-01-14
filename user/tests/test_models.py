from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


class UserModelTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )

    def test_user_creation(self):
        """Test that a user is created successfully."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.check_password("testpassword123"))

    def test_user_group_assignment(self):
        """Test that groups can be assigned to the user."""
        group = Group.objects.create(name="Test Group")
        self.user.groups.add(group)
        self.assertIn(group, self.user.groups.all())

    def test_user_permission_assignment(self):
        """Test that permissions can be assigned to the user."""
        permission = Permission.objects.first()
        self.user.user_permissions.add(permission)
        self.assertIn(permission, self.user.user_permissions.all())

    def test_custom_related_name_for_groups(self):
        """Test the custom related name for groups."""
        group = Group.objects.create(name="Custom Group")
        self.user.groups.add(group)
        self.assertIn(self.user, group.custom_user_set.all())

    def test_custom_related_name_for_permissions(self):
        """Test the custom related name for permissions."""
        permission = Permission.objects.first()
        self.user.user_permissions.add(permission)
        self.assertIn(self.user, permission.custom_user_set.all())

    def test_string_representation(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), self.user.username)

    def test_superuser_creation(self):
        """Test that a superuser is created successfully."""
        superuser = self.User.objects.create_superuser(
            username="adminuser",
            email="adminuser@example.com",
            password="adminpassword123",
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
