from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (GetUsersAPIView, LoginAPIView, LogoutAPIView,
                                  RegisterAPIView)

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name="Register"),
    path('login', LoginAPIView.as_view(), name="Login"),
    path('token/refresh', TokenRefreshView.as_view(), name='Refresh access token'),
    path('logout', LogoutAPIView.as_view(), name="Logout"),
    path('users', GetUsersAPIView.as_view(), name='Get Users')
]
