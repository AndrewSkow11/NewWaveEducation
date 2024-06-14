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
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializerCreate
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrStaff]


@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)