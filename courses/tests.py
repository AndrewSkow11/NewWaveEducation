from rest_framework.test import APITestCase
from django.urls import reverse
from courses.models import Material, Section
from django.contrib.auth.models import User


class MaterialAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='12345')
        self.section = Section.objects.create(
            title='Test Section',
            owner=self.user)
        self.material = Material.objects.create(
            section=self.section,
            title='Test Material',
            text_content='Test Content',
            owner=self.user)

    def test_material_list(self):
        url = reverse('materials_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_material_retrieve(self):
        url = reverse('materials_retrieve', args=[self.material.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Material')

    def test_material_create(self):
        data = {"section": self.section.pk, "title": "New Material", "text_content": "New Content",
                "owner": self.user.pk}
        url = reverse('materials_create')
        self.client.force_login(self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.json(),
            {
                'detail':
                    'У вас недостаточно прав для выполнения данного действия.'}
        )


class MaterialAPITestCaseAdmin(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='12345',
            is_staff=True,
            is_superuser=True,
        )
        self.section = Section.objects.create(
            title='Test Section',
            owner=self.user)
        self.material = Material.objects.create(
            section=self.section,
            title='Test Material',
            text_content='Test Content',
            owner=self.user)

    def test_material_create(self):
        data = {"section": self.section.pk, "title": "New Material", "text_content": "New Content",
                "owner": self.user.pk}
        url = reverse('materials_create')
        self.client.force_login(self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_material_update(self):
        data = {"title": "Updated Material", "text_content": "Updated Content"}
        url = reverse('material_update', args=[self.material.pk])
        self.client.force_login(self.user)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Material')

    def test_material_destroy(self):
        url = reverse('material_destroy', args=[self.material.pk])
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
