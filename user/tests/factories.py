import factory
from django.contrib.auth.models import Group, Permission
from user.models import Users


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Users

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    is_active = True
    is_staff = False

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.groups.add(*extracted)

    @factory.post_generation
    def user_permissions(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.user_permissions.add(*extracted)
