from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from user.models import Users
from user.tests.factories import UserFactory


class UsersModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory(username="testuser", email="testuser@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_user_with_groups(self):
        group1 = Group.objects.create(name="Group 1")
        group2 = Group.objects.create(name="Group 2")
        user_with_groups = UserFactory(groups=[group1, group2])

        self.assertEqual(user_with_groups.groups.count(), 2)
        self.assertIn(group1, user_with_groups.groups.all())
        self.assertIn(group2, user_with_groups.groups.all())

    def test_user_with_permissions(self):
        permission1 = Permission.objects.first()
        permission2 = Permission.objects.last()

        user_with_permissions = UserFactory(user_permissions=[permission1, permission2])

        self.assertEqual(user_with_permissions.user_permissions.count(), 2)
        self.assertIn(permission1, user_with_permissions.user_permissions.all())
        self.assertIn(permission2, user_with_permissions.user_permissions.all())

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), "testuser")
