import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tests.authentication.factories import ActiveUserFactory


class TestAuthenticationViewUnauthenticated(APITestCase):
    @pytest.mark.django_db
    def setUp(self):
        super().setUp()

        # Create new account
        self.new_user = ActiveUserFactory(password="default_password")

    def test_can_login_with_username_and_password(self):
        """
        This test ensures that user can login with username and password.
        """
        # username = self.new_user.username
        email = self.new_user.email
        url = reverse("login")
        response = self.client.post(
            url, {"email": email, "password": "default_password"}, format="json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["tokens"]["refresh_token"] is not None
        assert response.data["tokens"]["access_token"] is not None
