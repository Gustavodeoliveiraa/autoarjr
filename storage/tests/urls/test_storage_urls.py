from django.test import TestCase
from django.urls import reverse


class TestStorageURL(TestCase):

    def test_if_url_return_200(self):
        response = self.client.get(reverse('storage:storage_create'))
        self.assertEqual(response.status_code, 200)
