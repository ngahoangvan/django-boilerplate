from django.urls import path

from .views import GetMeAPIView, GetUserByIdAPIView, GetUsersAPIView

urlpatterns = [
    path("list", GetUsersAPIView.as_view(), name="Get list user"),
    path("me", GetMeAPIView.as_view(), name="Retrive and Update ME"),
    path("<uuid:user_id>", GetUserByIdAPIView.as_view(), name="Get user by user_id"),
]
