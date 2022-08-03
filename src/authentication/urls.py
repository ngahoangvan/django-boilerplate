from django.urls import path
from authentication.views import (GetUsersAPIView, LoginAPIView, LogoutAPIView,
                                  RegisterAPIView)

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('users', GetUsersAPIView.as_view(), name='Get Users')
]
