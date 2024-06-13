from accounts.permissions import IsOwnerOrStaff
from accounts.serializers import (
    UserSerializer,
    UserSerializerCreate,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.contrib.auth.models import User


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializerCreate
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrStaff]
