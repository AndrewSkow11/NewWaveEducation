from rest_framework import serializers
from courses.models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = (
            'title',
            'description'
        )
        