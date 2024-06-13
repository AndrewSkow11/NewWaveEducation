from django.test import TestCase
from rest_framework.test import APIRequestFactory
from courses.models import Section, Material
from courses.serializers import MaterialSerializer, SectionSerializer
from courses.views import MaterialListAPIView, MaterialRetrieveAPIView, SectionListAPIView, SectionRetrieveAPIView
from django.contrib.auth.models import User

class MaterialAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.section = Section.objects.create(title='Test Section')
        self.material = Material.objects.create(title='Test Material', content='Test Content', section=self.section)

    # def test_material_list_api_view(self):
    #     request = self.factory.get('/api/materials/')
    #     request.user = self.user
    #     response = MaterialListAPIView.as_view()(request)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_material_retrieve_api_view(self):
    #     request = self.factory.get(f'/api/materials/{self.material.id}/')
    #     request.user = self.user
    #     response = MaterialRetrieveAPIView.as_view()(request, pk=self.material.id)
    #     self.assertEqual(response.status_code, 200)

class SectionAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.section = Section.objects.create(title='Test Section')

    def test_section_list_api_view(self):
        request = self.factory.get('/api/sections/')
        request.user = self.user
        response = SectionListAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_section_retrieve_api_view(self):
        request = self.factory.get(f'/api/sections/{self.section.id}/')
        request.user = self.user
        response = SectionRetrieveAPIView.as_view()(request, pk=self.section.id)
        self.assertEqual(response.status_code, 200)

