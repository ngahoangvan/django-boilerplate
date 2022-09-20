import factory

from authentication.models import User
from utils import get_provider_populated_faker

_faker = get_provider_populated_faker()


class DefaultUserFactory(factory.django.DjangoModelFactory):
    """
    Default User Factory
    """

    class Meta:
        model = User
        django_get_or_create = ("email", "username")

    username = _faker("user_username")
    password = factory.PostGenerationMethodCall("set_password", "django12345")
    email = _faker("user_email")


class DummyUserFactory(DefaultUserFactory):
    """
    Dummy Admin User Factory.
    """

    username = "dummy"
    email = "dummy@python.com"
    first_name = "dummy"
    last_name = "crash"
    password = factory.PostGenerationMethodCall("set_password", "django12345")


class ActiveUserFactory(DefaultUserFactory):
    """
    Active User Factory.
    """

    is_active = True
    is_superuser = False
