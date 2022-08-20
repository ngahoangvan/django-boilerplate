from faker.providers.lorem.en_US import Provider as LoremProvider
from faker.providers.company.en_US import Provider as CompanyProvider
from faker.providers.profile import Provider as ProfileProvider
from faker.providers.python import Provider as PythonProvider
from faker.providers.address.en_US import Provider as AddressProvider
from faker.providers.date_time import Provider as DateProvider


class CommonProvider(LoremProvider, CompanyProvider, ProfileProvider,
                     PythonProvider, AddressProvider, DateProvider):
    """
    A Provider for amoda-related data

    >>> from faker import Faker
    >>> import CommonProvider
    >>> fake = Faker()
    >>> fake.add_provider(CommonProvider)
    """
    # User
    def user_first_name(self):
        return self.generator.name_male()

    def user_last_name(self):
        return self.generator.name_male()

    def user_username(self):
        return self.generator.user_name()

    def user_email(self):
        return self.generator.free_email()