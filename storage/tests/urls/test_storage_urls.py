from django.test import TestCase
from django.urls import reverse
from storage.models import Storage, CategoryStorage
from django.test import Client as TestClient
from django.contrib.auth.models import User


class TestStorageURL(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_superuser(username='gustavo', password='12345')  # type: ignore
        self.client = TestClient()
        self.client.login(username='gustavo', password='12345')
        return super().setUp()

    def test_if_list_storage_url_return_200(self):
        response = self.client.get(reverse('storage:storage_list'))
        self.assertEqual(response.status_code, 200)

    def test_if_create_storage_url_return_200(self):
        response = self.client.get(reverse('storage:storage_create'))
        self.assertEqual(response.status_code, 200)

    def test_if_update_storage_url_return_200(self):
        category = CategoryStorage.objects.create(name='category_teste')
        Storage.objects.create(
            name='teste', category=category
        )
        response = self.client.get(reverse('storage:storage_update', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_if_delete_storage_url_return_200(self):
        category = CategoryStorage.objects.create(name='category_teste')
        Storage.objects.create(
            name='teste', category=category
        )
        response = self.client.get(reverse('storage:storage_delete', args=(1,)))
        self.assertEqual(response.status_code, 200)
