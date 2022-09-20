from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from authentication.models import User

from .serializers import UserSerializer


# Create your views here.
class GetUsersAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        user_db = User.objects.all()
        response = self.serializer_class(user_db, many=True).data
        return Response(data={"data": response}, status=status.HTTP_200_OK)


class GetMeAPIView(generics.RetrieveUpdateAPIView):
    """
    Retrieve and Update user APIs
    """

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class GetUserByIdAPIView(generics.GenericAPIView):
    """
    Get other user by user_id
    """

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(User, id=user_id)
        return Response(
            data={"data": UserSerializer(user).data}, status=status.HTTP_200_OK
        )
