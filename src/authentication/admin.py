from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminAddForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The form to add and change user instance
    form = UserAdminChangeForm
    add_form = UserAdminAddForm

    # display on admin page
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "created_at",
        "updated_at",
    )
    list_filter = []
    fieldsets = (
        (
            "Permissions",
            {"fields": ("is_verified", "is_superuser", "is_active", "is_staff")},
        ),
        (
            "User info",
            {
                "fields": (
                    "avatar",
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                    "phone_number",
                    "address",
                    "date_of_birth",
                    "gender",
                    "role",
                )
            },
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password", "password_repeat"),
            },
        ),
    )
    search_fields = ["username"]
    ordering = ["username"]
    filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
