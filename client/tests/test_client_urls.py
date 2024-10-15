from django.test import TestCase
from django.urls import reverse


class TestClientUrl(TestCase):
    def test_if_url_of_create_client_return_200(self):
        response = self.client.get(reverse('client:register'))

        self.assertEqual(response.status_code, 200)