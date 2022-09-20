from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if email is None:
            raise serializers.ValidationError("User must have a valid email")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data, username="Unknow User")


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=5)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "password", "tokens"]

    def get_tokens(self, obj):
        user = User.objects.get(email=obj["email"])
        tokens = user.tokens()
        return {
            "refresh_token": str(tokens["refresh"]),
            "access_token": str(tokens["access"]),
        }

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed(
                "Invalid login credentials. Please check your email and password."
            )
        if not user.is_active:
            raise AuthenticationFailed("Your account is disabled")

        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {"bad_token": "Invalid or expired token"}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=255, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["password", "token", "uidb64"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            token = attrs.get("token")
            uidb64 = attrs.get("uidb64")
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed(
                    "Invalid or expired password reset link.", 401
                )

            user.set_password(password)
            user.save()

            return user
        except Exception:
            raise AuthenticationFailed("Invalid or expired password reset link.", 401)


class WelcomeEmailSerializer(serializers.Serializer):
    pass
