from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User
from .serializers import (LoginSerializer, LogoutSerializer,
                          RegisterSerializer, UserSerializer)

# Create your views here.

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        responses={
            201: RegisterSerializer(),
            401: 'Account with above email already exist. Please login instead.',
        })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            user_data = serializer.data
            return Response(user_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        responses={
            200: LoginSerializer(),
            401: 'Invalid login credentials. Please re-enter your email and password.'
        })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response(data={"erros": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(data={'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetUsersAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        user_db = User.objects.all()
        response = self.serializer_class(user_db, many=True).data
        return Response(data={'data': response}, status=status.HTTP_200_OK)
