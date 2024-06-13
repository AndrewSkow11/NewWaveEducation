from courses.serializers import MaterialSerializer, SectionSerializer
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from courses.models import Section, Material
from courses.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# --------------
# Material
# --------------
class MaterialCreateAPIView(CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAdminUser, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class MaterialListAPIView(ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]


class MaterialRetrieveAPIView(RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsOwner, IsAdminUser]


class MaterialUpdateAPIView(UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsOwner, IsAdminUser]


class MaterialDestroyAPIView(DestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAdminUser, IsOwner]


# --------------
# Section
# --------------
class SectionCreateAPIView(CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAdminUser, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class SectionListAPIView(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, ]


class SectionRetrieveAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsOwner, IsAdminUser]


class SectionUpdateAPIView(UpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsOwner, IsAdminUser]


class SectionDestroyAPIView(DestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAdminUser, IsOwner]
