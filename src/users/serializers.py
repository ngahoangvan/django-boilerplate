from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "username",
            "groups",
            "user_permissions",
            "is_superuser",
            "is_staff",
        ]
