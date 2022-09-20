from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginAPIView, LogoutAPIView, RegisterAPIView, WelcomeEmailView

urlpatterns = [
    path("register", RegisterAPIView.as_view(), name="register"),
    path("login", LoginAPIView.as_view(), name="login"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_access_token"),
    path("logout", LogoutAPIView.as_view(), name="logout"),
    # Render template
    path("welcome", WelcomeEmailView.as_view(), name="welcome"),
]
