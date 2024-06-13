from courses.models import Section, Material
from rest_framework import generics
from courses.serializers import MaterialSerializer, SectionSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


class MaterialListAPIView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]


class MaterialRetrieveAPIView(LoginRequiredMixin, generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]


class SectionListAPIView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]


class SectionRetrieveAPIView(LoginRequiredMixin, generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]
