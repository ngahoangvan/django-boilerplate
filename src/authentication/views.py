from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer


# Create your views here.
class GetUsersAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user_db = User.objects.all()
        response = self.serializer_class(user_db, many=True).data
        return Response(data={'data': response}, status=status.HTTP_200_OK)
        