import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from .constants import AVATAR_UPLOAD_TO


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


# gender options
MALE, FEMALE, OTHER, UNKNOW = range(4)
class GenderOptions(models.IntegerChoices):
    MALE   = MALE, _('male')
    FEMALE = FEMALE, _('female')
    OTHER  = OTHER , _("other")
    UNKNOW = UNKNOW, _('unknow')

# roles
ADMIN, NORMAL_USER, GUEST = range(3)
class RoleChoices(models.IntegerChoices):
    ADMIN       = ADMIN, _('ADMIN')
    NORMAL_USER = NORMAL_USER, _('NORMAL USER')
    GUEST       = GUEST, _('GUEST')


class User(AbstractUser):
    # id with uuid
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # User permission fields
    is_verified   = models.BooleanField(default=False)
    # User information
    avatar        = models.ImageField(upload_to=AVATAR_UPLOAD_TO, max_length=511, null=True, blank=True, default=None, verbose_name="avatar")
    email         = LowercaseEmailField(verbose_name='email address', max_length=255, unique=True, db_index=True)
    first_name    = models.CharField(max_length=64, null=True, blank=True)
    last_name     = models.CharField(max_length=64, null=True, blank=True)
    address       = models.CharField(verbose_name="address", max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="date of birth", null=True, blank=True, default=None)
    gender        = models.IntegerField(verbose_name="gender", choices=GenderOptions.choices, default=GenderOptions.UNKNOW)
    phone_number  = PhoneNumberField(null=True, blank=True)
    role          = models.IntegerField(choices=RoleChoices.choices, default=RoleChoices.NORMAL_USER)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} | {self.get_full_name()}"

    def tokens(self):
        refresh_tokens = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh_tokens),
            'access': str(refresh_tokens.access_token),
        }

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
