import factory

from .faker_common import CommonProvider


def get_provider_populated_faker():
    _faker = factory.Faker
    _faker.add_provider(CommonProvider)
    return _faker
