from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving
    """
    def to_python(self, value):
        value = super(LowercaseEmailField, self).to_python(value=value)
        if isinstance(value, str):
            return value.lower()
        return value


class UserManager():
    pass


class Test():
    pass