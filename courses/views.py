from django.shortcuts import render
from courses.models import Section
from rest_framework import generics
from courses.serializers import SectionSerializer

class SeactionListCreate(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
