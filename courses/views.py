from django.shortcuts import render
from courses.models import Section, Material
from rest_framework import generics
from courses.serializers import MaterialSerializer, SectionSerializer


class MaterialListAPIView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class SectionListAPIView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer