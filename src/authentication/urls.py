from django.urls import path

from authentication.views import GetUsersAPIView

urlpatterns = [
    path('user', GetUsersAPIView.as_view(), name='Get Users')
]