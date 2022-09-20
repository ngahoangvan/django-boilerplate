import pytest

from tests.authentication.factories import (
    ActiveUserFactory,
    DefaultUserFactory,
    DummyUserFactory,
)


@pytest.fixture
def default_user():
    return DefaultUserFactory(is_superuser=False, is_staff=False)


@pytest.fixture
def active_user():
    return ActiveUserFactory()


@pytest.fixture
def dummy_user():
    return DummyUserFactory()


@pytest.fixture(scope="class")
def _class_scoped_dummy_user():
    return DummyUserFactory()


@pytest.mark.usefixtures("_class_scoped_dummy_user")
@pytest.fixture(scope="class")
def dummy_user_class(request, _class_scoped_dummy_user):
    # set a class attribute on the invoking test context
    request.cls.user = _class_scoped_dummy_user


@pytest.mark.usefixtures("default_user")
@pytest.fixture
def default_user_class(request, default_user):
    request.cls.user = default_user
