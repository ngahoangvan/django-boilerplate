from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import (LoginSerializer, LogoutSerializer,
                          RegisterSerializer, UserSerializer)

# Create your views here.

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"erros": str(e)})


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)


class GetUsersAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        user_db = User.objects.all()
        response = self.serializer_class(user_db, many=True).data
        return Response(data={'data': response}, status=status.HTTP_200_OK)
